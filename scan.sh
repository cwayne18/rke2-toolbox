#!/bin/bash

# Output file to store the Trivy scan reports
output_file="trivy_scan_report.txt"
db_file="${SCAN_STATS_DB_PATH:-reports/scan_metrics.db}"
branch=""
pr_input=""
gist_title=""
use_prime_ingress="false"
release_version=""

usage() {
    echo "Usage: $0 [branch] [--pr <pr-number|pr-url>] [--release <version>] [--gist <title>] [--prime]"
    echo ""
    echo "Examples:"
    echo "  $0"
    echo "  $0 release-1.32"
    echo "  $0 --pr 9994"
    echo "  $0 --pr https://github.com/rancher/rke2/pull/9994"
    echo "  $0 --release v1.36.1-rc1-rke2r1"
    echo "  $0 --release v1.36.1+rke2r1"
    echo "  $0 --prime"
    echo "  $0 --gist 'My Scan Results'"
}

while [[ $# -gt 0 ]]; do
    case "$1" in
        -p|--pr)
            if [[ -z "$2" ]]; then
                echo "Error: --pr requires a value"
                usage
                exit 1
            fi
            pr_input="$2"
            shift 2
            ;;
        -g|--gist)
            if [[ -z "$2" ]]; then
                echo "Error: --gist requires a title value"
                usage
                exit 1
            fi
            gist_title="$2"
            shift 2
            ;;
        -r|--release)
            if [[ -z "$2" ]]; then
                echo "Error: --release requires a version value"
                usage
                exit 1
            fi
            release_version="$2"
            shift 2
            ;;
        --prime)
            use_prime_ingress="true"
            shift
            ;;
        -h|--help)
            usage
            exit 0
            ;;
        *)
            # Backward-compatible positional branch argument.
            if [[ -z "$branch" ]]; then
                branch="$1"
                shift
            else
                echo "Error: Unknown argument '$1'"
                usage
                exit 1
            fi
            ;;
    esac
done

if [[ -z "$branch" ]]; then
    branch="master"
fi

# Validate mutually exclusive flags
if [[ -n "$release_version" && -n "$pr_input" ]]; then
    echo "Error: --release and --pr cannot be used together"
    usage
    exit 1
fi

if [[ -n "$release_version" ]]; then
    # Normalize release version: convert "-rke2rN" suffix to "+rke2rN" so the
    # tag matches GitHub's release naming. URL-encode the '+' as '%2B'.
    release_tag="$release_version"
    if [[ "$release_tag" =~ ^(.*)-rke2r([0-9]+)$ ]]; then
        release_tag="${BASH_REMATCH[1]}+rke2r${BASH_REMATCH[2]}"
    fi
    release_tag_url="${release_tag//+/%2B}"
    source_desc="release ${release_tag}"
elif [[ -n "$pr_input" ]]; then
    if [[ "$pr_input" =~ ^[0-9]+$ ]]; then
        pr_number="$pr_input"
    elif [[ "$pr_input" =~ github\.com/rancher/rke2/pull/([0-9]+) ]]; then
        pr_number="${BASH_REMATCH[1]}"
    else
        echo "Error: --pr value must be a PR number or Rancher rke2 PR URL"
        usage
        exit 1
    fi

    ref_path="refs/pull/${pr_number}/head"
    source_desc="PR #${pr_number}"
    
    # Fetch PR head SHA and head branch for artifact lookup
    pr_info_output=$(gh pr view "$pr_number" -R rancher/rke2 --json headRefOid,headRefName,headRepositoryOwner 2>&1)
    pr_info_exit=$?
    if [[ $pr_info_exit -ne 0 ]]; then
        echo "Error fetching PR info: $pr_info_output"
        pr_head_sha=""
        pr_head_ref=""
    else
        pr_head_sha=$(echo "$pr_info_output" | grep -oE '"headRefOid":\s*"[^"]+"' | sed 's/.*"\([^"]*\)"$/\1/')
        pr_head_ref=$(echo "$pr_info_output" | grep -oE '"headRefName":\s*"[^"]+"' | sed 's/.*"\([^"]*\)"$/\1/')
        echo "PR head SHA: $pr_head_sha"
        echo "PR head ref: $pr_head_ref"
    fi
else
    ref_path="refs/heads/${branch}"
    source_desc="branch '${branch}'"
fi

# Canonical source reference recorded with the scan. Used both for the metrics
# DB row and for the metadata comment embedded in the report so HTML rendering
# can group the CVE trend chart by scan type (branch / release / PR).
source_ref="${ref_path:-release:${release_tag}}"

# Clear files if they already exist
rm -f "$output_file"
rm -f images.txt
rm -f images-optional.txt

echo "Scanning using ${source_desc} (${ref_path:-release tag $release_tag})"

# Always set up a work_dir + cleanup so the trap is consistent
work_dir=$(mktemp -d)
cleanup() {
    rm -rf "$work_dir"
    rm -f rancher.openvex.json
}
trap cleanup EXIT

if [[ -n "$release_version" ]]; then
    # Release mode: download the published images list directly from the GitHub release
    release_url="https://github.com/rancher/rke2/releases/download/${release_tag_url}/rke2-images.linux-amd64.txt"
    echo "Downloading release images list from: $release_url"
    if ! curl -fsSL "$release_url" -o images.txt; then
        echo "Error: Failed to download release images list from $release_url"
        echo "       Verify that the release tag '${release_tag}' exists at https://github.com/rancher/rke2/releases"
        exit 1
    fi
    
    if [[ ! -s images.txt ]]; then
        echo "Error: Downloaded release images list is empty"
        exit 1
    fi
    
    echo "Downloaded $(wc -l < images.txt | tr -d ' ') images from release ${release_tag}"
