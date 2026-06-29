#!/bin/bash

set -euo pipefail

output_file="image_update_report.txt"
images_file="images.txt"
branch=""
pr_input=""
raw_repo="rancher/rke2"
gist_title=""
use_prime_ingress="false"
release_version=""

# Optional overrides for image names that do not follow the standard mapping rules.
# Add mappings in the case statement below as needed.
repo_override() {
    case "$1" in
        klipper-lb) echo "k3s-io/klipper-lb" ;;
        klipper-helm) echo "k3s-io/klipper-helm" ;;
        kube-webhook-certgen) echo "rancher/ingress-nginx" ;;
        nginx-ingress-controller) echo "rancher/ingress-nginx" ;;
        hardened-snapshot-controller) echo "image-build-external-snapshotter" ;;
        hardened-dns-node-cache) echo "image-build-dns-nodecache" ;;
        hardened-cluster-autoscaler) echo "image-build-cluster-proportional-autoscaler" ;;
        # hardened-etcd) echo "rancher/image-build-etcd" ;;
        *) echo "" ;;
    esac
}

# For image sources built from a specific branch line, constrain tag matching.
# In rancher/ingress-nginx this corresponds to v1.14.x hardened tags.
tag_regex_override() {
    case "$1" in
        kube-webhook-certgen|nginx-ingress-controller)
            if [[ "$use_prime_ingress" == "true" ]]; then
                echo '^v1\.14\..*-prime[0-9]+$'
            else
                echo '^v1\.14\..*-hardened[0-9]+$'
            fi
            ;;
        *) echo "" ;;
    esac
}

# Manual upstream repo overrides (owner/repo on GitHub) for images whose
# image-build repo does not point at the true upstream, or that need special
# handling. Return "none" to explicitly skip upstream resolution for an image.
upstream_repo_override() {
    case "$1" in
        kube-webhook-certgen|nginx-ingress-controller) echo "kubernetes/ingress-nginx" ;;
        # klipper images are k3s-io's own projects; the build repo is the source,
        # so there is no separate upstream to track.
        klipper-helm|klipper-lb) echo "none" ;;
        *) echo "" ;;
    esac
}

# Optional regex to constrain which upstream tags are considered. Useful for
# monorepos or repos that publish multiple component tag families.
upstream_tag_regex_override() {
    case "$1" in
        kube-webhook-certgen|nginx-ingress-controller) echo '^controller-v[0-9]' ;;
        # kubernetes/autoscaler is a monorepo; the hardened image tracks the
        # addon-resizer 1.8.x component line.
        hardened-addon-resizer|addon-resizer) echo '^addon-resizer-1\.8\.' ;;
        *) echo "" ;;
    esac
}

usage() {
    cat <<EOF
Usage: $0 [branch] [--pr <pr-number|pr-url>] [--release <branch>] [--output <file>] [--gist <title>] [--prime]

Examples:
  $0
  $0 release-1.32
  $0 --pr 9994
  $0 --pr https://github.com/rancher/rke2/pull/9994
  $0 --release release-1.35
  $0 --output my_report.txt
  $0 --prime
  $0 --gist 'My Update Report'
EOF
}

while [[ $# -gt 0 ]]; do
    case "$1" in
        -p|--pr)
            [[ -n "${2:-}" ]] || { echo "Error: --pr requires a value"; usage; exit 1; }
            pr_input="$2"
            shift 2
            ;;
        -r|--release)
            [[ -n "${2:-}" ]] || { echo "Error: --release requires a branch value"; usage; exit 1; }
            release_version="$2"
            shift 2
            ;;
        -o|--output)
            [[ -n "${2:-}" ]] || { echo "Error: --output requires a value"; usage; exit 1; }
            output_file="$2"
            shift 2
            ;;
        -g|--gist)
            [[ -n "${2:-}" ]] || { echo "Error: --gist requires a title value"; usage; exit 1; }
            gist_title="$2"
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

# --release names a release branch to build from (e.g. release-1.35). It is a
# convenience alias for the positional branch argument so the value can be wired
# in from the GitHub Action.
if [[ -n "$release_version" ]]; then
    branch="$release_version"
fi

if [[ -z "$branch" ]]; then
    branch="master"
fi

# Validate mutually exclusive flags
if [[ -n "$release_version" && -n "$pr_input" ]]; then
    echo "Error: --release and --pr cannot be used together"
    usage
    exit 1
fi

if [[ -n "$pr_input" ]]; then
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
else
    ref_path="refs/heads/${branch}"
    source_desc="branch '${branch}'"