else
    # Build-from-source mode: execute the upstream build-images script in a temp sandbox
    # and use the generated image lists.
    mkdir -p "$work_dir/scripts" "$work_dir/bin" "$work_dir/build"

    raw_repo="rancher/rke2"
    raw_ref="$ref_path"

    download_build_scripts() {
        curl -fsSL "https://raw.githubusercontent.com/${raw_repo}/${raw_ref}/scripts/version.sh" \
            -o "$work_dir/scripts/version.sh" 2>/dev/null \
        && curl -fsSL "https://raw.githubusercontent.com/${raw_repo}/${raw_ref}/scripts/build-images" \
            -o "$work_dir/scripts/build-images" 2>/dev/null
    }

    if ! download_build_scripts; then
        if [[ -n "$pr_input" ]]; then
            echo "Unable to fetch scripts via ${raw_repo}/${raw_ref}; resolving PR head via GitHub API..."
            if ! pr_json=$(curl -fsSL "https://api.github.com/repos/rancher/rke2/pulls/${pr_number}" 2>/dev/null); then
                echo "Error: PR #${pr_number} not found or inaccessible in rancher/rke2"
                exit 1
            fi

            pr_head_repo=$(printf '%s' "$pr_json" | perl -0777 -ne 'if (/"head"\s*:\s*\{.*?"repo"\s*:\s*\{.*?"full_name"\s*:\s*"([^"]+)"/s) { print $1; }')
            pr_head_sha=$(printf '%s' "$pr_json" | perl -0777 -ne 'if (/"head"\s*:\s*\{.*?"sha"\s*:\s*"([0-9a-f]{40})"/s) { print $1; }')

            if [[ -z "$pr_head_repo" || -z "$pr_head_sha" ]]; then
                echo "Error: could not parse head repo/SHA for PR #${pr_number}"
                exit 1
            fi

            raw_repo="$pr_head_repo"
            raw_ref="$pr_head_sha"
            source_desc="PR #${pr_number} (${raw_repo}@${raw_ref})"
            echo "Retrying with ${source_desc}"

            if ! download_build_scripts; then
                echo "Error: failed to fetch scripts for PR #${pr_number} from ${raw_repo}@${raw_ref}"
                exit 1
            fi
        else
            echo "Error: failed to fetch scripts for ${source_desc} (${ref_path})"
            exit 1
        fi
    fi

    chmod +x "$work_dir/scripts/build-images"

    if [[ "$use_prime_ingress" == "true" ]]; then
        ingress_nginx_hardened_tag=$(sed -n 's/^INGRESS_NGINX_HARDENED_TAG=//p' "$work_dir/scripts/build-images" | head -n 1)
        ingress_nginx_prime_tag=$(sed -n 's/^INGRESS_NGINX_PRIME_TAG=//p' "$work_dir/scripts/build-images" | head -n 1)

        if [[ -z "$ingress_nginx_hardened_tag" || -z "$ingress_nginx_prime_tag" ]]; then
            echo "Error: failed to determine ingress-nginx hardened/prime tags from build-images"
            exit 1
        fi
    fi

    cat <<'EOF' > "$work_dir/bin/git"
#!/bin/sh
case "$1" in
    rev-parse)
        echo deadbeefdeadbeefdeadbeefdeadbeefdeadbeef
        ;;
    diff|status|tag)
        exit 0
        ;;
    log)
        echo deadbeefdeadbeefdeadbeefdeadbeefdeadbeef someone@example.com
        ;;
    *)
        exit 0
        ;;