fi

rm -f "$output_file" "$images_file"

echo "Building image list from ${source_desc} (${ref_path})" >&2

work_dir=$(mktemp -d)
cleanup() {
    rm -rf "$work_dir"
}
trap cleanup EXIT

mkdir -p "$work_dir/scripts" "$work_dir/bin" "$work_dir/build"
raw_ref="$ref_path"

download_build_scripts() {
    curl -fsSL "https://raw.githubusercontent.com/${raw_repo}/${raw_ref}/scripts/version.sh" \
        -o "$work_dir/scripts/version.sh" 2>/dev/null \
    && curl -fsSL "https://raw.githubusercontent.com/${raw_repo}/${raw_ref}/scripts/build-images" \
        -o "$work_dir/scripts/build-images" 2>/dev/null
}

if ! download_build_scripts; then
    if [[ -n "$pr_input" ]]; then
        echo "Unable to fetch scripts via ${raw_repo}/${raw_ref}; resolving PR head via GitHub API..." >&2
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
        echo "Retrying with ${source_desc}" >&2

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

exclude_pattern="multus|harvester|mirrored|rke2-runtime|hardened-kubernetes"

find "$work_dir/build" -maxdepth 1 -type f -name 'images-*.txt' ! -name 'images.txt' -print0 \
    | xargs -0 cat \
    | grep -vE "$exclude_pattern" \
    | sed '/^\s*$/d' \
    | sort -u \
    > "$images_file"

if [[ ! -s "$images_file" ]]; then
    echo "Error: no images were generated" >&2
    exit 1
fi

have_gh="false"
if command -v gh >/dev/null 2>&1; then
    have_gh="true"
fi

go_build_base_cache_file="$work_dir/go_build_base_cache.txt"
touch "$go_build_base_cache_file"

upstream_cache_file="$work_dir/upstream_cache.txt"
touch "$upstream_cache_file"