esac
EOF
    chmod +x "$work_dir/bin/git"

    if ! PATH="$work_dir/bin:$PATH" \
        GOARCH="${GOARCH:-$(go env GOARCH)}" \
        GOOS="${GOOS:-$(go env GOOS)}" \
        BUILD_DIR="$work_dir/build" \
        SKIP_BUILD_IMAGE_RUNTIME=1 \
        PULL_CMD=echo \
        PULL_CMD_CORE=echo \
        bash "$work_dir/scripts/build-images" \
        > /dev/null 2> "$work_dir/build-images.log"; then
        cat "$work_dir/build-images.log"
        exit 1
    fi

    if [[ "$use_prime_ingress" == "true" ]]; then
        ingress_images_file="$work_dir/build/images-ingress-nginx.txt"

        if [[ ! -f "$ingress_images_file" ]]; then
            echo "Error: expected ingress-nginx image list was not generated"
            exit 1
        fi

        sed -i.bak "s/:${ingress_nginx_hardened_tag}$/:${ingress_nginx_prime_tag}/" "$ingress_images_file"
        rm -f "${ingress_images_file}.bak"
    fi


    # Optional (non-default) image groups. These add-on images are NOT shipped in
    # the default RKE2 airgap tarball (images-core + images-canal), but we still
    # want to scan them. They are reported in a separate, clearly delineated
    # section so it is obvious they are not part of the default install.
    optional_groups="cilium calico vsphere multus harvester"

    optional_files=()
    find_default_exclude=( ! -name 'images.txt' )
    for grp in $optional_groups; do
        grp_file="$work_dir/build/images-${grp}.txt"
        [[ -f "$grp_file" ]] && optional_files+=("$grp_file")
        # Exclude the optional group's list file from the default image list so
        # those images are reported only in the optional section. Matching is by
        # file name (not image reference) so default images such as
        # hardened-calico in images-canal.txt are not accidentally dropped.
        find_default_exclude+=( ! -name "images-${grp}.txt" )
    done

    # Default image list: every generated list EXCEPT the optional group files.
    # The historical "mirrored-" passthrough exclusion is preserved so the
    # default report keeps reflecting the default install set.
    find "$work_dir/build" -maxdepth 1 -type f -name 'images-*.txt' \
        "${find_default_exclude[@]}" -print0 \
        | xargs -0 cat \
        | grep -vE 'mirrored' \
        | awk 'NF && !seen[$0]++' \
        > images.txt

    # Optional image list: the union of the optional group files, de-duplicated
    # and with any image already present in the default list removed so nothing
    # is scanned twice.
    : > images-optional.txt
    if (( ${#optional_files[@]} > 0 )); then
        cat "${optional_files[@]}" \
            | awk 'NF && !seen[$0]++' \
            | { grep -vxF -f images.txt || true; } \
            > images-optional.txt
    fi
fi

# Ensure the optional list exists even in release mode (no per-group breakdown
# is available for a published release tarball, so it stays empty).
[[ -f images-optional.txt ]] || : > images-optional.txt

# When --prime is set, rewrite image references to use registry.rancher.com instead
# of docker.io (or no registry prefix, which implicitly means docker.io).
if [[ "$use_prime_ingress" == "true" ]]; then
    rewrite_registry_prime() {
        local target="$1"
        [[ -s "$target" ]] || return 0
        awk '
            {
                line = $0
                if (line == "") { print; next }
                sub(/^docker\.io\//, "registry.rancher.com/", line)
                # If still has no registry (no "." or ":" in the first path segment), prepend.
                n = index(line, "/")
                first = (n > 0) ? substr(line, 1, n - 1) : line
                if (first !~ /[.:]/) {
                    line = "registry.rancher.com/" line
                }
                print line
            }
        ' "$target" > "${target}.tmp" && mv "${target}.tmp" "$target"
    }

    rewrite_registry_prime images.txt
    rewrite_registry_prime images-optional.txt
fi

# Input file containing the list of Docker images
input_file="./images.txt"
# Input file containing the list of optional (non-default) add-on images
optional_input_file="./images-optional.txt"

# The rke2-runtime image is only built and published during a real CI run; for an
# unreleased build (a branch tip or a PR head) it never exists in a registry, so a
# plain `trivy image rancher/rke2-runtime:<dev-version>` cannot pull anything. To
# scan it we download the prebuilt image tarball from the source's latest CI run and
# scan it directly. Release scans are skipped here because the runtime image is
# published to the registry alongside the release and is scanned like any other image.
#
# Determine where to look for the runtime artifact: a PR head (SHA + branch) or, for a
# plain branch scan, the branch tip on rancher/rke2.
pr_runtime_tar=""
keep_artifact_dir=""
runtime_lookup_sha=""
runtime_lookup_ref=""
runtime_lookup_desc=""
if [[ -n "$pr_number" ]]; then
    runtime_lookup_sha="$pr_head_sha"
    runtime_lookup_ref="$pr_head_ref"
    runtime_lookup_desc="PR #${pr_number}"
elif [[ -z "$release_version" ]]; then
    runtime_lookup_ref="$branch"
    runtime_lookup_desc="branch '${branch}'"
fi

if [[ -n "$runtime_lookup_sha" || -n "$runtime_lookup_ref" ]]; then
    echo "Fetching workflow runs for ${runtime_lookup_desc}..."

    candidate_run_ids=""

        # Get all completed runs matching the head SHA, when known.
        if [[ -n "$runtime_lookup_sha" ]]; then
            sha_run_ids=$(gh run list -R rancher/rke2 -s completed --limit 100 --json databaseId,headSha,name --jq ".[] | select(.headSha==\"$runtime_lookup_sha\") | .databaseId" 2>/dev/null)
            candidate_run_ids="$candidate_run_ids $sha_run_ids"
        fi

        # Also try matching by branch name (covers branch scans and PR cases where the
        # SHA differs, e.g. a merge commit).
        if [[ -n "$runtime_lookup_ref" ]]; then
            branch_run_ids=$(gh run list -R rancher/rke2 -s completed -b "$runtime_lookup_ref" --limit 50 --json databaseId --jq '.[].databaseId' 2>/dev/null)
            candidate_run_ids="$candidate_run_ids $branch_run_ids"
        fi

        # For PRs, also try associated workflow runs via the GitHub API (matches PR by event).
        if [[ -n "$pr_number" ]]; then
            api_run_ids=$(gh api "repos/rancher/rke2/actions/runs?event=pull_request&per_page=100" --jq ".workflow_runs[] | select(.pull_requests[]?.number == ${pr_number}) | .id" 2>/dev/null)
            candidate_run_ids="$candidate_run_ids $api_run_ids"
        fi
        
        # De-duplicate
        candidate_run_ids=$(echo "$candidate_run_ids" | tr ' ' '\n' | grep -v '^$' | sort -u | tr '\n' ' ')
        
        if [[ -z "$candidate_run_ids" ]]; then
            echo "Warning: No completed workflow runs found for ${runtime_lookup_desc}"
        else
            # Find a run that has an artifact containing rke2 runtime/images
            run_id=""
            artifact_name=""
            for candidate in $candidate_run_ids; do
                artifact_names=$(gh api "repos/rancher/rke2/actions/runs/${candidate}/artifacts" --paginate --jq '.artifacts[].name' 2>/dev/null)
                if [[ -z "$artifact_names" ]]; then
                    continue
                fi
                # Try to find a matching artifact: prefer runtime, then test-artifacts, then images
                match=$(echo "$artifact_names" | grep -E "rke2-runtime|rke2-test-artifacts|rke2-images" | head -1)
                if [[ -n "$match" ]]; then
                    run_id="$candidate"
                    artifact_name="$match"
                    echo "Found workflow run ID $run_id with artifact: $artifact_name"
                    break
                fi
            done
            
            if [[ -z "$run_id" ]]; then
                echo "Warning: None of the workflow runs for ${runtime_lookup_desc} contain a matching rke2 artifact"
                echo "Checked runs: $candidate_run_ids"
                echo ""
                echo "Available artifacts across runs:"
                for candidate in $candidate_run_ids; do
                    names=$(gh api "repos/rancher/rke2/actions/runs/${candidate}/artifacts" --paginate --jq '.artifacts[].name' 2>/dev/null)
                    if [[ -n "$names" ]]; then
                        echo "  Run $candidate:"
                        echo "$names" | sed 's/^/    /'
                    fi
                done
            else
                artifact_dir=$(mktemp -d)
                
                # Download the artifact
                echo "Downloading $artifact_name from workflow run..."
                download_output=$(gh run download "$run_id" -R rancher/rke2 -n "$artifact_name" -D "$artifact_dir" 2>&1)
                download_exit=$?
                if [[ $download_exit -eq 0 ]]; then
                    
                    # Prefer the rke2-runtime tarball; fall back to linux-amd64 images archive
                    runtime_tar=""
                    
                    # Look for rke2-runtime tarball (could be .tar or .tar.zst)
                    runtime_archive=$(find "$artifact_dir" -type f \( -name "rke2-runtime*.tar.zst" -o -name "rke2-runtime*.tar" \) | head -1)
                    
                    if [[ -z "$runtime_archive" ]]; then
                        # Fall back to linux-amd64 image archive
                        runtime_archive=$(find "$artifact_dir" -type f -name "rke2-images.linux-amd64.tar.zst" | head -1)
                    fi
                    
                    if [[ -n "$runtime_archive" ]]; then
                        echo "Found archive: $runtime_archive"
                        
                        # Decompress if zstd-compressed
                        if [[ "$runtime_archive" == *.zst ]]; then
                            runtime_tar="${runtime_archive%.zst}"
                            echo "Decompressing archive..."
                            if ! zstd -d "$runtime_archive" -o "$runtime_tar" 2>/dev/null; then
                                echo "Warning: Failed to decompress archive"
                                runtime_tar=""
                            fi
                        else
                            runtime_tar="$runtime_archive"
                        fi
                        
                        if [[ -n "$runtime_tar" ]]; then
                            # Save the tarball path for trivy to scan directly via --input
                            pr_runtime_tar="$runtime_tar"
                            # Don't delete the artifact_dir until after scan
                            keep_artifact_dir="$artifact_dir"
                            artifact_dir=""
                            echo "Will scan runtime tarball: $pr_runtime_tar"

                            # The runtime image reference generated by build-images
                            # (e.g. rancher/rke2-runtime:<dev-version>) is never
                            # pushed to a registry for an unreleased build, so a
                            # registry scan of it always comes back empty. Now that
                            # we have the real image tarball, drop that unpullable
                            # reference from the image lists so it isn't reported as
                            # an empty "scanned" image; the tarball scan covers it.
                            for img_list in images.txt images-optional.txt; do
                                [[ -f "$img_list" ]] || continue
                                if grep -v '/rke2-runtime:' "$img_list" > "${img_list}.tmp" 2>/dev/null; then
                                    mv "${img_list}.tmp" "$img_list"
                                else
                                    rm -f "${img_list}.tmp"
                                fi
                            done
                        fi
                    else
                        echo "Warning: No suitable runtime/image archive found in artifact"
                        echo "Artifact contents:"
                        find "$artifact_dir" -type f
                    fi
                else
                    echo "Warning: Failed to download artifact from workflow run (exit $download_exit): $download_output"
                fi
                
                # Cleanup temp directory if not retained for scanning
                if [[ -n "$artifact_dir" ]]; then
                    rm -rf "$artifact_dir"
                fi
            fi
        fi
fi

# Download the Rancher OpenVEX Trivy report
if curl -fsSL https://github.com/rancher/vexhub/raw/refs/heads/main/reports/rancher.openvex.json \
    -o rancher.openvex.json 2>/dev/null && [[ -s rancher.openvex.json ]]; then
    # Validate it's actually valid JSON/VEX by checking for opening brace
    if head -c 1 rancher.openvex.json | grep -q '{'; then
        vex_flag="--vex rancher.openvex.json"
    else
        echo "Warning: Downloaded OpenVEX file appears invalid; continuing without VEX suppression"
        rm -f rancher.openvex.json
        vex_flag=""
    fi
else
    echo "Warning: Failed to download Rancher OpenVEX report; continuing without VEX suppression"
    vex_flag=""
fi

# Write markdown header and the list of images being scanned to the output file
{
    echo "# Trivy Scan Report"
    echo ""
    echo "<!-- scan-source-ref: ${source_ref} -->"
    echo "<!-- scan-source-desc: ${source_desc} -->"
    echo "## Images Scanned"
    echo ""
    while IFS= read -r image; do
        printf -- '- `%s`\n' "$image"
    done < "$input_file"
    if [[ -n "$pr_runtime_tar" ]]; then
        echo ""
        echo "## Runtime Image Tarball"
        echo ""
        printf -- '- `%s`\n' "$pr_runtime_tar"
    fi
    echo ""
} >> "$output_file"

# Track per-image CVE counts for the default-images summary section
total_critical=0
total_high=0
images_with_cves=()
images_clean=()

# Track per-image CVE counts for the optional (non-default) add-on summary
optional_total_critical=0
optional_total_high=0
optional_images_with_cves=()
optional_images_clean=()

# Track bundle-level metrics for sqlite persistence (default images list only).
bundle_total_critical=0
bundle_total_high=0
bundle_images_with_cves=0
bundle_go_stdlib_cves=0
bundle_go_module_cves=0
bundle_base_image_cves=0
bundle_images_scanned=0

# tally_severities <display-name> <scan-output-file> [scope]
# Parses trivy "Total: N (HIGH: x, CRITICAL: y)" lines and updates summary state.
# scope defaults to "default"; pass "optional" to accumulate into the optional
# add-on summary counters instead.
tally_severities() {
    local display_name="$1"
    local scan_file="$2"
    local scope="${3:-default}"
    local img_critical=0 img_high=0 h c

    while IFS= read -r line; do
        h=$(echo "$line" | sed -nE 's/.*HIGH:[[:space:]]*([0-9]+).*/\1/p')
        c=$(echo "$line" | sed -nE 's/.*CRITICAL:[[:space:]]*([0-9]+).*/\1/p')
        [[ -n "$h" ]] && img_high=$((img_high + h))
        [[ -n "$c" ]] && img_critical=$((img_critical + c))
    done < <(grep -E '^Total: [0-9]+ \(' "$scan_file")

    if [[ "$scope" == "optional" ]]; then
        optional_total_high=$((optional_total_high + img_high))
        optional_total_critical=$((optional_total_critical + img_critical))

        if (( img_high + img_critical > 0 )); then
            optional_images_with_cves+=("${display_name}|${img_critical}|${img_high}")
        else
            optional_images_clean+=("$display_name")
        fi
        return
    fi

    total_high=$((total_high + img_high))
    total_critical=$((total_critical + img_critical))

    if (( img_high + img_critical > 0 )); then
        images_with_cves+=("${display_name}|${img_critical}|${img_high}")
    else
        images_clean+=("$display_name")
    fi
}

sqlite_escape() {
    printf '%s' "$1" | sed "s/'/''/g"
}

source_attribution_python_enabled=1
source_attribution_warning_emitted=0
if ! command -v python3 >/dev/null 2>&1; then
    source_attribution_python_enabled=0
    source_attribution_warning_emitted=1
    echo "Warning: python3 not found; skipping CVE source attribution"
fi

init_metrics_db() {
    local db_dir

    if ! command -v sqlite3 >/dev/null 2>&1; then
        echo "Warning: sqlite3 not found; skipping metrics database updates"
        return 1
    fi

    db_dir="$(dirname "$db_file")"
    mkdir -p "$db_dir"

    sqlite3 "$db_file" <<'SQL'
CREATE TABLE IF NOT EXISTS scan_metrics (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    scanned_at TEXT NOT NULL,
    source_desc TEXT NOT NULL,
    source_ref TEXT NOT NULL,
    total_images INTEGER NOT NULL,
    images_with_cves INTEGER NOT NULL,
    critical_cves INTEGER NOT NULL,
    high_cves INTEGER NOT NULL,
    go_stdlib_cves INTEGER NOT NULL,
    go_module_cves INTEGER NOT NULL,
    base_image_cves INTEGER NOT NULL,
    optional_total_images INTEGER NOT NULL DEFAULT 0,
    optional_images_with_cves INTEGER NOT NULL DEFAULT 0,
    optional_critical_cves INTEGER NOT NULL DEFAULT 0,
    optional_high_cves INTEGER NOT NULL DEFAULT 0,
    created_at TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ', 'now'))
);
CREATE INDEX IF NOT EXISTS idx_scan_metrics_scanned_at ON scan_metrics(scanned_at);
CREATE INDEX IF NOT EXISTS idx_scan_metrics_source_ref_scanned_at
    ON scan_metrics(source_ref, scanned_at);
CREATE UNIQUE INDEX IF NOT EXISTS uq_scan_metrics_run_signature
    ON scan_metrics(
        scanned_at,
        source_ref,
        total_images,
        images_with_cves,
        critical_cves,
        high_cves,
        go_stdlib_cves,
        go_module_cves,
        base_image_cves
    );

-- Per-CVE identities captured per scan run. Enables precise fix tracking:
-- a CVE present for a source in one scan but absent in the next was resolved
-- on the later scan's date. Linked to the aggregate row via scan_id.
CREATE TABLE IF NOT EXISTS scan_cves (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    scan_id INTEGER NOT NULL REFERENCES scan_metrics(id),
    scanned_at TEXT NOT NULL,
    source_ref TEXT NOT NULL,
    scope TEXT NOT NULL DEFAULT 'default',
    image TEXT NOT NULL,
    cve_id TEXT NOT NULL,
    severity TEXT NOT NULL,
    package TEXT NOT NULL DEFAULT '',
    installed_version TEXT NOT NULL DEFAULT '',
    fixed_version TEXT NOT NULL DEFAULT '',
    created_at TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ', 'now'))
);
CREATE INDEX IF NOT EXISTS idx_scan_cves_scan_id ON scan_cves(scan_id);
CREATE INDEX IF NOT EXISTS idx_scan_cves_cve_id ON scan_cves(cve_id);
CREATE INDEX IF NOT EXISTS idx_scan_cves_source_ref_scanned_at
    ON scan_cves(source_ref, scanned_at);
CREATE UNIQUE INDEX IF NOT EXISTS uq_scan_cves_identity
    ON scan_cves(scan_id, image, cve_id, package, installed_version);
SQL

    # Backfill optional-image columns on databases created before these metrics
    # existed. CREATE TABLE IF NOT EXISTS will not add columns to an existing
    # table, so add any that are missing (idempotent).
    local existing_cols col
    existing_cols="$(sqlite3 "$db_file" "SELECT name FROM pragma_table_info('scan_metrics');" 2>/dev/null)"
    for col in optional_total_images optional_images_with_cves optional_critical_cves optional_high_cves; do
        if ! grep -qx "$col" <<<"$existing_cols"; then
            sqlite3 "$db_file" "ALTER TABLE scan_metrics ADD COLUMN ${col} INTEGER NOT NULL DEFAULT 0;"
        fi
    done
}

classify_cve_sources() {
    local scan_json="$1"
    local result

    if (( source_attribution_python_enabled == 0 )); then
        echo "0|0|0"
        return
    fi

    if [[ ! -s "$scan_json" ]]; then
        if (( source_attribution_warning_emitted == 0 )); then
            echo "Warning: missing Trivy JSON results; CVE source attribution will default to zero counts" >&2
            source_attribution_warning_emitted=1
        fi
        echo "0|0|0"
        return
    fi

    if ! result="$(python3 - "$scan_json" <<'PY'
import json
import sys

try:
    with open(sys.argv[1], "r", encoding="utf-8") as f:
        data = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    print("0|0|0")
    sys.exit(0)

counts = {"go_stdlib": 0, "go_module": 0, "base_image": 0}
for result in data.get("Results", []):
    result_class = (result.get("Class") or "").lower()
    result_type = (result.get("Type") or "").lower()

    for vuln in result.get("Vulnerabilities") or []:
        if vuln.get("Severity") not in {"HIGH", "CRITICAL"}:
            continue

        pkg_name = (vuln.get("PkgName") or "").lower()

        if result_class == "os-pkgs":
            counts["base_image"] += 1
            continue

        if pkg_name in {"stdlib", "go"}:
            counts["go_stdlib"] += 1
            continue

        if result_type in {"gomod", "gobinary"}:
            counts["go_module"] += 1

print(
    f"{counts['go_stdlib']}|{counts['go_module']}|{counts['base_image']}"
)
PY
)"; then
        if (( source_attribution_warning_emitted == 0 )); then
            echo "Warning: failed to classify CVE sources from Trivy JSON; defaulting attribution to zero counts" >&2
            source_attribution_warning_emitted=1
        fi
        echo "0|0|0"
        return
    fi

    echo "$result"
}

# Accumulator file for per-CVE rows captured across every scan path. Populated by
# collect_cve_rows and flushed into the scan_cves table alongside scan_metrics.
cve_rows_file="$(mktemp)"

# collect_cve_rows <scan-json> <image> [scope]
# Appends one tab-separated row per CRITICAL/HIGH vulnerability found in the
# Trivy JSON to $cve_rows_file. Columns: scope, image, cve_id, severity,
# package, installed_version, fixed_version. Tabs/newlines inside values are
# stripped so each CVE stays on a single, parseable line. No-op when python3 is
# unavailable or the JSON is missing/empty (mirrors classify_cve_sources).
collect_cve_rows() {
    local scan_json="$1"
    local image="$2"
    local scope="${3:-default}"

    if (( source_attribution_python_enabled == 0 )); then
        return
    fi

    if [[ ! -s "$scan_json" ]]; then
        return
    fi

    python3 - "$scan_json" "$image" "$scope" >> "$cve_rows_file" <<'PY'
import json
import sys

scan_json, image, scope = sys.argv[1], sys.argv[2], sys.argv[3]

try:
    with open(scan_json, "r", encoding="utf-8") as f:
        data = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    sys.exit(0)


def clean(value):
    return str(value or "").replace("\t", " ").replace("\n", " ").replace("\r", " ")


seen = set()
for result in data.get("Results", []):
    for vuln in result.get("Vulnerabilities") or []:
        severity = vuln.get("Severity")
        if severity not in {"HIGH", "CRITICAL"}:
            continue

        cve_id = clean(vuln.get("VulnerabilityID"))
        if not cve_id:
            continue

        package = clean(vuln.get("PkgName"))
        installed = clean(vuln.get("InstalledVersion"))

        # Collapse duplicate findings (same CVE/package/version reported more
        # than once for an image) to match the table's unique-identity index.
        key = (cve_id, package, installed)
        if key in seen:
            continue
        seen.add(key)

        fixed = clean(vuln.get("FixedVersion"))
        print(
            "\t".join(
                [clean(scope), clean(image), cve_id, clean(severity), package, installed, fixed]
            )
        )
PY
}

# Loop through each image in the input file
while IFS= read -r image; do
    image="${image#"${image%%[![:space:]]*}"}"
    image="${image%"${image##*[![:space:]]}"}"
    if [[ -z "$image" || "$image" == \#* ]]; then
        continue
    fi

    echo "Scanning image: $image"
    bundle_images_scanned=$((bundle_images_scanned + 1))
    scan_tmp=$(mktemp)
    scan_json_tmp=$(mktemp)
    trivy image "$image" $vex_flag --severity CRITICAL,HIGH --format json > "$scan_json_tmp" 2>/dev/null
    trivy convert --format table "$scan_json_tmp" > "$scan_tmp" 2>/dev/null
    {
        echo "## Scan Results: \`$image\`"
        echo ""
        echo '```text'
        cat "$scan_tmp"
        echo '```'
        echo ""
    } >> "$output_file"
    tally_severities "$image" "$scan_tmp"
    source_breakdown=$(classify_cve_sources "$scan_json_tmp")
    collect_cve_rows "$scan_json_tmp" "$image" "default"
    IFS='|' read -r img_go_stdlib img_go_module img_base_image <<< "$source_breakdown"

    bundle_go_stdlib_cves=$((bundle_go_stdlib_cves + img_go_stdlib))
    bundle_go_module_cves=$((bundle_go_module_cves + img_go_module))
    bundle_base_image_cves=$((bundle_base_image_cves + img_base_image))
    img_critical=$(grep -E '^Total: [0-9]+ \(' "$scan_tmp" | sed -nE 's/.*CRITICAL:[[:space:]]*([0-9]+).*/\1/p' | awk '{s+=$1} END{print s+0}')
    img_high=$(grep -E '^Total: [0-9]+ \(' "$scan_tmp" | sed -nE 's/.*HIGH:[[:space:]]*([0-9]+).*/\1/p' | awk '{s+=$1} END{print s+0}')

    bundle_total_critical=$((bundle_total_critical + img_critical))
    bundle_total_high=$((bundle_total_high + img_high))
    if (( img_critical + img_high > 0 )); then
        bundle_images_with_cves=$((bundle_images_with_cves + 1))
    fi

    rm -f "$scan_tmp"
    rm -f "$scan_json_tmp"
done < "$input_file"

# Also scan the runtime image tarball directly if available
if [[ -n "$pr_runtime_tar" ]]; then
    echo "Scanning runtime tarball: $pr_runtime_tar"
    tarball_label="Runtime Image Tarball: $(basename "$pr_runtime_tar")"
    scan_tmp=$(mktemp)
    scan_json_tmp=$(mktemp)
    trivy image --input "$pr_runtime_tar" $vex_flag  --severity CRITICAL,HIGH --format json > "$scan_json_tmp" 2>/dev/null
    trivy convert --format table "$scan_json_tmp" > "$scan_tmp" 2>/dev/null
    {
        echo "## Scan Results: ${tarball_label}"
        echo ""
        echo '```text'
        cat "$scan_tmp"
        echo '```'
        echo ""
    } >> "$output_file"
    tally_severities "$tarball_label" "$scan_tmp"
    source_breakdown=$(classify_cve_sources "$scan_json_tmp")
    collect_cve_rows "$scan_json_tmp" "$tarball_label" "default"
    rm -f "$scan_tmp"
    rm -f "$scan_json_tmp"

    # Cleanup the artifact dir now that we're done
    if [[ -n "$keep_artifact_dir" ]]; then
        rm -rf "$keep_artifact_dir"
    fi
fi

# Scan optional (non-default) add-on images, if any, into a clearly delineated
# section. The HTML converter wraps everything between the OPTIONAL-START and
# OPTIONAL-END markers in a show/hide toggle (enabled by default).
optional_count=0
if [[ -s "$optional_input_file" ]]; then
    opt_results_md=$(mktemp)

    while IFS= read -r image; do
        image="${image#"${image%%[![:space:]]*}"}"
        image="${image%"${image##*[![:space:]]}"}"
        if [[ -z "$image" || "$image" == \#* ]]; then
            continue
        fi

        echo "Scanning optional add-on image: $image"
        optional_count=$((optional_count + 1))
        scan_tmp=$(mktemp)
        scan_json_tmp=$(mktemp)
        trivy image "$image" $vex_flag --severity CRITICAL,HIGH --format json > "$scan_json_tmp" 2>/dev/null
        trivy convert --format table "$scan_json_tmp" > "$scan_tmp" 2>/dev/null
        {
            echo "## Scan Results: \`$image\`"
            echo ""
            echo '```text'
            cat "$scan_tmp"
            echo '```'
            echo ""
        } >> "$opt_results_md"
        tally_severities "$image" "$scan_tmp" "optional"
        collect_cve_rows "$scan_json_tmp" "$image" "optional"
        rm -f "$scan_tmp"
        rm -f "$scan_json_tmp"
    done < "$optional_input_file"
fi

if (( optional_count > 0 )); then
    {
        echo "<!--OPTIONAL-START-->"
        echo ""
        echo "## Optional Add-on Images (Not in Default Tarball)"
        echo ""
        echo "> ⚠️ The images in this section are **not** part of the default RKE2 airgap tarball (\`images-core\` + \`images-canal\`). They ship with optional add-ons — Cilium, Calico, vSphere, Multus, and Harvester. Use the toggle above to show or hide them."
        echo ""

        echo "### Optional CVEs by Severity"
        echo ""
        echo "| Severity | Count |"
        echo "| --- | ---: |"
        echo "| CRITICAL | ${optional_total_critical} |"
        echo "| HIGH | ${optional_total_high} |"
        echo "| **Total** | **$((optional_total_critical + optional_total_high))** |"
        echo ""

        echo "### Optional Images with CVEs (${#optional_images_with_cves[@]})"
        echo ""
        if (( ${#optional_images_with_cves[@]} == 0 )); then
            echo "_None_"
        else
            echo "| Image | CRITICAL | HIGH |"
            echo "| --- | ---: | ---: |"
            for entry in "${optional_images_with_cves[@]}"; do
                name="${entry%%|*}"
                rest="${entry#*|}"
                crit="${rest%%|*}"
                high="${rest#*|}"
                printf '| `%s` | %d | %d |\n' "$name" "$crit" "$high"
            done
        fi
        echo ""

        echo "### Images Scanned (Optional)"
        echo ""
        while IFS= read -r image; do
            [[ -n "$image" ]] || continue
            printf -- '- `%s`\n' "$image"
        done < "$optional_input_file"
        echo ""
    } >> "$output_file"

    cat "$opt_results_md" >> "$output_file"

    {
        echo "<!--OPTIONAL-END-->"
        echo ""
    } >> "$output_file"
fi

if [[ -n "${opt_results_md:-}" ]]; then
    rm -f "$opt_results_md"
fi

# Append a markdown summary section to the end of the report
{
    echo "## Summary"
    echo ""
    echo "### CVEs by Severity"
    echo ""
    echo "| Severity | Count |"
    echo "| --- | ---: |"
    echo "| CRITICAL | ${total_critical} |"
    echo "| HIGH | ${total_high} |"
    echo "| **Total** | **$((total_critical + total_high))** |"
    echo ""

    echo "### Images with CVEs (${#images_with_cves[@]})"
    echo ""
    if (( ${#images_with_cves[@]} == 0 )); then
        echo "_None_"
    else
        echo "| Image | CRITICAL | HIGH |"
        echo "| --- | ---: | ---: |"
        for entry in "${images_with_cves[@]}"; do
            name="${entry%%|*}"
            rest="${entry#*|}"
            crit="${rest%%|*}"
            high="${rest#*|}"
            printf '| `%s` | %d | %d |\n' "$name" "$crit" "$high"
        done
    fi
    echo ""

    echo "### CVE-free Images (${#images_clean[@]})"
    echo ""
    if (( ${#images_clean[@]} == 0 )); then
        echo "_None_"
    else
        for name in "${images_clean[@]}"; do
            printf -- '- `%s`\n' "$name"
        done
    fi
    echo ""
} >> "$output_file"

echo "Trivy scan completed. Reports are saved in $output_file."

if init_metrics_db; then
    scanned_at="$(date -u '+%Y-%m-%dT%H:%M:%SZ')"
    source_desc_db="$(sqlite_escape "$source_desc")"
    source_ref_db="$(sqlite_escape "${source_ref}")"

    sqlite3 "$db_file" <<SQL
INSERT OR IGNORE INTO scan_metrics (
    scanned_at,
    source_desc,
    source_ref,
    total_images,
    images_with_cves,
    critical_cves,
    high_cves,
    go_stdlib_cves,
    go_module_cves,
    base_image_cves,
    optional_total_images,
    optional_images_with_cves,
    optional_critical_cves,
    optional_high_cves
) VALUES (
    '${scanned_at}',
    '${source_desc_db}',
    '${source_ref_db}',
    $(wc -l < "$input_file" | tr -d ' '),
    ${bundle_images_with_cves},
    ${total_critical},
    ${total_high},
    ${bundle_go_stdlib_cves},
    ${bundle_go_module_cves},
    ${bundle_base_image_cves},
    ${optional_count},
    ${#optional_images_with_cves[@]},
    ${optional_total_critical},
    ${optional_total_high}
);
SQL
    if [[ "$(sqlite3 "$db_file" 'SELECT changes();')" -gt 0 ]]; then
        echo "Scan metrics written to $db_file"
    else
        echo "Scan metrics already recorded for this run signature; skipped duplicate insert"
    fi

    # Persist the individual CVE identities captured during the scan, linked to
    # this run's scan_metrics row. Idempotent via uq_scan_cves_identity; a
    # duplicate run signature reuses the existing scan_id and inserts nothing
    # new. No-op when no rows were collected (e.g. python3 unavailable).
    if [[ -s "$cve_rows_file" ]]; then
        scan_id="$(sqlite3 "$db_file" \
            "SELECT id FROM scan_metrics WHERE scanned_at='${scanned_at}' AND source_ref='${source_ref_db}' ORDER BY id DESC LIMIT 1;")"
        if [[ -n "$scan_id" ]] && command -v python3 >/dev/null 2>&1; then
            if python3 - "$cve_rows_file" "$scan_id" "$scanned_at" "$source_ref" <<'PY' | sqlite3 "$db_file"
import sys

rows_file, scan_id, scanned_at, source_ref = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]


def q(value):
    return "'" + str(value).replace("'", "''") + "'"


with open(rows_file, "r", encoding="utf-8") as f:
    for line in f:
        line = line.rstrip("\n")
        if not line:
            continue
        fields = line.split("\t")
        if len(fields) != 7:
            continue
        scope, image, cve_id, severity, package, installed, fixed = fields
        print(
            "INSERT OR IGNORE INTO scan_cves "
            "(scan_id, scanned_at, source_ref, scope, image, cve_id, severity, "
            "package, installed_version, fixed_version) VALUES ("
            + ", ".join(
                [
                    str(int(scan_id)),
                    q(scanned_at),
                    q(source_ref),
                    q(scope),
                    q(image),
                    q(cve_id),
                    q(severity),
                    q(package),
                    q(installed),
                    q(fixed),
                ]
            )
            + ");"
        )
PY
            then
                cve_row_count="$(sqlite3 "$db_file" "SELECT count(*) FROM scan_cves WHERE scan_id=${scan_id};")"
                echo "Recorded ${cve_row_count} per-CVE rows for scan ${scan_id} in $db_file"
            else
                echo "Warning: failed to persist per-CVE rows to $db_file" >&2
            fi
        fi
    fi
fi

rm -f "$cve_rows_file"

if [[ -n "$gist_title" ]]; then
    echo "Uploading results to GitHub Gist..."
    gist_url=$(gh gist create --public --desc "$gist_title" --filename "$output_file" "$output_file" 2>&1)
    if [[ $? -eq 0 ]]; then
        echo "Gist created: $gist_url"

        # If both PR and gist are provided, add a comment to the PR with the gist link
        if [[ -n "$pr_number" ]]; then
            echo "Adding comment to PR #${pr_number} with gist link..."
            if gh pr comment "$pr_number" -R "rancher/rke2" --body "Trivy scan results: ${gist_url}"; then
                echo "Comment added to PR #${pr_number}"
            else
                echo "Warning: Failed to add comment to PR #${pr_number}"
            fi
        fi
    else
        echo "Error creating gist: $gist_url"
        exit 1
    fi
fi