normalize_repo_slug() {
    local repo="$1"
    if [[ "$repo" == */* ]]; then
        printf '%s\n' "$repo"
    else
        printf 'rancher/%s\n' "$repo"
    fi
}

github_tags() {
    local repo="$1"
    local repo_slug

    repo_slug="$(normalize_repo_slug "$repo")"

    if [[ "$have_gh" == "true" ]]; then
        gh api --paginate "repos/${repo_slug}/tags?per_page=100" 2>/dev/null \
            | perl -ne 'while (/"name"\s*:\s*"([^"]+)"/g) { print "$1\n" }'
    else
        curl -fsSL "https://api.github.com/repos/${repo_slug}/tags?per_page=100" 2>/dev/null \
            | perl -ne 'while (/"name"\s*:\s*"([^"]+)"/g) { print "$1\n" }'
    fi
}

fetch_repo_file_at_ref() {
    local repo_slug="$1"
    local git_ref="$2"
    local file_path="$3"

    curl -fsSL "https://raw.githubusercontent.com/${repo_slug}/${git_ref}/${file_path}" 2>/dev/null || true
}

extract_go_build_base_version() {
    local file_content="$1"
    local base_tag
    local go_version

    base_tag=$(printf '%s\n' "$file_content" \
        | grep -Eom1 'hardened-build-base:[A-Za-z0-9._-]+' \
        | sed 's/^.*://')
    if [[ -n "$base_tag" ]]; then
        printf '%s\n' "$base_tag"
        return 0
    fi

    go_version=$(printf '%s\n' "$file_content" \
        | sed -nE 's/^[[:space:]]*(ARG[[:space:]]+)?GO_VERSION[[:space:]]*=?[[:space:]]*"?([^"[:space:]]+)"?.*/\2/p' \
        | head -n 1)
    if [[ -n "$go_version" ]]; then
        printf '%s\n' "$go_version"
        return 0
    fi

    printf 'N/A\n'
    return 1
}

fetch_ingress_nginx_go_version() {
    local git_ref="$1"
    local golang_version_content
    local branch

    branch="hardened-nginx-1.14.x"

    golang_version_content=$(fetch_repo_file_at_ref "rancher/ingress-nginx" "$branch" "GOLANG_VERSION")
    if [[ -n "$golang_version_content" ]]; then
        printf '%s\n' "$golang_version_content" | sed 's/^[[:space:]]*//;s/[[:space:]]*$//'
        return 0
    fi

    printf 'N/A\n'
    return 1
}

find_repo_go_build_base_version() {
    local repo="$1"
    local git_ref="$2"
    local repo_slug
    local cache_key
    local cached_line
    local file_content
    local version=""
    local candidate_path

    repo_slug="$(normalize_repo_slug "$repo")"
    cache_key="${repo_slug}|${git_ref}"

    cached_line=$(grep -F "${cache_key}|" "$go_build_base_cache_file" | head -n 1 || true)
    if [[ -n "$cached_line" ]]; then
        printf '%s\n' "${cached_line#${cache_key}|}"
        return 0
    fi

    if [[ "$repo_slug" == "rancher/ingress-nginx" ]]; then
        version=$(fetch_ingress_nginx_go_version "$git_ref" || true)
        if [[ -n "$version" && "$version" != "N/A" ]]; then
            printf '%s|%s\n' "$cache_key" "$version" >> "$go_build_base_cache_file"
            printf '%s\n' "$version"
            return 0
        fi
    fi

    for candidate_path in Dockerfile.dapper Dockerfile package/Dockerfile scripts/version.sh; do
        file_content=$(fetch_repo_file_at_ref "$repo_slug" "$git_ref" "$candidate_path")
        if [[ -n "$file_content" ]]; then
            version=$(extract_go_build_base_version "$file_content" || true)
            if [[ -n "$version" && "$version" != "N/A" ]]; then
                printf '%s|%s\n' "$cache_key" "$version" >> "$go_build_base_cache_file"
                printf '%s\n' "$version"
                return 0
            fi
        fi
    done

    printf '%s|N/A\n' "$cache_key" >> "$go_build_base_cache_file"
    printf 'N/A\n'
    return 1
}

# Parse an upstream "owner/repo" (on GitHub) out of an image-build repo's
# Dockerfile/Makefile content. Resolution order: SRC -> PKG -> git clone URL.
extract_upstream_repo() {
    local content="$1"
    local match=""
    local repo

    # 1. SRC=github.com/owner/repo (ARG SRC=, SRC ?=, quoted or not)
    match=$(printf '%s\n' "$content" \
        | grep -oE '(^|[^A-Za-z0-9_])SRC[[:space:]]*\??[:=][[:space:]]*"?github\.com/[A-Za-z0-9._/-]+' \
        | head -n 1 | grep -oE 'github\.com/[A-Za-z0-9._/-]+' | head -n 1 || true)

    # 2. PKG=github.com/owner/repo
    if [[ -z "$match" ]]; then
        match=$(printf '%s\n' "$content" \
            | grep -oE '(^|[^A-Za-z0-9_])PKG[[:space:]]*\??[:=][[:space:]]*"?github\.com/[A-Za-z0-9._/-]+' \
            | head -n 1 | grep -oE 'github\.com/[A-Za-z0-9._/-]+' | head -n 1 || true)
    fi

    # 3. git clone https://github.com/owner/repo[.git]
    if [[ -z "$match" ]]; then
        match=$(printf '%s\n' "$content" \
            | grep -ioE 'git[[:space:]]+clone[^#]*github\.com/[A-Za-z0-9._/-]+' \
            | head -n 1 | grep -oE 'github\.com/[A-Za-z0-9._/-]+' | head -n 1 || true)
    fi

    [[ -n "$match" ]] || return 1

    repo="${match#github.com/}"
    repo="${repo%.git}"
    # Reduce to the first two path segments (owner/repo), dropping any trailing
    # path like a Go semantic-import suffix (/v3) or /releases.
    repo=$(printf '%s\n' "$repo" | awk -F/ 'NF>=2 {print $1"/"$2}')
    [[ "$repo" == */* ]] || return 1
    printf '%s\n' "$repo"
}

# Fetch the Dockerfile and Makefile of a build repo, trying the latest build tag
# first, then the default branches. Output is the concatenated file contents.
fetch_build_repo_source_files() {
    local build_repo="$1"
    local build_latest_tag="$2"
    local repo_slug
    local ref
    local path
    local part
    local content=""

    repo_slug="$(normalize_repo_slug "$build_repo")"

    for ref in "$build_latest_tag" master main; do
        [[ -n "$ref" && "$ref" != "N/A" ]] || continue
        content=""
        for path in Dockerfile Makefile; do
            part="$(fetch_repo_file_at_ref "$repo_slug" "$ref" "$path")"
            if [[ -n "$part" ]]; then
                content+="$part"$'\n'
            fi
        done
        if [[ -n "$content" ]]; then
            printf '%s' "$content"
            return 0
        fi
    done

    return 1
}

# Determine the latest stable upstream tag for an image's upstream repo.
find_upstream_latest_tag() {
    local upstream_repo="$1"
    local image_name="$2"
    local tags
    local regex
    local filtered
    local latest

    tags=$(github_tags "$upstream_repo" || true)
    [[ -n "$tags" ]] || return 1

    regex="$(upstream_tag_regex_override "$image_name")"
    if [[ -n "$regex" ]]; then
        # Explicit override: only consider matching tags, no fallback.
        filtered=$(printf '%s\n' "$tags" | grep -E "$regex" || true)
    else
        # Default: stable semver tags, excluding pre-release markers.
        filtered=$(printf '%s\n' "$tags" \
            | grep -E '^v?[0-9]+\.[0-9]+\.[0-9]+' \
            | grep -viE 'rc|alpha|beta|dev|pre|snapshot|nightly' || true)
        [[ -n "$filtered" ]] || filtered="$tags"
    fi

    latest=$(printf '%s\n' "$filtered" | sed '/^\s*$/d' | sort -uV | tail -1)
    [[ -n "$latest" ]] || return 1
    printf '%s\n' "$latest"
}

# Resolve an image's upstream repo and its latest tag. Output: "repo|tag".
# Results are cached per image name to avoid repeated network calls.
find_image_upstream() {
    local image_name="$1"
    local build_repo="$2"
    local build_latest_tag="$3"
    local cached
    local upstream_repo
    local content
    local tag

    cached=$(grep -F "${image_name}|" "$upstream_cache_file" | head -n 1 || true)
    if [[ -n "$cached" ]]; then
        printf '%s\n' "${cached#${image_name}|}"
        return 0
    fi

    upstream_repo="$(upstream_repo_override "$image_name")"

    if [[ "$upstream_repo" == "none" ]]; then
        printf '%s|N/A|N/A\n' "$image_name" >> "$upstream_cache_file"
        printf 'N/A|N/A\n'
        return 0
    fi

    if [[ -z "$upstream_repo" && -n "$build_repo" && "$build_repo" != "N/A" ]]; then
        content="$(fetch_build_repo_source_files "$build_repo" "$build_latest_tag" || true)"
        if [[ -n "$content" ]]; then
            upstream_repo="$(extract_upstream_repo "$content" || true)"
        fi
    fi

    if [[ -z "$upstream_repo" ]]; then
        printf '%s|N/A|N/A\n' "$image_name" >> "$upstream_cache_file"
        printf 'N/A|N/A\n'
        return 0
    fi

    tag="$(find_upstream_latest_tag "$upstream_repo" "$image_name" || true)"
    [[ -n "$tag" ]] || tag="N/A"

    printf '%s|%s|%s\n' "$image_name" "$upstream_repo" "$tag" >> "$upstream_cache_file"
    printf '%s|%s\n' "$upstream_repo" "$tag"
    return 0
}

find_build_repo_and_latest_tag() {
    local image_name="$1"
    local repo_candidate
    local latest=""
    local override_repo
    local tag_regex
    local filtered_tags

    local candidates=()
    override_repo="$(repo_override "$image_name")"
    if [[ -n "$override_repo" ]]; then
        candidates+=("$override_repo")
    fi

    tag_regex="$(tag_regex_override "$image_name")"

    candidates+=("image-build-${image_name}")

    if [[ "$image_name" == hardened-* ]]; then
        candidates+=("image-build-${image_name#hardened-}")
    fi

    if [[ "$image_name" == mirrored-* ]]; then
        candidates+=("image-build-${image_name#mirrored-}")
    fi

    for repo_candidate in "${candidates[@]}"; do
        tags=$(github_tags "$repo_candidate" || true)
        if [[ -n "$tags" ]]; then
            filtered_tags="$tags"
            if [[ -n "$tag_regex" ]]; then
                filtered_tags=$(printf '%s\n' "$filtered_tags" | grep -E "$tag_regex" || true)
            fi

            latest=$(printf '%s\n' "$filtered_tags" | sed '/^\s*$/d' | sort -uV | tail -1)
            if [[ -n "$latest" ]]; then
                printf '%s|%s\n' "$repo_candidate" "$latest"
                return 0
            fi
        fi
    done

    printf '|' 
    return 1
}

extract_image_name_and_tag() {
    local image_ref="$1"
    local ref_no_digest="${image_ref%@*}"
    local image_path
    local image_name
    local current_tag

    # If the first segment contains '.' or ':' or is 'localhost', it is a registry host.
    local first_seg="${ref_no_digest%%/*}"
    if [[ "$ref_no_digest" == */* ]] && [[ "$first_seg" == *.* || "$first_seg" == *:* || "$first_seg" == "localhost" ]]; then
        image_path="${ref_no_digest#*/}"
    else
        image_path="$ref_no_digest"
    fi

    # Tag is only valid if ':' appears after the last '/'.
    local last_seg="${image_path##*/}"
    if [[ "$last_seg" == *:* ]]; then
        current_tag="${last_seg##*:}"
        image_name="${last_seg%%:*}"
    else
        current_tag="latest"
        image_name="$last_seg"
    fi

    printf '%s|%s\n' "$image_name" "$current_tag"
}

{
    echo "# Image update check report"
    echo ""
    echo "- Source: ${source_desc}"
    echo "- Generated: $(date -u '+%Y-%m-%dT%H:%M:%SZ')"
    echo ""
    echo "| Image | Current Tag | Build Repo | Latest Tag | Upstream Repo | Upstream Latest Tag | Go (hardened-build-base) | Status |"
    echo "|---|---|---|---|---|---|---|---|"
} >> "$output_file"

total=0
needs_update=0
up_to_date=0
unknown=0
needs_update_stdout=""

while IFS= read -r image; do
    [[ -n "$image" ]] || continue
    total=$((total + 1))

    echo "[$total] Processing $image" >&2

    parsed=$(extract_image_name_and_tag "$image")
    image_name="${parsed%%|*}"
    current_tag="${parsed##*|}"

    repo_latest=$(find_build_repo_and_latest_tag "$image_name" || true)
    build_repo="${repo_latest%%|*}"
    latest_tag="${repo_latest##*|}"
    go_build_base_version="N/A"

    upstream_info=$(find_image_upstream "$image_name" "${build_repo:-N/A}" "${latest_tag:-N/A}" || true)
    upstream_repo="${upstream_info%%|*}"
    upstream_latest_tag="${upstream_info##*|}"

    if [[ -z "$build_repo" || -z "$latest_tag" ]]; then
        status="UNKNOWN"
        unknown=$((unknown + 1))
    elif [[ "$current_tag" == "$latest_tag" ]]; then
        go_build_base_version=$(find_repo_go_build_base_version "$build_repo" "$latest_tag" || true)
        status="UP_TO_DATE"
        up_to_date=$((up_to_date + 1))
    else
        go_build_base_version=$(find_repo_go_build_base_version "$build_repo" "$latest_tag" || true)
        status="NEEDS_UPDATE"
        needs_update=$((needs_update + 1))
        needs_update_stdout+="$image"$'\n'
    fi

    printf '| %s | %s | %s | %s | %s | %s | %s | %s |\n' \
        "$image" "$current_tag" "${build_repo:-N/A}" "${latest_tag:-N/A}" \
        "${upstream_repo:-N/A}" "${upstream_latest_tag:-N/A}" \
        "${go_build_base_version:-N/A}" "$status" \
        >> "$output_file"
done < "$images_file"

{
    echo ""
    echo "## Summary"
    echo ""
    echo "- Total images: $total"
    echo "- Needs update: $needs_update"
    echo "- Up to date: $up_to_date"
    echo "- Unknown mapping/latest tag: $unknown"
} >> "$output_file"

echo "Report written to $output_file" >&2
echo "Image list written to $images_file" >&2

if [[ -n "$gist_title" ]]; then
    echo "Uploading results to GitHub Gist..." >&2
    if ! command -v gh >/dev/null 2>&1; then
        echo "Error: gh CLI is required for --gist" >&2
        exit 1
    fi

    gist_upload_path="$output_file"
    gist_temp_dir=""

    # Gist naming is based on uploaded file path; ensure .md for Markdown rendering.
    if [[ "$output_file" != *.md ]]; then
        gist_temp_dir=$(mktemp -d)
        gist_upload_path="$gist_temp_dir/image_update_report.md"
        cp "$output_file" "$gist_upload_path"
    fi

    gist_url=$(gh gist create --public --desc "$gist_title" "$gist_upload_path" 2>&1)

    if [[ -n "$gist_temp_dir" ]]; then
        rm -rf "$gist_temp_dir"
    fi

    if [[ $? -eq 0 ]]; then
        echo "Gist created: $gist_url" >&2
    else
        echo "Error creating gist: $gist_url" >&2
        exit 1
    fi
fi

# Stdout is intentionally reserved for just the images that need updating.
if [[ -n "$needs_update_stdout" ]]; then
    printf '%s' "$needs_update_stdout"
fi
