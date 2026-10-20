# Trivy Scan Report

<!-- scan-source-ref: refs/heads/release-1.36 -->
<!-- scan-source-desc: branch 'release-1.36' -->
<!-- suse-cvss-rescore: enabled -->
> Go binary CVE severities reflect SUSE's CVSS re-scoring where it differs from Trivy.

## Images Scanned

- `registry.rancher.com/rancher/hardened-calico:v3.32.2-build20261012`
- `registry.rancher.com/rancher/hardened-flannel:v0.28.10-build20261009`
- `registry.rancher.com/rancher/kube-webhook-certgen:v1.15.1-prime16`
- `registry.rancher.com/rancher/nginx-ingress-controller:v1.15.1-prime16`
- `registry.rancher.com/rancher/rke2-runtime:v1.36.5-dev.`
- `registry.rancher.com/rancher/hardened-kubernetes:v1.36.5-rke2r1-build20260923`
- `registry.rancher.com/rancher/hardened-coredns:v1.14.7-build20261016`
- `registry.rancher.com/rancher/hardened-cluster-autoscaler:v1.11.0-build20261016`
- `registry.rancher.com/rancher/hardened-dns-node-cache:1.27.2-r1-build20261016`
- `registry.rancher.com/rancher/hardened-etcd:v3.6.14-k3s3-build20260915`
- `registry.rancher.com/rancher/hardened-k8s-metrics-server:v0.9.0-build20261012`
- `registry.rancher.com/rancher/hardened-addon-resizer:1.8.23-build20261012`
- `registry.rancher.com/rancher/klipper-helm:v0.13.3-build20261014`
- `registry.rancher.com/rancher/klipper-lb:v0.4.17`
- `registry.rancher.com/rancher/rke2-cloud-provider:v1.36.6-0.20261016153003-c2fdd7c56c2c-build20261016`
- `registry.rancher.com/rancher/hardened-snapshot-controller:v8.7.0-build20261015`
- `registry.rancher.com/rancher/hardened-traefik:v3.7.15-build20261016`
- `registry.rancher.com/rancher/hardened-cni-plugins:v1.9.1-build20261012`

## Scan Results: `registry.rancher.com/rancher/hardened-calico:v3.32.2-build20261012`

```text
```

## Scan Results: `registry.rancher.com/rancher/hardened-flannel:v0.28.10-build20261009`

```text
```

## Scan Results: `registry.rancher.com/rancher/kube-webhook-certgen:v1.15.1-prime16`

```text
```

## Scan Results: `registry.rancher.com/rancher/nginx-ingress-controller:v1.15.1-prime16`

```text
```

## Scan Results: `registry.rancher.com/rancher/rke2-runtime:v1.36.5-dev.`

```text
```

## Scan Results: `registry.rancher.com/rancher/hardened-kubernetes:v1.36.5-rke2r1-build20260923`

```text

usr/local/bin/kube-apiserver (gobinary)
=======================================
Total: 10 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 10, CRITICAL: 0)

┌──────────────────┬────────────────┬──────────┬────────┬───────────────────┬────────────────┬──────────────────────────────────────────────────────────────┐
│     Library      │ Vulnerability  │ Severity │ Status │ Installed Version │ Fixed Version  │                            Title                             │
├──────────────────┼────────────────┼──────────┼────────┼───────────────────┼────────────────┼──────────────────────────────────────────────────────────────┤
│ golang.org/x/net │ CVE-2026-78659 │ HIGH     │ fixed  │ v0.56.0           │ 0.60.0         │ When "Trailer" headers are sent by a client, the HTTP server │
│                  │                │          │        │                   │                │ internall...                                                 │
│                  │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-78659                   │
│                  ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                  │ CVE-2026-78660 │          │        │                   │                │ Historically, we have been rather lax about malformed        │
│                  │                │          │        │                   │                │ framing-related ...                                          │
│                  │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-78660                   │
│                  ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                  │ CVE-2026-78669 │          │        │                   │                │ net/http: net/http/internal/http2: golang.org/x/net/http2:   │
│                  │                │          │        │                   │                │ net/http: Denial of Service via excessive HTTP/2 SETTINGS    │
│                  │                │          │        │                   │                │ frames...                                                    │
│                  │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-78669                   │
├──────────────────┼────────────────┤          │        ├───────────────────┼────────────────┼──────────────────────────────────────────────────────────────┤
│ stdlib           │ CVE-2026-56866 │          │        │ v1.26.8           │ 1.26.9, 1.27.2 │ net/http: golang: golang: Cross-user response poisoning via  │
│                  │                │          │        │                   │                │ desynchronized HTTP CONNECT connections                      │
│                  │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-56866                   │
│                  ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                  │ CVE-2026-78659 │          │        │                   │                │ When "Trailer" headers are sent by a client, the HTTP server │
│                  │                │          │        │                   │                │ internall...                                                 │
│                  │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-78659                   │
│                  ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                  │ CVE-2026-78660 │          │        │                   │                │ Historically, we have been rather lax about malformed        │
│                  │                │          │        │                   │                │ framing-related ...                                          │
│                  │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-78660                   │
│                  ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                  │ CVE-2026-78667 │          │        │                   │                │ net/http: golang: golang: Denial of Service via crafted HTTP │
│                  │                │          │        │                   │                │ Range headers                                                │
│                  │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-78667                   │
│                  ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                  │ CVE-2026-78669 │          │        │                   │                │ net/http: net/http/internal/http2: golang.org/x/net/http2:   │
│                  │                │          │        │                   │                │ net/http: Denial of Service via excessive HTTP/2 SETTINGS    │
│                  │                │          │        │                   │                │ frames...                                                    │
│                  │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-78669                   │
│                  ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                  │ CVE-2026-94440 │          │        │                   │                │ Parsing a multipart form can bypass memory limits and read   │
│                  │                │          │        │                   │                │ an arbitrar...                                               │
│                  │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-94440                   │
│                  ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                  │ CVE-2026-97031 │          │        │                   │                │ crypto/tls: golang: crypto/tls: Denial of Service via        │
│                  │                │          │        │                   │                │ multiple ECH outer extension references...                   │
│                  │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-97031                   │
└──────────────────┴────────────────┴──────────┴────────┴───────────────────┴────────────────┴──────────────────────────────────────────────────────────────┘

usr/local/bin/kube-controller-manager (gobinary)
================================================
Total: 10 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 10, CRITICAL: 0)

┌──────────────────┬────────────────┬──────────┬────────┬───────────────────┬────────────────┬──────────────────────────────────────────────────────────────┐
│     Library      │ Vulnerability  │ Severity │ Status │ Installed Version │ Fixed Version  │                            Title                             │
├──────────────────┼────────────────┼──────────┼────────┼───────────────────┼────────────────┼──────────────────────────────────────────────────────────────┤
│ golang.org/x/net │ CVE-2026-78659 │ HIGH     │ fixed  │ v0.56.0           │ 0.60.0         │ When "Trailer" headers are sent by a client, the HTTP server │
│                  │                │          │        │                   │                │ internall...                                                 │
│                  │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-78659                   │
│                  ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                  │ CVE-2026-78660 │          │        │                   │                │ Historically, we have been rather lax about malformed        │
│                  │                │          │        │                   │                │ framing-related ...                                          │
│                  │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-78660                   │
│                  ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                  │ CVE-2026-78669 │          │        │                   │                │ net/http: net/http/internal/http2: golang.org/x/net/http2:   │
│                  │                │          │        │                   │                │ net/http: Denial of Service via excessive HTTP/2 SETTINGS    │
│                  │                │          │        │                   │                │ frames...                                                    │
│                  │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-78669                   │
├──────────────────┼────────────────┤          │        ├───────────────────┼────────────────┼──────────────────────────────────────────────────────────────┤
│ stdlib           │ CVE-2026-56866 │          │        │ v1.26.8           │ 1.26.9, 1.27.2 │ net/http: golang: golang: Cross-user response poisoning via  │
│                  │                │          │        │                   │                │ desynchronized HTTP CONNECT connections                      │
│                  │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-56866                   │
│                  ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                  │ CVE-2026-78659 │          │        │                   │                │ When "Trailer" headers are sent by a client, the HTTP server │
│                  │                │          │        │                   │                │ internall...                                                 │
│                  │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-78659                   │
│                  ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                  │ CVE-2026-78660 │          │        │                   │                │ Historically, we have been rather lax about malformed        │
│                  │                │          │        │                   │                │ framing-related ...                                          │
│                  │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-78660                   │
│                  ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                  │ CVE-2026-78667 │          │        │                   │                │ net/http: golang: golang: Denial of Service via crafted HTTP │
│                  │                │          │        │                   │                │ Range headers                                                │
│                  │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-78667                   │
│                  ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                  │ CVE-2026-78669 │          │        │                   │                │ net/http: net/http/internal/http2: golang.org/x/net/http2:   │
│                  │                │          │        │                   │                │ net/http: Denial of Service via excessive HTTP/2 SETTINGS    │
│                  │                │          │        │                   │                │ frames...                                                    │
│                  │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-78669                   │
│                  ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                  │ CVE-2026-94440 │          │        │                   │                │ Parsing a multipart form can bypass memory limits and read   │
│                  │                │          │        │                   │                │ an arbitrar...                                               │
│                  │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-94440                   │
│                  ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                  │ CVE-2026-97031 │          │        │                   │                │ crypto/tls: golang: crypto/tls: Denial of Service via        │
│                  │                │          │        │                   │                │ multiple ECH outer extension references...                   │
│                  │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-97031                   │
└──────────────────┴────────────────┴──────────┴────────┴───────────────────┴────────────────┴──────────────────────────────────────────────────────────────┘

usr/local/bin/kube-proxy (gobinary)
===================================
Total: 10 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 10, CRITICAL: 0)

┌──────────────────┬────────────────┬──────────┬────────┬───────────────────┬────────────────┬──────────────────────────────────────────────────────────────┐
│     Library      │ Vulnerability  │ Severity │ Status │ Installed Version │ Fixed Version  │                            Title                             │
├──────────────────┼────────────────┼──────────┼────────┼───────────────────┼────────────────┼──────────────────────────────────────────────────────────────┤
│ golang.org/x/net │ CVE-2026-78659 │ HIGH     │ fixed  │ v0.56.0           │ 0.60.0         │ When "Trailer" headers are sent by a client, the HTTP server │
│                  │                │          │        │                   │                │ internall...                                                 │
│                  │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-78659                   │
│                  ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                  │ CVE-2026-78660 │          │        │                   │                │ Historically, we have been rather lax about malformed        │
│                  │                │          │        │                   │                │ framing-related ...                                          │
│                  │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-78660                   │
│                  ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                  │ CVE-2026-78669 │          │        │                   │                │ net/http: net/http/internal/http2: golang.org/x/net/http2:   │
│                  │                │          │        │                   │                │ net/http: Denial of Service via excessive HTTP/2 SETTINGS    │
│                  │                │          │        │                   │                │ frames...                                                    │
│                  │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-78669                   │
├──────────────────┼────────────────┤          │        ├───────────────────┼────────────────┼──────────────────────────────────────────────────────────────┤
│ stdlib           │ CVE-2026-56866 │          │        │ v1.26.8           │ 1.26.9, 1.27.2 │ net/http: golang: golang: Cross-user response poisoning via  │
│                  │                │          │        │                   │                │ desynchronized HTTP CONNECT connections                      │
│                  │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-56866                   │
│                  ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                  │ CVE-2026-78659 │          │        │                   │                │ When "Trailer" headers are sent by a client, the HTTP server │
│                  │                │          │        │                   │                │ internall...                                                 │
│                  │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-78659                   │
│                  ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                  │ CVE-2026-78660 │          │        │                   │                │ Historically, we have been rather lax about malformed        │
│                  │                │          │        │                   │                │ framing-related ...                                          │
│                  │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-78660                   │
│                  ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                  │ CVE-2026-78667 │          │        │                   │                │ net/http: golang: golang: Denial of Service via crafted HTTP │
│                  │                │          │        │                   │                │ Range headers                                                │
│                  │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-78667                   │
│                  ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                  │ CVE-2026-78669 │          │        │                   │                │ net/http: net/http/internal/http2: golang.org/x/net/http2:   │
│                  │                │          │        │                   │                │ net/http: Denial of Service via excessive HTTP/2 SETTINGS    │
│                  │                │          │        │                   │                │ frames...                                                    │
│                  │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-78669                   │
│                  ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                  │ CVE-2026-94440 │          │        │                   │                │ Parsing a multipart form can bypass memory limits and read   │
│                  │                │          │        │                   │                │ an arbitrar...                                               │
│                  │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-94440                   │
│                  ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                  │ CVE-2026-97031 │          │        │                   │                │ crypto/tls: golang: crypto/tls: Denial of Service via        │
│                  │                │          │        │                   │                │ multiple ECH outer extension references...                   │
│                  │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-97031                   │
└──────────────────┴────────────────┴──────────┴────────┴───────────────────┴────────────────┴──────────────────────────────────────────────────────────────┘

usr/local/bin/kube-scheduler (gobinary)
=======================================
Total: 10 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 10, CRITICAL: 0)

┌──────────────────┬────────────────┬──────────┬────────┬───────────────────┬────────────────┬──────────────────────────────────────────────────────────────┐
│     Library      │ Vulnerability  │ Severity │ Status │ Installed Version │ Fixed Version  │                            Title                             │
├──────────────────┼────────────────┼──────────┼────────┼───────────────────┼────────────────┼──────────────────────────────────────────────────────────────┤
│ golang.org/x/net │ CVE-2026-78659 │ HIGH     │ fixed  │ v0.56.0           │ 0.60.0         │ When "Trailer" headers are sent by a client, the HTTP server │
│                  │                │          │        │                   │                │ internall...                                                 │
│                  │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-78659                   │
│                  ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                  │ CVE-2026-78660 │          │        │                   │                │ Historically, we have been rather lax about malformed        │
│                  │                │          │        │                   │                │ framing-related ...                                          │
│                  │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-78660                   │
│                  ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                  │ CVE-2026-78669 │          │        │                   │                │ net/http: net/http/internal/http2: golang.org/x/net/http2:   │
│                  │                │          │        │                   │                │ net/http: Denial of Service via excessive HTTP/2 SETTINGS    │
│                  │                │          │        │                   │                │ frames...                                                    │
│                  │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-78669                   │
├──────────────────┼────────────────┤          │        ├───────────────────┼────────────────┼──────────────────────────────────────────────────────────────┤
│ stdlib           │ CVE-2026-56866 │          │        │ v1.26.8           │ 1.26.9, 1.27.2 │ net/http: golang: golang: Cross-user response poisoning via  │
│                  │                │          │        │                   │                │ desynchronized HTTP CONNECT connections                      │
│                  │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-56866                   │
│                  ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                  │ CVE-2026-78659 │          │        │                   │                │ When "Trailer" headers are sent by a client, the HTTP server │
│                  │                │          │        │                   │                │ internall...                                                 │
│                  │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-78659                   │
│                  ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                  │ CVE-2026-78660 │          │        │                   │                │ Historically, we have been rather lax about malformed        │
│                  │                │          │        │                   │                │ framing-related ...                                          │
│                  │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-78660                   │
│                  ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                  │ CVE-2026-78667 │          │        │                   │                │ net/http: golang: golang: Denial of Service via crafted HTTP │
│                  │                │          │        │                   │                │ Range headers                                                │
│                  │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-78667                   │
│                  ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                  │ CVE-2026-78669 │          │        │                   │                │ net/http: net/http/internal/http2: golang.org/x/net/http2:   │
│                  │                │          │        │                   │                │ net/http: Denial of Service via excessive HTTP/2 SETTINGS    │
│                  │                │          │        │                   │                │ frames...                                                    │
│                  │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-78669                   │
│                  ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                  │ CVE-2026-94440 │          │        │                   │                │ Parsing a multipart form can bypass memory limits and read   │
│                  │                │          │        │                   │                │ an arbitrar...                                               │
│                  │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-94440                   │
│                  ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                  │ CVE-2026-97031 │          │        │                   │                │ crypto/tls: golang: crypto/tls: Denial of Service via        │
│                  │                │          │        │                   │                │ multiple ECH outer extension references...                   │
│                  │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-97031                   │
└──────────────────┴────────────────┴──────────┴────────┴───────────────────┴────────────────┴──────────────────────────────────────────────────────────────┘

usr/local/bin/kubectl (gobinary)
================================
Total: 10 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 10, CRITICAL: 0)

┌──────────────────┬────────────────┬──────────┬────────┬───────────────────┬────────────────┬──────────────────────────────────────────────────────────────┐
│     Library      │ Vulnerability  │ Severity │ Status │ Installed Version │ Fixed Version  │                            Title                             │
├──────────────────┼────────────────┼──────────┼────────┼───────────────────┼────────────────┼──────────────────────────────────────────────────────────────┤
│ golang.org/x/net │ CVE-2026-78659 │ HIGH     │ fixed  │ v0.56.0           │ 0.60.0         │ When "Trailer" headers are sent by a client, the HTTP server │
│                  │                │          │        │                   │                │ internall...                                                 │
│                  │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-78659                   │
│                  ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                  │ CVE-2026-78660 │          │        │                   │                │ Historically, we have been rather lax about malformed        │
│                  │                │          │        │                   │                │ framing-related ...                                          │
│                  │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-78660                   │
│                  ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                  │ CVE-2026-78669 │          │        │                   │                │ net/http: net/http/internal/http2: golang.org/x/net/http2:   │
│                  │                │          │        │                   │                │ net/http: Denial of Service via excessive HTTP/2 SETTINGS    │
│                  │                │          │        │                   │                │ frames...                                                    │
│                  │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-78669                   │
├──────────────────┼────────────────┤          │        ├───────────────────┼────────────────┼──────────────────────────────────────────────────────────────┤
│ stdlib           │ CVE-2026-56866 │          │        │ v1.26.8           │ 1.26.9, 1.27.2 │ net/http: golang: golang: Cross-user response poisoning via  │
│                  │                │          │        │                   │                │ desynchronized HTTP CONNECT connections                      │
│                  │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-56866                   │
│                  ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                  │ CVE-2026-78659 │          │        │                   │                │ When "Trailer" headers are sent by a client, the HTTP server │
│                  │                │          │        │                   │                │ internall...                                                 │
│                  │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-78659                   │
│                  ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                  │ CVE-2026-78660 │          │        │                   │                │ Historically, we have been rather lax about malformed        │
│                  │                │          │        │                   │                │ framing-related ...                                          │
│                  │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-78660                   │
│                  ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                  │ CVE-2026-78667 │          │        │                   │                │ net/http: golang: golang: Denial of Service via crafted HTTP │
│                  │                │          │        │                   │                │ Range headers                                                │
│                  │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-78667                   │
│                  ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                  │ CVE-2026-78669 │          │        │                   │                │ net/http: net/http/internal/http2: golang.org/x/net/http2:   │
│                  │                │          │        │                   │                │ net/http: Denial of Service via excessive HTTP/2 SETTINGS    │
│                  │                │          │        │                   │                │ frames...                                                    │
│                  │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-78669                   │
│                  ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                  │ CVE-2026-94440 │          │        │                   │                │ Parsing a multipart form can bypass memory limits and read   │
│                  │                │          │        │                   │                │ an arbitrar...                                               │
│                  │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-94440                   │
│                  ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                  │ CVE-2026-97031 │          │        │                   │                │ crypto/tls: golang: crypto/tls: Denial of Service via        │
│                  │                │          │        │                   │                │ multiple ECH outer extension references...                   │
│                  │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-97031                   │
└──────────────────┴────────────────┴──────────┴────────┴───────────────────┴────────────────┴──────────────────────────────────────────────────────────────┘

usr/local/bin/kubelet (gobinary)
================================
Total: 10 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 10, CRITICAL: 0)

┌──────────────────┬────────────────┬──────────┬────────┬───────────────────┬────────────────┬──────────────────────────────────────────────────────────────┐
│     Library      │ Vulnerability  │ Severity │ Status │ Installed Version │ Fixed Version  │                            Title                             │
├──────────────────┼────────────────┼──────────┼────────┼───────────────────┼────────────────┼──────────────────────────────────────────────────────────────┤
│ golang.org/x/net │ CVE-2026-78659 │ HIGH     │ fixed  │ v0.56.0           │ 0.60.0         │ When "Trailer" headers are sent by a client, the HTTP server │
│                  │                │          │        │                   │                │ internall...                                                 │
│                  │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-78659                   │
│                  ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                  │ CVE-2026-78660 │          │        │                   │                │ Historically, we have been rather lax about malformed        │
│                  │                │          │        │                   │                │ framing-related ...                                          │
│                  │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-78660                   │
│                  ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                  │ CVE-2026-78669 │          │        │                   │                │ net/http: net/http/internal/http2: golang.org/x/net/http2:   │
│                  │                │          │        │                   │                │ net/http: Denial of Service via excessive HTTP/2 SETTINGS    │
│                  │                │          │        │                   │                │ frames...                                                    │
│                  │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-78669                   │
├──────────────────┼────────────────┤          │        ├───────────────────┼────────────────┼──────────────────────────────────────────────────────────────┤
│ stdlib           │ CVE-2026-56866 │          │        │ v1.26.8           │ 1.26.9, 1.27.2 │ net/http: golang: golang: Cross-user response poisoning via  │
│                  │                │          │        │                   │                │ desynchronized HTTP CONNECT connections                      │
│                  │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-56866                   │
│                  ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                  │ CVE-2026-78659 │          │        │                   │                │ When "Trailer" headers are sent by a client, the HTTP server │
│                  │                │          │        │                   │                │ internall...                                                 │
│                  │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-78659                   │
│                  ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                  │ CVE-2026-78660 │          │        │                   │                │ Historically, we have been rather lax about malformed        │
│                  │                │          │        │                   │                │ framing-related ...                                          │
│                  │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-78660                   │
│                  ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                  │ CVE-2026-78667 │          │        │                   │                │ net/http: golang: golang: Denial of Service via crafted HTTP │
│                  │                │          │        │                   │                │ Range headers                                                │
│                  │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-78667                   │
│                  ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                  │ CVE-2026-78669 │          │        │                   │                │ net/http: net/http/internal/http2: golang.org/x/net/http2:   │
│                  │                │          │        │                   │                │ net/http: Denial of Service via excessive HTTP/2 SETTINGS    │
│                  │                │          │        │                   │                │ frames...                                                    │
│                  │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-78669                   │
│                  ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                  │ CVE-2026-94440 │          │        │                   │                │ Parsing a multipart form can bypass memory limits and read   │
│                  │                │          │        │                   │                │ an arbitrar...                                               │
│                  │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-94440                   │
│                  ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                  │ CVE-2026-97031 │          │        │                   │                │ crypto/tls: golang: crypto/tls: Denial of Service via        │
│                  │                │          │        │                   │                │ multiple ECH outer extension references...                   │
│                  │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-97031                   │
└──────────────────┴────────────────┴──────────┴────────┴───────────────────┴────────────────┴──────────────────────────────────────────────────────────────┘
```

## Scan Results: `registry.rancher.com/rancher/hardened-coredns:v1.14.7-build20261016`

```text
```

## Scan Results: `registry.rancher.com/rancher/hardened-cluster-autoscaler:v1.11.0-build20261016`

```text
```

## Scan Results: `registry.rancher.com/rancher/hardened-dns-node-cache:1.27.2-r1-build20261016`

```text
```

## Scan Results: `registry.rancher.com/rancher/hardened-etcd:v3.6.14-k3s3-build20260915`

```text

usr/local/bin/etcd (gobinary)
=============================
Total: 9 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 9, CRITICAL: 0)

┌──────────────────┬────────────────┬──────────┬────────┬───────────────────┬────────────────┬──────────────────────────────────────────────────────────────┐
│     Library      │ Vulnerability  │ Severity │ Status │ Installed Version │ Fixed Version  │                            Title                             │
├──────────────────┼────────────────┼──────────┼────────┼───────────────────┼────────────────┼──────────────────────────────────────────────────────────────┤
│ golang.org/x/net │ CVE-2026-78659 │ HIGH     │ fixed  │ v0.58.0           │ 0.60.0         │ When "Trailer" headers are sent by a client, the HTTP server │
│                  │                │          │        │                   │                │ internall...                                                 │
│                  │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-78659                   │
│                  ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                  │ CVE-2026-78660 │          │        │                   │                │ Historically, we have been rather lax about malformed        │
│                  │                │          │        │                   │                │ framing-related ...                                          │
│                  │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-78660                   │
│                  ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                  │ CVE-2026-78669 │          │        │                   │                │ net/http: net/http/internal/http2: golang.org/x/net/http2:   │
│                  │                │          │        │                   │                │ net/http: Denial of Service via excessive HTTP/2 SETTINGS    │
│                  │                │          │        │                   │                │ frames...                                                    │
│                  │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-78669                   │
├──────────────────┼────────────────┤          │        ├───────────────────┼────────────────┼──────────────────────────────────────────────────────────────┤
│ stdlib           │ CVE-2026-56866 │          │        │ v1.26.8           │ 1.26.9, 1.27.2 │ net/http: golang: golang: Cross-user response poisoning via  │
│                  │                │          │        │                   │                │ desynchronized HTTP CONNECT connections                      │
│                  │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-56866                   │
│                  ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                  │ CVE-2026-78659 │          │        │                   │                │ When "Trailer" headers are sent by a client, the HTTP server │
│                  │                │          │        │                   │                │ internall...                                                 │
│                  │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-78659                   │
│                  ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                  │ CVE-2026-78660 │          │        │                   │                │ Historically, we have been rather lax about malformed        │
│                  │                │          │        │                   │                │ framing-related ...                                          │
│                  │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-78660                   │
│                  ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                  │ CVE-2026-78669 │          │        │                   │                │ net/http: net/http/internal/http2: golang.org/x/net/http2:   │
│                  │                │          │        │                   │                │ net/http: Denial of Service via excessive HTTP/2 SETTINGS    │
│                  │                │          │        │                   │                │ frames...                                                    │
│                  │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-78669                   │
│                  ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                  │ CVE-2026-94440 │          │        │                   │                │ Parsing a multipart form can bypass memory limits and read   │
│                  │                │          │        │                   │                │ an arbitrar...                                               │
│                  │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-94440                   │
│                  ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                  │ CVE-2026-97031 │          │        │                   │                │ crypto/tls: golang: crypto/tls: Denial of Service via        │
│                  │                │          │        │                   │                │ multiple ECH outer extension references...                   │
│                  │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-97031                   │
└──────────────────┴────────────────┴──────────┴────────┴───────────────────┴────────────────┴──────────────────────────────────────────────────────────────┘

usr/local/bin/etcdctl (gobinary)
================================
Total: 9 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 9, CRITICAL: 0)

┌──────────────────┬────────────────┬──────────┬────────┬───────────────────┬────────────────┬──────────────────────────────────────────────────────────────┐
│     Library      │ Vulnerability  │ Severity │ Status │ Installed Version │ Fixed Version  │                            Title                             │
├──────────────────┼────────────────┼──────────┼────────┼───────────────────┼────────────────┼──────────────────────────────────────────────────────────────┤
│ golang.org/x/net │ CVE-2026-78659 │ HIGH     │ fixed  │ v0.58.0           │ 0.60.0         │ When "Trailer" headers are sent by a client, the HTTP server │
│                  │                │          │        │                   │                │ internall...                                                 │
│                  │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-78659                   │
│                  ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                  │ CVE-2026-78660 │          │        │                   │                │ Historically, we have been rather lax about malformed        │
│                  │                │          │        │                   │                │ framing-related ...                                          │
│                  │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-78660                   │
│                  ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                  │ CVE-2026-78669 │          │        │                   │                │ net/http: net/http/internal/http2: golang.org/x/net/http2:   │
│                  │                │          │        │                   │                │ net/http: Denial of Service via excessive HTTP/2 SETTINGS    │
│                  │                │          │        │                   │                │ frames...                                                    │
│                  │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-78669                   │
├──────────────────┼────────────────┤          │        ├───────────────────┼────────────────┼──────────────────────────────────────────────────────────────┤
│ stdlib           │ CVE-2026-56866 │          │        │ v1.26.8           │ 1.26.9, 1.27.2 │ net/http: golang: golang: Cross-user response poisoning via  │
│                  │                │          │        │                   │                │ desynchronized HTTP CONNECT connections                      │
│                  │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-56866                   │
│                  ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                  │ CVE-2026-78659 │          │        │                   │                │ When "Trailer" headers are sent by a client, the HTTP server │
│                  │                │          │        │                   │                │ internall...                                                 │
│                  │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-78659                   │
│                  ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                  │ CVE-2026-78660 │          │        │                   │                │ Historically, we have been rather lax about malformed        │
│                  │                │          │        │                   │                │ framing-related ...                                          │
│                  │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-78660                   │
│                  ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                  │ CVE-2026-78669 │          │        │                   │                │ net/http: net/http/internal/http2: golang.org/x/net/http2:   │
│                  │                │          │        │                   │                │ net/http: Denial of Service via excessive HTTP/2 SETTINGS    │
│                  │                │          │        │                   │                │ frames...                                                    │
│                  │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-78669                   │
│                  ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                  │ CVE-2026-94440 │          │        │                   │                │ Parsing a multipart form can bypass memory limits and read   │
│                  │                │          │        │                   │                │ an arbitrar...                                               │
│                  │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-94440                   │
│                  ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                  │ CVE-2026-97031 │          │        │                   │                │ crypto/tls: golang: crypto/tls: Denial of Service via        │
│                  │                │          │        │                   │                │ multiple ECH outer extension references...                   │
│                  │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-97031                   │
└──────────────────┴────────────────┴──────────┴────────┴───────────────────┴────────────────┴──────────────────────────────────────────────────────────────┘
```

## Scan Results: `registry.rancher.com/rancher/hardened-k8s-metrics-server:v0.9.0-build20261012`

```text
```

## Scan Results: `registry.rancher.com/rancher/hardened-addon-resizer:1.8.23-build20261012`

```text
```

## Scan Results: `registry.rancher.com/rancher/klipper-helm:v0.13.3-build20261014`

```text

home/klipper-helm/.local/share/helm/plugins/helm-mapkubeapis/bin/mapkubeapis (gobinary)
=======================================================================================
Total: 1 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 1, CRITICAL: 0)

┌───────────────────┬────────────────┬──────────┬────────┬───────────────────┬───────────────┬─────────────────────────────────────────────────────────────┐
│      Library      │ Vulnerability  │ Severity │ Status │ Installed Version │ Fixed Version │                            Title                            │
├───────────────────┼────────────────┼──────────┼────────┼───────────────────┼───────────────┼─────────────────────────────────────────────────────────────┤
│ golang.org/x/text │ CVE-2026-56851 │ HIGH     │ fixed  │ v0.39.0           │ 0.41.0        │ golang.org/x/text: golang.org/x/text: Denial of Service via │
│                   │                │          │        │                   │               │ out-of-bounds slice error in Nickname profile...            │
│                   │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-56851                  │
└───────────────────┴────────────────┴──────────┴────────┴───────────────────┴───────────────┴─────────────────────────────────────────────────────────────┘

home/klipper-helm/.local/share/helm/plugins/helm-set-status/helm-set-status (gobinary)
======================================================================================
Total: 1 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 1, CRITICAL: 0)

┌───────────────────┬────────────────┬──────────┬────────┬───────────────────┬───────────────┬─────────────────────────────────────────────────────────────┐
│      Library      │ Vulnerability  │ Severity │ Status │ Installed Version │ Fixed Version │                            Title                            │
├───────────────────┼────────────────┼──────────┼────────┼───────────────────┼───────────────┼─────────────────────────────────────────────────────────────┤
│ golang.org/x/text │ CVE-2026-56851 │ HIGH     │ fixed  │ v0.39.0           │ 0.41.0        │ golang.org/x/text: golang.org/x/text: Denial of Service via │
│                   │                │          │        │                   │               │ out-of-bounds slice error in Nickname profile...            │
│                   │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-56851                  │
└───────────────────┴────────────────┴──────────┴────────┴───────────────────┴───────────────┴─────────────────────────────────────────────────────────────┘

usr/bin/helm (gobinary)
=======================
Total: 1 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 1, CRITICAL: 0)

┌───────────────────┬────────────────┬──────────┬────────┬───────────────────┬───────────────┬─────────────────────────────────────────────────────────────┐
│      Library      │ Vulnerability  │ Severity │ Status │ Installed Version │ Fixed Version │                            Title                            │
├───────────────────┼────────────────┼──────────┼────────┼───────────────────┼───────────────┼─────────────────────────────────────────────────────────────┤
│ golang.org/x/text │ CVE-2026-56851 │ HIGH     │ fixed  │ v0.39.0           │ 0.41.0        │ golang.org/x/text: golang.org/x/text: Denial of Service via │
│                   │                │          │        │                   │               │ out-of-bounds slice error in Nickname profile...            │
│                   │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-56851                  │
└───────────────────┴────────────────┴──────────┴────────┴───────────────────┴───────────────┴─────────────────────────────────────────────────────────────┘
```

## Scan Results: `registry.rancher.com/rancher/klipper-lb:v0.4.17`

```text
```

## Scan Results: `registry.rancher.com/rancher/rke2-cloud-provider:v1.36.6-0.20261016153003-c2fdd7c56c2c-build20261016`

```text
```

## Scan Results: `registry.rancher.com/rancher/hardened-snapshot-controller:v8.7.0-build20261015`

```text

snapshot-controller (gobinary)
==============================
Total: 1 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 1, CRITICAL: 0)

┌───────────────────┬────────────────┬──────────┬────────┬───────────────────┬───────────────┬─────────────────────────────────────────────────────────────┐
│      Library      │ Vulnerability  │ Severity │ Status │ Installed Version │ Fixed Version │                            Title                            │
├───────────────────┼────────────────┼──────────┼────────┼───────────────────┼───────────────┼─────────────────────────────────────────────────────────────┤
│ golang.org/x/text │ CVE-2026-56851 │ HIGH     │ fixed  │ v0.39.0           │ 0.41.0        │ golang.org/x/text: golang.org/x/text: Denial of Service via │
│                   │                │          │        │                   │               │ out-of-bounds slice error in Nickname profile...            │
│                   │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-56851                  │
└───────────────────┴────────────────┴──────────┴────────┴───────────────────┴───────────────┴─────────────────────────────────────────────────────────────┘
```

## Scan Results: `registry.rancher.com/rancher/hardened-traefik:v3.7.15-build20261016`

```text
```

## Scan Results: `registry.rancher.com/rancher/hardened-cni-plugins:v1.9.1-build20261012`

```text
```

<!--OPTIONAL-START-->

## Optional Add-on Images (Not in Default Tarball)

> ⚠️ The images in this section are **not** part of the default RKE2 airgap tarball (`images-core` + `images-canal`). They ship with optional add-ons — Cilium, Calico, vSphere, Multus, and Harvester. Use the toggle above to show or hide them.

### Optional CVEs by Severity

| Severity | Count |
| --- | ---: |
| CRITICAL | 6 |
| HIGH | 351 |
| **Total** | **357** |

### Optional Images with CVEs (34)

| Image | CRITICAL | HIGH |
| --- | ---: | ---: |
| `registry.rancher.com/rancher/mirrored-cilium-certgen:v0.4.11` | 0 | 12 |
| `registry.rancher.com/rancher/mirrored-cilium-cilium:v1.20.3` | 0 | 7 |
| `registry.rancher.com/rancher/mirrored-cilium-cilium-envoy:v1.38.6-1791537840-00e749f11f69334c625e53fc1ce2fc6c7f34a51f` | 0 | 24 |
| `registry.rancher.com/rancher/mirrored-cilium-clustermesh-apiserver:v1.20.3` | 0 | 11 |
| `registry.rancher.com/rancher/mirrored-cilium-hubble-ui:v0.13.6` | 0 | 1 |
| `registry.rancher.com/rancher/mirrored-cilium-hubble-ui-backend:v0.13.6` | 0 | 10 |
| `registry.rancher.com/rancher/mirrored-calico-operator:v1.42.6` | 0 | 12 |
| `registry.rancher.com/rancher/mirrored-calico-ctl:v3.32.2` | 1 | 14 |
| `registry.rancher.com/rancher/mirrored-calico-kube-controllers:v3.32.2` | 0 | 8 |
| `registry.rancher.com/rancher/mirrored-calico-typha:v3.32.2` | 0 | 5 |
| `registry.rancher.com/rancher/mirrored-calico-node:v3.32.2` | 1 | 18 |
| `registry.rancher.com/rancher/mirrored-calico-pod2daemon-flexvol:v3.32.2` | 0 | 7 |
| `registry.rancher.com/rancher/mirrored-calico-cni:v3.32.2` | 0 | 8 |
| `registry.rancher.com/rancher/mirrored-calico-apiserver:v3.32.2` | 0 | 5 |
| `registry.rancher.com/rancher/mirrored-calico-csi:v3.32.2` | 1 | 12 |
| `registry.rancher.com/rancher/mirrored-calico-node-driver-registrar:v3.32.2` | 1 | 13 |
| `registry.rancher.com/rancher/mirrored-calico-envoy-gateway:v3.32.2` | 1 | 16 |
| `registry.rancher.com/rancher/mirrored-calico-envoy-ratelimit:v3.32.2` | 1 | 13 |
| `registry.rancher.com/rancher/mirrored-calico-goldmane:v3.32.2` | 0 | 10 |
| `registry.rancher.com/rancher/mirrored-calico-whisker-backend:v3.32.2` | 0 | 5 |
| `registry.rancher.com/rancher/hardened-cloud-provider-vsphere:v1.36.0-build20261012` | 0 | 1 |
| `registry.rancher.com/rancher/hardened-vsphere-csi-driver:v3.7.3-build20261012` | 0 | 1 |
| `registry.rancher.com/rancher/hardened-vsphere-csi-syncer:v3.7.3-build20261012` | 0 | 1 |
| `registry.rancher.com/rancher/hardened-csi-resizer:v1.12.0-build20261012` | 0 | 1 |
| `registry.rancher.com/rancher/hardened-csi-attacher:v4.9.0-build20261012` | 0 | 1 |
| `registry.rancher.com/rancher/hardened-csi-provisioner:v4.0.1-build20261012` | 0 | 1 |
| `registry.rancher.com/rancher/hardened-csi-snapshotter:v8.6.0-build20261012` | 0 | 1 |
| `registry.rancher.com/rancher/mirrored-kube-vip-kube-vip-iptables:v1.2.4` | 0 | 11 |
| `registry.rancher.com/rancher/harvester-csi-driver:v0.2.10` | 0 | 24 |
| `registry.rancher.com/rancher/mirrored-longhornio-csi-node-driver-registrar:v2.16.0-20260428` | 0 | 18 |
| `registry.rancher.com/rancher/mirrored-longhornio-csi-resizer:v2.1.0-20260428` | 0 | 20 |
| `registry.rancher.com/rancher/mirrored-longhornio-csi-provisioner:v5.3.0-20260428` | 0 | 20 |
| `registry.rancher.com/rancher/mirrored-longhornio-csi-attacher:v4.11.0-20260428` | 0 | 20 |
| `registry.rancher.com/rancher/mirrored-longhornio-csi-snapshotter:v8.5.0-20260428` | 0 | 20 |

### Images Scanned (Optional)

- `registry.rancher.com/rancher/mirrored-cilium-certgen:v0.4.11`
- `registry.rancher.com/rancher/mirrored-cilium-cilium:v1.20.3`
- `registry.rancher.com/rancher/mirrored-cilium-cilium-envoy:v1.38.6-1791537840-00e749f11f69334c625e53fc1ce2fc6c7f34a51f`
- `registry.rancher.com/rancher/mirrored-cilium-clustermesh-apiserver:v1.20.3`
- `registry.rancher.com/rancher/mirrored-cilium-hubble-relay:v1.20.3`
- `registry.rancher.com/rancher/mirrored-cilium-hubble-ui:v0.13.6`
- `registry.rancher.com/rancher/mirrored-cilium-hubble-ui-backend:v0.13.6`
- `registry.rancher.com/rancher/mirrored-cilium-operator-aws:v1.20.3`
- `registry.rancher.com/rancher/mirrored-cilium-operator-azure:v1.20.3`
- `registry.rancher.com/rancher/mirrored-cilium-operator-generic:v1.20.3`
- `registry.rancher.com/rancher/hardened-cni-plugins:v1.9.1-build20261013`
- `registry.rancher.com/rancher/mirrored-calico-operator:v1.42.6`
- `registry.rancher.com/rancher/mirrored-calico-ctl:v3.32.2`
- `registry.rancher.com/rancher/mirrored-calico-kube-controllers:v3.32.2`
- `registry.rancher.com/rancher/mirrored-calico-typha:v3.32.2`
- `registry.rancher.com/rancher/mirrored-calico-node:v3.32.2`
- `registry.rancher.com/rancher/mirrored-calico-pod2daemon-flexvol:v3.32.2`
- `registry.rancher.com/rancher/mirrored-calico-cni:v3.32.2`
- `registry.rancher.com/rancher/mirrored-calico-apiserver:v3.32.2`
- `registry.rancher.com/rancher/mirrored-calico-csi:v3.32.2`
- `registry.rancher.com/rancher/mirrored-calico-node-driver-registrar:v3.32.2`
- `registry.rancher.com/rancher/mirrored-calico-envoy-gateway:v3.32.2`
- `registry.rancher.com/rancher/mirrored-calico-envoy-proxy:v3.32.2`
- `registry.rancher.com/rancher/mirrored-calico-envoy-ratelimit:v3.32.2`
- `registry.rancher.com/rancher/mirrored-calico-goldmane:v3.32.2`
- `registry.rancher.com/rancher/mirrored-calico-whisker:v3.32.2`
- `registry.rancher.com/rancher/mirrored-calico-whisker-backend:v3.32.2`
- `registry.rancher.com/rancher/hardened-cloud-provider-vsphere:v1.36.0-build20261012`
- `registry.rancher.com/rancher/hardened-vsphere-csi-driver:v3.7.3-build20261012`
- `registry.rancher.com/rancher/hardened-vsphere-csi-syncer:v3.7.3-build20261012`
- `registry.rancher.com/rancher/hardened-csi-node-driver-registrar:v2.13.0-build20261012`
- `registry.rancher.com/rancher/hardened-csi-resizer:v1.12.0-build20261012`
- `registry.rancher.com/rancher/hardened-livenessprobe:v2.15.0-build20261012`
- `registry.rancher.com/rancher/hardened-csi-attacher:v4.9.0-build20261012`
- `registry.rancher.com/rancher/hardened-csi-provisioner:v4.0.1-build20261012`
- `registry.rancher.com/rancher/hardened-csi-snapshotter:v8.6.0-build20261012`
- `registry.rancher.com/rancher/hardened-multus-cni:v4.3.1-build20261016`
- `registry.rancher.com/rancher/hardened-multus-thick:v4.3.1-build20261016`
- `registry.rancher.com/rancher/hardened-multus-dynamic-networks-controller:v0.3.8-build20261012`
- `registry.rancher.com/rancher/hardened-cni-plugins:v1.9.1-build20261015`
- `registry.rancher.com/rancher/hardened-whereabouts:v0.9.4-build20261016`
- `registry.rancher.com/rancher/mirrored-library-busybox:1.36.1`
- `registry.rancher.com/rancher/harvester-cloud-provider:v0.2.9`
- `registry.rancher.com/rancher/mirrored-kube-vip-kube-vip-iptables:v1.2.4`
- `registry.rancher.com/rancher/harvester-csi-driver:v0.2.10`
- `registry.rancher.com/rancher/mirrored-longhornio-csi-node-driver-registrar:v2.16.0-20260428`
- `registry.rancher.com/rancher/mirrored-longhornio-csi-resizer:v2.1.0-20260428`
- `registry.rancher.com/rancher/mirrored-longhornio-csi-provisioner:v5.3.0-20260428`
- `registry.rancher.com/rancher/mirrored-longhornio-csi-attacher:v4.11.0-20260428`
- `registry.rancher.com/rancher/mirrored-longhornio-csi-snapshotter:v8.5.0-20260428`

## Scan Results: `registry.rancher.com/rancher/mirrored-cilium-certgen:v0.4.11`

```text

usr/bin/cilium-certgen (gobinary)
=================================
Total: 12 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 12, CRITICAL: 0)

┌─────────────────────┬────────────────┬──────────┬────────┬───────────────────┬────────────────┬──────────────────────────────────────────────────────────────┐
│       Library       │ Vulnerability  │ Severity │ Status │ Installed Version │ Fixed Version  │                            Title                             │
├─────────────────────┼────────────────┼──────────┼────────┼───────────────────┼────────────────┼──────────────────────────────────────────────────────────────┤
│ golang.org/x/crypto │ CVE-2026-56855 │ HIGH     │ fixed  │ v0.55.0           │ 0.56.0         │ golang.org/x/crypto/ssh: golang.org/x/crypto/ssh: Denial of  │
│                     │                │          │        │                   │                │ Service via crafted messages                                 │
│                     │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-56855                   │
│                     ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                     │ CVE-2026-78662 │          │        │                   │                │ golang.org/x/crypto/ssh: golang.org/x/crypto/ssh: Denial of  │
│                     │                │          │        │                   │                │ Service via channel request flooding                         │
│                     │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-78662                   │
├─────────────────────┼────────────────┤          │        ├───────────────────┼────────────────┼──────────────────────────────────────────────────────────────┤
│ golang.org/x/net    │ CVE-2026-78659 │          │        │ v0.58.0           │ 0.60.0         │ When "Trailer" headers are sent by a client, the HTTP server │
│                     │                │          │        │                   │                │ internall...                                                 │
│                     │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-78659                   │
│                     ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                     │ CVE-2026-78660 │          │        │                   │                │ Historically, we have been rather lax about malformed        │
│                     │                │          │        │                   │                │ framing-related ...                                          │
│                     │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-78660                   │
│                     ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                     │ CVE-2026-78669 │          │        │                   │                │ net/http: net/http/internal/http2: golang.org/x/net/http2:   │
│                     │                │          │        │                   │                │ net/http: Denial of Service via excessive HTTP/2 SETTINGS    │
│                     │                │          │        │                   │                │ frames...                                                    │
│                     │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-78669                   │
├─────────────────────┼────────────────┤          │        ├───────────────────┼────────────────┼──────────────────────────────────────────────────────────────┤
│ stdlib              │ CVE-2026-56866 │          │        │ v1.26.6           │ 1.26.9, 1.27.2 │ net/http: golang: golang: Cross-user response poisoning via  │
│                     │                │          │        │                   │                │ desynchronized HTTP CONNECT connections                      │
│                     │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-56866                   │
│                     ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                     │ CVE-2026-78659 │          │        │                   │                │ When "Trailer" headers are sent by a client, the HTTP server │
│                     │                │          │        │                   │                │ internall...                                                 │
│                     │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-78659                   │
│                     ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                     │ CVE-2026-78660 │          │        │                   │                │ Historically, we have been rather lax about malformed        │
│                     │                │          │        │                   │                │ framing-related ...                                          │
│                     │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-78660                   │
│                     ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                     │ CVE-2026-78667 │          │        │                   │                │ net/http: golang: golang: Denial of Service via crafted HTTP │
│                     │                │          │        │                   │                │ Range headers                                                │
│                     │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-78667                   │
│                     ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                     │ CVE-2026-78669 │          │        │                   │                │ net/http: net/http/internal/http2: golang.org/x/net/http2:   │
│                     │                │          │        │                   │                │ net/http: Denial of Service via excessive HTTP/2 SETTINGS    │
│                     │                │          │        │                   │                │ frames...                                                    │
│                     │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-78669                   │
│                     ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                     │ CVE-2026-94440 │          │        │                   │                │ Parsing a multipart form can bypass memory limits and read   │
│                     │                │          │        │                   │                │ an arbitrar...                                               │
│                     │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-94440                   │
│                     ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                     │ CVE-2026-97031 │          │        │                   │                │ crypto/tls: golang: crypto/tls: Denial of Service via        │
│                     │                │          │        │                   │                │ multiple ECH outer extension references...                   │
│                     │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-97031                   │
└─────────────────────┴────────────────┴──────────┴────────┴───────────────────┴────────────────┴──────────────────────────────────────────────────────────────┘
```

## Scan Results: `registry.rancher.com/rancher/mirrored-cilium-cilium:v1.20.3`

```text

usr/bin/pebble (gobinary)
=========================
Total: 7 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 7, CRITICAL: 0)

┌─────────┬────────────────┬──────────┬────────┬───────────────────┬────────────────┬──────────────────────────────────────────────────────────────┐
│ Library │ Vulnerability  │ Severity │ Status │ Installed Version │ Fixed Version  │                            Title                             │
├─────────┼────────────────┼──────────┼────────┼───────────────────┼────────────────┼──────────────────────────────────────────────────────────────┤
│ stdlib  │ CVE-2026-56866 │ HIGH     │ fixed  │ v1.26.7           │ 1.26.9, 1.27.2 │ net/http: golang: golang: Cross-user response poisoning via  │
│         │                │          │        │                   │                │ desynchronized HTTP CONNECT connections                      │
│         │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-56866                   │
│         ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│         │ CVE-2026-78659 │          │        │                   │                │ When "Trailer" headers are sent by a client, the HTTP server │
│         │                │          │        │                   │                │ internall...                                                 │
│         │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-78659                   │
│         ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│         │ CVE-2026-78660 │          │        │                   │                │ Historically, we have been rather lax about malformed        │
│         │                │          │        │                   │                │ framing-related ...                                          │
│         │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-78660                   │
│         ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│         │ CVE-2026-78667 │          │        │                   │                │ net/http: golang: golang: Denial of Service via crafted HTTP │
│         │                │          │        │                   │                │ Range headers                                                │
│         │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-78667                   │
│         ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│         │ CVE-2026-78669 │          │        │                   │                │ net/http: net/http/internal/http2: golang.org/x/net/http2:   │
│         │                │          │        │                   │                │ net/http: Denial of Service via excessive HTTP/2 SETTINGS    │
│         │                │          │        │                   │                │ frames...                                                    │
│         │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-78669                   │
│         ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│         │ CVE-2026-94440 │          │        │                   │                │ Parsing a multipart form can bypass memory limits and read   │
│         │                │          │        │                   │                │ an arbitrar...                                               │
│         │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-94440                   │
│         ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│         │ CVE-2026-97031 │          │        │                   │                │ crypto/tls: golang: crypto/tls: Denial of Service via        │
│         │                │          │        │                   │                │ multiple ECH outer extension references...                   │
│         │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-97031                   │
└─────────┴────────────────┴──────────┴────────┴───────────────────┴────────────────┴──────────────────────────────────────────────────────────────┘
```

## Scan Results: `registry.rancher.com/rancher/mirrored-cilium-cilium-envoy:v1.38.6-1791537840-00e749f11f69334c625e53fc1ce2fc6c7f34a51f`

```text

usr/bin/cilium-envoy-healthcheck (gobinary)
===========================================
Total: 24 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 24, CRITICAL: 0)

┌─────────┬────────────────┬──────────┬────────┬───────────────────┬──────────────────────────────┬──────────────────────────────────────────────────────────────┐
│ Library │ Vulnerability  │ Severity │ Status │ Installed Version │        Fixed Version         │                            Title                             │
├─────────┼────────────────┼──────────┼────────┼───────────────────┼──────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ stdlib  │ CVE-2025-47912 │ HIGH     │ fixed  │ v1.24.6           │ 1.24.8, 1.25.2               │ net/url: Insufficient validation of bracketed IPv6 hostnames │
│         │                │          │        │                   │                              │ in net/url                                                   │
│         │                │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2025-47912                   │
│         ├────────────────┤          │        │                   │                              ├──────────────────────────────────────────────────────────────┤
│         │ CVE-2025-58188 │          │        │                   │                              │ crypto/x509: golang: Panic when validating certificates with │
│         │                │          │        │                   │                              │ DSA public keys in crypto/x509...                            │
│         │                │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2025-58188                   │
│         ├────────────────┤          │        │                   ├──────────────────────────────┼──────────────────────────────────────────────────────────────┤
│         │ CVE-2025-61727 │          │        │                   │ 1.24.11, 1.25.5              │ golang: crypto/x509: excluded subdomain constraint does not  │
│         │                │          │        │                   │                              │ restrict wildcard SANs                                       │
│         │                │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2025-61727                   │
│         ├────────────────┤          │        │                   │                              ├──────────────────────────────────────────────────────────────┤
│         │ CVE-2025-61729 │          │        │                   │                              │ crypto/x509: golang: Denial of Service due to excessive      │
│         │                │          │        │                   │                              │ resource consumption via crafted...                          │
│         │                │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2025-61729                   │
│         ├────────────────┤          │        │                   ├──────────────────────────────┼──────────────────────────────────────────────────────────────┤
│         │ CVE-2025-68121 │          │        │                   │ 1.24.13, 1.25.7, 1.26.0-rc.3 │ crypto/tls: crypto/tls: Incorrect certificate validation     │
│         │                │          │        │                   │                              │ during TLS session resumption                                │
│         │                │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2025-68121                   │
│         ├────────────────┤          │        │                   ├──────────────────────────────┼──────────────────────────────────────────────────────────────┤
│         │ CVE-2026-32280 │          │        │                   │ 1.25.9, 1.26.2               │ crypto/x509: crypto/tls: golang: Go: Denial of Service       │
│         │                │          │        │                   │                              │ vulnerability in certificate chain building...               │
│         │                │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-32280                   │
│         ├────────────────┤          │        │                   ├──────────────────────────────┼──────────────────────────────────────────────────────────────┤
│         │ CVE-2026-33811 │          │        │                   │ 1.25.10, 1.26.3              │ net: golang: Go net package: Denial of Service via long      │
│         │                │          │        │                   │                              │ CNAME response...                                            │
│         │                │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-33811                   │
│         ├────────────────┤          │        │                   │                              ├──────────────────────────────────────────────────────────────┤
│         │ CVE-2026-33814 │          │        │                   │                              │ net/http/internal/http2: golang: golang.org/x/net: Go        │
│         │                │          │        │                   │                              │ HTTP/2: Denial of Service via malformed                      │
│         │                │          │        │                   │                              │ SETTINGS_MAX_FRAME_SIZE frame...                             │
│         │                │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-33814                   │
│         ├────────────────┤          │        │                   ├──────────────────────────────┼──────────────────────────────────────────────────────────────┤
│         │ CVE-2026-33818 │          │        │                   │ 1.25.13, 1.26.6, 1.27.0-rc.3 │ encoding/asn1: golang: Go encoding/asn1: Denial of Service   │
│         │                │          │        │                   │                              │ via excessive recursion in Unmarshal...                      │
│         │                │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-33818                   │
│         ├────────────────┤          │        │                   ├──────────────────────────────┼──────────────────────────────────────────────────────────────┤
│         │ CVE-2026-39820 │          │        │                   │ 1.25.10, 1.26.3              │ net/mail: golang: Go net/mail: Denial of Service via crafted │
│         │                │          │        │                   │                              │ email inputs                                                 │
│         │                │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-39820                   │
│         ├────────────────┤          │        │                   ├──────────────────────────────┼──────────────────────────────────────────────────────────────┤
│         │ CVE-2026-39821 │          │        │                   │ 1.25.13, 1.26.6, 1.27.0-rc.3 │ golang.org/x/net/idna: golang: net/http:                     │
│         │                │          │        │                   │                              │ golang.org/x/net/idna: Privilege escalation via incorrect    │
│         │                │          │        │                   │                              │ Punycode label processing                                    │
│         │                │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-39821                   │
│         ├────────────────┤          │        │                   ├──────────────────────────────┼──────────────────────────────────────────────────────────────┤
│         │ CVE-2026-39822 │          │        │                   │ 1.25.12, 1.26.5, 1.27.0-rc.2 │ golang: Go os.Root: Symlink following vulnerability allows   │
│         │                │          │        │                   │                              │ directory traversal                                          │
│         │                │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-39822                   │
│         ├────────────────┤          │        │                   ├──────────────────────────────┼──────────────────────────────────────────────────────────────┤
│         │ CVE-2026-39836 │          │        │                   │ 1.25.10, 1.26.3              │ net: golang: Go net package: Denial of Service via NUL byte  │
│         │                │          │        │                   │                              │ in...                                                        │
│         │                │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-39836                   │
│         ├────────────────┤          │        │                   │                              ├──────────────────────────────────────────────────────────────┤
│         │ CVE-2026-42499 │          │        │                   │                              │ net/mail: golang: net/mail: Denial of Service via            │
│         │                │          │        │                   │                              │ pathological email address parsing                           │
│         │                │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-42499                   │
│         ├────────────────┤          │        │                   ├──────────────────────────────┼──────────────────────────────────────────────────────────────┤
│         │ CVE-2026-56853 │          │        │                   │ 1.25.13, 1.26.6, 1.27.0-rc.3 │ net/http: golang: Go net/http: Unencrypted HTTP/2            │
│         │                │          │        │                   │                              │ connections vulnerable to Denial of Service...               │
│         │                │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-56853                   │
│         ├────────────────┤          │        │                   │                              ├──────────────────────────────────────────────────────────────┤
│         │ CVE-2026-56859 │          │        │                   │                              │ encoding/xml: golang: Go: Denial of Service via XML decoding │
│         │                │          │        │                   │                              │ recursion depth issue...                                     │
│         │                │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-56859                   │
│         ├────────────────┤          │        │                   │                              ├──────────────────────────────────────────────────────────────┤
│         │ CVE-2026-56862 │          │        │                   │                              │ crypto/tls: golang: Golang crypto/tls: Denial of Service via │
│         │                │          │        │                   │                              │ indefinite KeyUpdate messages                                │
│         │                │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-56862                   │
│         ├────────────────┤          │        │                   ├──────────────────────────────┼──────────────────────────────────────────────────────────────┤
│         │ CVE-2026-56866 │          │        │                   │ 1.26.9, 1.27.2               │ net/http: golang: golang: Cross-user response poisoning via  │
│         │                │          │        │                   │                              │ desynchronized HTTP CONNECT connections                      │
│         │                │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-56866                   │
│         ├────────────────┤          │        │                   │                              ├──────────────────────────────────────────────────────────────┤
│         │ CVE-2026-78659 │          │        │                   │                              │ When "Trailer" headers are sent by a client, the HTTP server │
│         │                │          │        │                   │                              │ internall...                                                 │
│         │                │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-78659                   │
│         ├────────────────┤          │        │                   │                              ├──────────────────────────────────────────────────────────────┤
│         │ CVE-2026-78660 │          │        │                   │                              │ Historically, we have been rather lax about malformed        │
│         │                │          │        │                   │                              │ framing-related ...                                          │
│         │                │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-78660                   │
│         ├────────────────┤          │        │                   │                              ├──────────────────────────────────────────────────────────────┤
│         │ CVE-2026-78667 │          │        │                   │                              │ net/http: golang: golang: Denial of Service via crafted HTTP │
│         │                │          │        │                   │                              │ Range headers                                                │
│         │                │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-78667                   │
│         ├────────────────┤          │        │                   │                              ├──────────────────────────────────────────────────────────────┤
│         │ CVE-2026-78669 │          │        │                   │                              │ net/http: net/http/internal/http2: golang.org/x/net/http2:   │
│         │                │          │        │                   │                              │ net/http: Denial of Service via excessive HTTP/2 SETTINGS    │
│         │                │          │        │                   │                              │ frames...                                                    │
│         │                │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-78669                   │
│         ├────────────────┤          │        │                   │                              ├──────────────────────────────────────────────────────────────┤
│         │ CVE-2026-94440 │          │        │                   │                              │ Parsing a multipart form can bypass memory limits and read   │
│         │                │          │        │                   │                              │ an arbitrar...                                               │
│         │                │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-94440                   │
│         ├────────────────┤          │        │                   │                              ├──────────────────────────────────────────────────────────────┤
│         │ CVE-2026-97031 │          │        │                   │                              │ crypto/tls: golang: crypto/tls: Denial of Service via        │
│         │                │          │        │                   │                              │ multiple ECH outer extension references...                   │
│         │                │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-97031                   │
└─────────┴────────────────┴──────────┴────────┴───────────────────┴──────────────────────────────┴──────────────────────────────────────────────────────────────┘
```

## Scan Results: `registry.rancher.com/rancher/mirrored-cilium-clustermesh-apiserver:v1.20.3`

```text

usr/bin/etcd (gobinary)
=======================
Total: 11 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 11, CRITICAL: 0)

┌─────────────────────┬────────────────┬──────────┬────────┬───────────────────┬────────────────┬──────────────────────────────────────────────────────────────┐
│       Library       │ Vulnerability  │ Severity │ Status │ Installed Version │ Fixed Version  │                            Title                             │
├─────────────────────┼────────────────┼──────────┼────────┼───────────────────┼────────────────┼──────────────────────────────────────────────────────────────┤
│ golang.org/x/crypto │ CVE-2026-56855 │ HIGH     │ fixed  │ v0.55.0           │ 0.56.0         │ golang.org/x/crypto/ssh: golang.org/x/crypto/ssh: Denial of  │
│                     │                │          │        │                   │                │ Service via crafted messages                                 │
│                     │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-56855                   │
│                     ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                     │ CVE-2026-78662 │          │        │                   │                │ golang.org/x/crypto/ssh: golang.org/x/crypto/ssh: Denial of  │
│                     │                │          │        │                   │                │ Service via channel request flooding                         │
│                     │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-78662                   │
├─────────────────────┼────────────────┤          │        ├───────────────────┼────────────────┼──────────────────────────────────────────────────────────────┤
│ golang.org/x/net    │ CVE-2026-78659 │          │        │ v0.58.0           │ 0.60.0         │ When "Trailer" headers are sent by a client, the HTTP server │
│                     │                │          │        │                   │                │ internall...                                                 │
│                     │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-78659                   │
│                     ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                     │ CVE-2026-78660 │          │        │                   │                │ Historically, we have been rather lax about malformed        │
│                     │                │          │        │                   │                │ framing-related ...                                          │
│                     │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-78660                   │
│                     ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                     │ CVE-2026-78669 │          │        │                   │                │ net/http: net/http/internal/http2: golang.org/x/net/http2:   │
│                     │                │          │        │                   │                │ net/http: Denial of Service via excessive HTTP/2 SETTINGS    │
│                     │                │          │        │                   │                │ frames...                                                    │
│                     │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-78669                   │
├─────────────────────┼────────────────┤          │        ├───────────────────┼────────────────┼──────────────────────────────────────────────────────────────┤
│ stdlib              │ CVE-2026-56866 │          │        │ v1.26.8           │ 1.26.9, 1.27.2 │ net/http: golang: golang: Cross-user response poisoning via  │
│                     │                │          │        │                   │                │ desynchronized HTTP CONNECT connections                      │
│                     │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-56866                   │
│                     ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                     │ CVE-2026-78659 │          │        │                   │                │ When "Trailer" headers are sent by a client, the HTTP server │
│                     │                │          │        │                   │                │ internall...                                                 │
│                     │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-78659                   │
│                     ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                     │ CVE-2026-78660 │          │        │                   │                │ Historically, we have been rather lax about malformed        │
│                     │                │          │        │                   │                │ framing-related ...                                          │
│                     │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-78660                   │
│                     ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                     │ CVE-2026-78669 │          │        │                   │                │ net/http: net/http/internal/http2: golang.org/x/net/http2:   │
│                     │                │          │        │                   │                │ net/http: Denial of Service via excessive HTTP/2 SETTINGS    │
│                     │                │          │        │                   │                │ frames...                                                    │
│                     │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-78669                   │
│                     ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                     │ CVE-2026-94440 │          │        │                   │                │ Parsing a multipart form can bypass memory limits and read   │
│                     │                │          │        │                   │                │ an arbitrar...                                               │
│                     │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-94440                   │
│                     ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                     │ CVE-2026-97031 │          │        │                   │                │ crypto/tls: golang: crypto/tls: Denial of Service via        │
│                     │                │          │        │                   │                │ multiple ECH outer extension references...                   │
│                     │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-97031                   │
└─────────────────────┴────────────────┴──────────┴────────┴───────────────────┴────────────────┴──────────────────────────────────────────────────────────────┘
```

## Scan Results: `registry.rancher.com/rancher/mirrored-cilium-hubble-relay:v1.20.3`

```text
```

## Scan Results: `registry.rancher.com/rancher/mirrored-cilium-hubble-ui:v0.13.6`

```text

registry.rancher.com/rancher/mirrored-cilium-hubble-ui:v0.13.6 (alpine 3.24.1)
==============================================================================
Total: 1 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 1, CRITICAL: 0)

┌─────────┬─────────────────┬──────────┬────────┬───────────────────┬───────────────┬───────────────────────────────────────────────────────┐
│ Library │  Vulnerability  │ Severity │ Status │ Installed Version │ Fixed Version │                         Title                         │
├─────────┼─────────────────┼──────────┼────────┼───────────────────┼───────────────┼───────────────────────────────────────────────────────┤
│ pcre2   │ CVE-2026-103111 │ HIGH     │ fixed  │ 10.48-r0          │ 10.49-r0      │ pcre2: pcre2: Out-of-bounds write via crafted regular │
│         │                 │          │        │                   │               │ expression                                            │
│         │                 │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-103111           │
└─────────┴─────────────────┴──────────┴────────┴───────────────────┴───────────────┴───────────────────────────────────────────────────────┘
```

## Scan Results: `registry.rancher.com/rancher/mirrored-cilium-hubble-ui-backend:v0.13.6`

```text

usr/bin/backend (gobinary)
==========================
Total: 10 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 10, CRITICAL: 0)

┌──────────────────┬────────────────┬──────────┬────────┬───────────────────┬────────────────┬──────────────────────────────────────────────────────────────┐
│     Library      │ Vulnerability  │ Severity │ Status │ Installed Version │ Fixed Version  │                            Title                             │
├──────────────────┼────────────────┼──────────┼────────┼───────────────────┼────────────────┼──────────────────────────────────────────────────────────────┤
│ golang.org/x/net │ CVE-2026-78659 │ HIGH     │ fixed  │ v0.58.0           │ 0.60.0         │ When "Trailer" headers are sent by a client, the HTTP server │
│                  │                │          │        │                   │                │ internall...                                                 │
│                  │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-78659                   │
│                  ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                  │ CVE-2026-78660 │          │        │                   │                │ Historically, we have been rather lax about malformed        │
│                  │                │          │        │                   │                │ framing-related ...                                          │
│                  │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-78660                   │
│                  ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                  │ CVE-2026-78669 │          │        │                   │                │ net/http: net/http/internal/http2: golang.org/x/net/http2:   │
│                  │                │          │        │                   │                │ net/http: Denial of Service via excessive HTTP/2 SETTINGS    │
│                  │                │          │        │                   │                │ frames...                                                    │
│                  │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-78669                   │
├──────────────────┼────────────────┤          │        ├───────────────────┼────────────────┼──────────────────────────────────────────────────────────────┤
│ stdlib           │ CVE-2026-56866 │          │        │ v1.27.1           │ 1.26.9, 1.27.2 │ net/http: golang: golang: Cross-user response poisoning via  │
│                  │                │          │        │                   │                │ desynchronized HTTP CONNECT connections                      │
│                  │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-56866                   │
│                  ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                  │ CVE-2026-78659 │          │        │                   │                │ When "Trailer" headers are sent by a client, the HTTP server │
│                  │                │          │        │                   │                │ internall...                                                 │
│                  │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-78659                   │
│                  ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                  │ CVE-2026-78660 │          │        │                   │                │ Historically, we have been rather lax about malformed        │
│                  │                │          │        │                   │                │ framing-related ...                                          │
│                  │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-78660                   │
│                  ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                  │ CVE-2026-78667 │          │        │                   │                │ net/http: golang: golang: Denial of Service via crafted HTTP │
│                  │                │          │        │                   │                │ Range headers                                                │
│                  │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-78667                   │
│                  ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                  │ CVE-2026-78669 │          │        │                   │                │ net/http: net/http/internal/http2: golang.org/x/net/http2:   │
│                  │                │          │        │                   │                │ net/http: Denial of Service via excessive HTTP/2 SETTINGS    │
│                  │                │          │        │                   │                │ frames...                                                    │
│                  │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-78669                   │
│                  ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                  │ CVE-2026-94440 │          │        │                   │                │ Parsing a multipart form can bypass memory limits and read   │
│                  │                │          │        │                   │                │ an arbitrar...                                               │
│                  │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-94440                   │
│                  ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                  │ CVE-2026-97031 │          │        │                   │                │ crypto/tls: golang: crypto/tls: Denial of Service via        │
│                  │                │          │        │                   │                │ multiple ECH outer extension references...                   │
│                  │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-97031                   │
└──────────────────┴────────────────┴──────────┴────────┴───────────────────┴────────────────┴──────────────────────────────────────────────────────────────┘
```

## Scan Results: `registry.rancher.com/rancher/mirrored-cilium-operator-aws:v1.20.3`

```text
```

## Scan Results: `registry.rancher.com/rancher/mirrored-cilium-operator-azure:v1.20.3`

```text
```

## Scan Results: `registry.rancher.com/rancher/mirrored-cilium-operator-generic:v1.20.3`

```text
```

## Scan Results: `registry.rancher.com/rancher/hardened-cni-plugins:v1.9.1-build20261013`

```text
```

## Scan Results: `registry.rancher.com/rancher/mirrored-calico-operator:v1.42.6`

```text

usr/bin/operator (gobinary)
===========================
Total: 12 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 12, CRITICAL: 0)

┌─────────────────────┬────────────────┬──────────┬────────┬───────────────────┬────────────────┬──────────────────────────────────────────────────────────────┐
│       Library       │ Vulnerability  │ Severity │ Status │ Installed Version │ Fixed Version  │                            Title                             │
├─────────────────────┼────────────────┼──────────┼────────┼───────────────────┼────────────────┼──────────────────────────────────────────────────────────────┤
│ golang.org/x/crypto │ CVE-2026-56855 │ HIGH     │ fixed  │ v0.55.0           │ 0.56.0         │ golang.org/x/crypto/ssh: golang.org/x/crypto/ssh: Denial of  │
│                     │                │          │        │                   │                │ Service via crafted messages                                 │
│                     │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-56855                   │
│                     ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                     │ CVE-2026-78662 │          │        │                   │                │ golang.org/x/crypto/ssh: golang.org/x/crypto/ssh: Denial of  │
│                     │                │          │        │                   │                │ Service via channel request flooding                         │
│                     │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-78662                   │
├─────────────────────┼────────────────┤          │        ├───────────────────┼────────────────┼──────────────────────────────────────────────────────────────┤
│ golang.org/x/net    │ CVE-2026-78659 │          │        │ v0.58.0           │ 0.60.0         │ When "Trailer" headers are sent by a client, the HTTP server │
│                     │                │          │        │                   │                │ internall...                                                 │
│                     │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-78659                   │
│                     ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                     │ CVE-2026-78660 │          │        │                   │                │ Historically, we have been rather lax about malformed        │
│                     │                │          │        │                   │                │ framing-related ...                                          │
│                     │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-78660                   │
│                     ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                     │ CVE-2026-78669 │          │        │                   │                │ net/http: net/http/internal/http2: golang.org/x/net/http2:   │
│                     │                │          │        │                   │                │ net/http: Denial of Service via excessive HTTP/2 SETTINGS    │
│                     │                │          │        │                   │                │ frames...                                                    │
│                     │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-78669                   │
├─────────────────────┼────────────────┤          │        ├───────────────────┼────────────────┼──────────────────────────────────────────────────────────────┤
│ stdlib              │ CVE-2026-56866 │          │        │ v1.26.7           │ 1.26.9, 1.27.2 │ net/http: golang: golang: Cross-user response poisoning via  │
│                     │                │          │        │                   │                │ desynchronized HTTP CONNECT connections                      │
│                     │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-56866                   │
│                     ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                     │ CVE-2026-78659 │          │        │                   │                │ When "Trailer" headers are sent by a client, the HTTP server │
│                     │                │          │        │                   │                │ internall...                                                 │
│                     │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-78659                   │
│                     ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                     │ CVE-2026-78660 │          │        │                   │                │ Historically, we have been rather lax about malformed        │
│                     │                │          │        │                   │                │ framing-related ...                                          │
│                     │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-78660                   │
│                     ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                     │ CVE-2026-78667 │          │        │                   │                │ net/http: golang: golang: Denial of Service via crafted HTTP │
│                     │                │          │        │                   │                │ Range headers                                                │
│                     │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-78667                   │
│                     ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                     │ CVE-2026-78669 │          │        │                   │                │ net/http: net/http/internal/http2: golang.org/x/net/http2:   │
│                     │                │          │        │                   │                │ net/http: Denial of Service via excessive HTTP/2 SETTINGS    │
│                     │                │          │        │                   │                │ frames...                                                    │
│                     │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-78669                   │
│                     ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                     │ CVE-2026-94440 │          │        │                   │                │ Parsing a multipart form can bypass memory limits and read   │
│                     │                │          │        │                   │                │ an arbitrar...                                               │
│                     │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-94440                   │
│                     ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                     │ CVE-2026-97031 │          │        │                   │                │ crypto/tls: golang: crypto/tls: Denial of Service via        │
│                     │                │          │        │                   │                │ multiple ECH outer extension references...                   │
│                     │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-97031                   │
└─────────────────────┴────────────────┴──────────┴────────┴───────────────────┴────────────────┴──────────────────────────────────────────────────────────────┘
```

## Scan Results: `registry.rancher.com/rancher/mirrored-calico-ctl:v3.32.2`

```text

usr/bin/calicoctl (gobinary)
============================
Total: 15 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 14, CRITICAL: 1)

┌────────────────────────┬────────────────┬──────────┬────────┬───────────────────┬───────────────────────────────────────────────────────────┬──────────────────────────────────────────────────────────────┐
│        Library         │ Vulnerability  │ Severity │ Status │ Installed Version │                       Fixed Version                       │                            Title                             │
├────────────────────────┼────────────────┼──────────┼────────┼───────────────────┼───────────────────────────────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ golang.org/x/crypto    │ CVE-2026-56855 │ HIGH     │ fixed  │ v0.55.0           │ 0.56.0                                                    │ golang.org/x/crypto/ssh: golang.org/x/crypto/ssh: Denial of  │
│                        │                │          │        │                   │                                                           │ Service via crafted messages                                 │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-56855                   │
│                        ├────────────────┤          │        │                   │                                                           ├──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-78662 │          │        │                   │                                                           │ golang.org/x/crypto/ssh: golang.org/x/crypto/ssh: Denial of  │
│                        │                │          │        │                   │                                                           │ Service via channel request flooding                         │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-78662                   │
├────────────────────────┼────────────────┤          │        ├───────────────────┼───────────────────────────────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ golang.org/x/net       │ CVE-2026-78659 │          │        │ v0.58.0           │ 0.60.0                                                    │ When "Trailer" headers are sent by a client, the HTTP server │
│                        │                │          │        │                   │                                                           │ internall...                                                 │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-78659                   │
│                        ├────────────────┤          │        │                   │                                                           ├──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-78660 │          │        │                   │                                                           │ Historically, we have been rather lax about malformed        │
│                        │                │          │        │                   │                                                           │ framing-related ...                                          │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-78660                   │
│                        ├────────────────┤          │        │                   │                                                           ├──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-78669 │          │        │                   │                                                           │ net/http: net/http/internal/http2: golang.org/x/net/http2:   │
│                        │                │          │        │                   │                                                           │ net/http: Denial of Service via excessive HTTP/2 SETTINGS    │
│                        │                │          │        │                   │                                                           │ frames...                                                    │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-78669                   │
├────────────────────────┼────────────────┼──────────┤        ├───────────────────┼───────────────────────────────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ google.golang.org/grpc │ CVE-2026-84303 │ CRITICAL │        │ v1.82.1           │ 1.83.1                                                    │ gRPC-Go is the Go language implementation of gRPC. Prior to  │
│                        │                │          │        │                   │                                                           │ 1.83.1, th...                                                │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-84303                   │
│                        ├────────────────┼──────────┤        │                   │                                                           ├──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-84304 │ HIGH     │        │                   │                                                           │ google.golang.org/grpc: gRPC-Go: Denial of Service via       │
│                        │                │          │        │                   │                                                           │ HTTP/2 DATA Frame Fragmentation                              │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-84304                   │
│                        ├────────────────┤          │        │                   ├───────────────────────────────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-84445 │          │        │                   │ 1.82.2, 1.83.2, 1.84.0-dev.0.20260825144003-d5a41119e0e3, │ google.golang.org/grpc: gRPC-Go: Denial of Service via       │
│                        │                │          │        │                   │ 1.85.0-dev.0.20260825072537-93e31b48545e                  │ malformed RPC requests                                       │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-84445                   │
├────────────────────────┼────────────────┤          │        ├───────────────────┼───────────────────────────────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ stdlib                 │ CVE-2026-56866 │          │        │ v1.25.14          │ 1.26.9, 1.27.2                                            │ net/http: golang: golang: Cross-user response poisoning via  │
│                        │                │          │        │                   │                                                           │ desynchronized HTTP CONNECT connections                      │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-56866                   │
│                        ├────────────────┤          │        │                   │                                                           ├──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-78659 │          │        │                   │                                                           │ When "Trailer" headers are sent by a client, the HTTP server │
│                        │                │          │        │                   │                                                           │ internall...                                                 │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-78659                   │
│                        ├────────────────┤          │        │                   │                                                           ├──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-78660 │          │        │                   │                                                           │ Historically, we have been rather lax about malformed        │
│                        │                │          │        │                   │                                                           │ framing-related ...                                          │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-78660                   │
│                        ├────────────────┤          │        │                   │                                                           ├──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-78667 │          │        │                   │                                                           │ net/http: golang: golang: Denial of Service via crafted HTTP │
│                        │                │          │        │                   │                                                           │ Range headers                                                │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-78667                   │
│                        ├────────────────┤          │        │                   │                                                           ├──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-78669 │          │        │                   │                                                           │ net/http: net/http/internal/http2: golang.org/x/net/http2:   │
│                        │                │          │        │                   │                                                           │ net/http: Denial of Service via excessive HTTP/2 SETTINGS    │
│                        │                │          │        │                   │                                                           │ frames...                                                    │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-78669                   │
│                        ├────────────────┤          │        │                   │                                                           ├──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-94440 │          │        │                   │                                                           │ Parsing a multipart form can bypass memory limits and read   │
│                        │                │          │        │                   │                                                           │ an arbitrar...                                               │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-94440                   │
│                        ├────────────────┤          │        │                   │                                                           ├──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-97031 │          │        │                   │                                                           │ crypto/tls: golang: crypto/tls: Denial of Service via        │
│                        │                │          │        │                   │                                                           │ multiple ECH outer extension references...                   │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-97031                   │
└────────────────────────┴────────────────┴──────────┴────────┴───────────────────┴───────────────────────────────────────────────────────────┴──────────────────────────────────────────────────────────────┘
```

## Scan Results: `registry.rancher.com/rancher/mirrored-calico-kube-controllers:v3.32.2`

```text

usr/bin/kube-controllers (gobinary)
===================================
Total: 5 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 5, CRITICAL: 0)

┌────────────────────────┬────────────────┬──────────┬────────┬───────────────────┬───────────────────────────────────────────────────────────┬──────────────────────────────────────────────────────────────┐
│        Library         │ Vulnerability  │ Severity │ Status │ Installed Version │                       Fixed Version                       │                            Title                             │
├────────────────────────┼────────────────┼──────────┼────────┼───────────────────┼───────────────────────────────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ golang.org/x/net       │ CVE-2026-78659 │ HIGH     │ fixed  │ v0.58.0           │ 0.60.0                                                    │ When "Trailer" headers are sent by a client, the HTTP server │
│                        │                │          │        │                   │                                                           │ internall...                                                 │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-78659                   │
│                        ├────────────────┤          │        │                   │                                                           ├──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-78660 │          │        │                   │                                                           │ Historically, we have been rather lax about malformed        │
│                        │                │          │        │                   │                                                           │ framing-related ...                                          │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-78660                   │
│                        ├────────────────┤          │        │                   │                                                           ├──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-78669 │          │        │                   │                                                           │ net/http: net/http/internal/http2: golang.org/x/net/http2:   │
│                        │                │          │        │                   │                                                           │ net/http: Denial of Service via excessive HTTP/2 SETTINGS    │
│                        │                │          │        │                   │                                                           │ frames...                                                    │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-78669                   │
├────────────────────────┼────────────────┤          │        ├───────────────────┼───────────────────────────────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ google.golang.org/grpc │ CVE-2026-84304 │          │        │ v1.82.1           │ 1.83.1                                                    │ google.golang.org/grpc: gRPC-Go: Denial of Service via       │
│                        │                │          │        │                   │                                                           │ HTTP/2 DATA Frame Fragmentation                              │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-84304                   │
│                        ├────────────────┤          │        │                   ├───────────────────────────────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-84445 │          │        │                   │ 1.82.2, 1.83.2, 1.84.0-dev.0.20260825144003-d5a41119e0e3, │ google.golang.org/grpc: gRPC-Go: Denial of Service via       │
│                        │                │          │        │                   │ 1.85.0-dev.0.20260825072537-93e31b48545e                  │ malformed RPC requests                                       │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-84445                   │
└────────────────────────┴────────────────┴──────────┴────────┴───────────────────┴───────────────────────────────────────────────────────────┴──────────────────────────────────────────────────────────────┘

usr/bin/wrapper (gobinary)
==========================
Total: 3 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 3, CRITICAL: 0)

┌──────────────────┬────────────────┬──────────┬────────┬───────────────────┬───────────────┬──────────────────────────────────────────────────────────────┐
│     Library      │ Vulnerability  │ Severity │ Status │ Installed Version │ Fixed Version │                            Title                             │
├──────────────────┼────────────────┼──────────┼────────┼───────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ golang.org/x/net │ CVE-2026-78659 │ HIGH     │ fixed  │ v0.58.0           │ 0.60.0        │ When "Trailer" headers are sent by a client, the HTTP server │
│                  │                │          │        │                   │               │ internall...                                                 │
│                  │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-78659                   │
│                  ├────────────────┤          │        │                   │               ├──────────────────────────────────────────────────────────────┤
│                  │ CVE-2026-78660 │          │        │                   │               │ Historically, we have been rather lax about malformed        │
│                  │                │          │        │                   │               │ framing-related ...                                          │
│                  │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-78660                   │
│                  ├────────────────┤          │        │                   │               ├──────────────────────────────────────────────────────────────┤
│                  │ CVE-2026-78669 │          │        │                   │               │ net/http: net/http/internal/http2: golang.org/x/net/http2:   │
│                  │                │          │        │                   │               │ net/http: Denial of Service via excessive HTTP/2 SETTINGS    │
│                  │                │          │        │                   │               │ frames...                                                    │
│                  │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-78669                   │
└──────────────────┴────────────────┴──────────┴────────┴───────────────────┴───────────────┴──────────────────────────────────────────────────────────────┘
```

## Scan Results: `registry.rancher.com/rancher/mirrored-calico-typha:v3.32.2`

```text

usr/bin/calico-typha (gobinary)
===============================
Total: 5 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 5, CRITICAL: 0)

┌────────────────────────┬────────────────┬──────────┬────────┬───────────────────┬───────────────────────────────────────────────────────────┬──────────────────────────────────────────────────────────────┐
│        Library         │ Vulnerability  │ Severity │ Status │ Installed Version │                       Fixed Version                       │                            Title                             │
├────────────────────────┼────────────────┼──────────┼────────┼───────────────────┼───────────────────────────────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ golang.org/x/net       │ CVE-2026-78659 │ HIGH     │ fixed  │ v0.58.0           │ 0.60.0                                                    │ When "Trailer" headers are sent by a client, the HTTP server │
│                        │                │          │        │                   │                                                           │ internall...                                                 │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-78659                   │
│                        ├────────────────┤          │        │                   │                                                           ├──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-78660 │          │        │                   │                                                           │ Historically, we have been rather lax about malformed        │
│                        │                │          │        │                   │                                                           │ framing-related ...                                          │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-78660                   │
│                        ├────────────────┤          │        │                   │                                                           ├──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-78669 │          │        │                   │                                                           │ net/http: net/http/internal/http2: golang.org/x/net/http2:   │
│                        │                │          │        │                   │                                                           │ net/http: Denial of Service via excessive HTTP/2 SETTINGS    │
│                        │                │          │        │                   │                                                           │ frames...                                                    │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-78669                   │
├────────────────────────┼────────────────┤          │        ├───────────────────┼───────────────────────────────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ google.golang.org/grpc │ CVE-2026-84304 │          │        │ v1.82.1           │ 1.83.1                                                    │ google.golang.org/grpc: gRPC-Go: Denial of Service via       │
│                        │                │          │        │                   │                                                           │ HTTP/2 DATA Frame Fragmentation                              │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-84304                   │
│                        ├────────────────┤          │        │                   ├───────────────────────────────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-84445 │          │        │                   │ 1.82.2, 1.83.2, 1.84.0-dev.0.20260825144003-d5a41119e0e3, │ google.golang.org/grpc: gRPC-Go: Denial of Service via       │
│                        │                │          │        │                   │ 1.85.0-dev.0.20260825072537-93e31b48545e                  │ malformed RPC requests                                       │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-84445                   │
└────────────────────────┴────────────────┴──────────┴────────┴───────────────────┴───────────────────────────────────────────────────────────┴──────────────────────────────────────────────────────────────┘
```

## Scan Results: `registry.rancher.com/rancher/mirrored-calico-node:v3.32.2`

```text

registry.rancher.com/rancher/mirrored-calico-node:v3.32.2 (redhat 9.8)
======================================================================
Total: 4 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 4, CRITICAL: 0)

┌─────────────────┬────────────────┬──────────┬──────────┬───────────────────┬─────────────────┬──────────────────────────────────────────────────────────────┐
│     Library     │ Vulnerability  │ Severity │  Status  │ Installed Version │  Fixed Version  │                            Title                             │
├─────────────────┼────────────────┼──────────┼──────────┼───────────────────┼─────────────────┼──────────────────────────────────────────────────────────────┤
│ openssl-libs    │ CVE-2026-84782 │ HIGH     │ fixed    │ 1:3.5.5-6.el9_8   │ 1:3.5.8-2.el9_8 │ openssl: compat-openssl: openssl: Information disclosure via │
│                 │                │          │          │                   │                 │ DTLS handshake retransmission                                │
│                 │                │          │          │                   │                 │ https://avd.aquasec.com/nvd/cve-2026-84782                   │
├─────────────────┼────────────────┤          ├──────────┼───────────────────┼─────────────────┼──────────────────────────────────────────────────────────────┤
│ util-linux      │ CVE-2026-53615 │          │ affected │ 2.37.4-25.el9     │                 │ util-linux: util-linux: Partition metadata compromise via    │
│                 │                │          │          │                   │                 │ integer overflow in DOS partition parser...                  │
│                 │                │          │          │                   │                 │ https://avd.aquasec.com/nvd/cve-2026-53615                   │
├─────────────────┼────────────────┤          │          │                   ├─────────────────┼──────────────────────────────────────────────────────────────┤
│ util-linux-core │ CVE-2026-53613 │          │          │                   │                 │ util-linux: util-linux: TOCTOU in the mount program via      │
│                 │                │          │          │                   │                 │ ancestor directory swap on...                                │
│                 │                │          │          │                   │                 │ https://avd.aquasec.com/nvd/cve-2026-53613                   │
│                 ├────────────────┤          │          │                   ├─────────────────┼──────────────────────────────────────────────────────────────┤
│                 │ CVE-2026-53615 │          │          │                   │                 │ util-linux: util-linux: Partition metadata compromise via    │
│                 │                │          │          │                   │                 │ integer overflow in DOS partition parser...                  │
│                 │                │          │          │                   │                 │ https://avd.aquasec.com/nvd/cve-2026-53615                   │
└─────────────────┴────────────────┴──────────┴──────────┴───────────────────┴─────────────────┴──────────────────────────────────────────────────────────────┘

usr/bin/calico-node (gobinary)
==============================
Total: 15 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 14, CRITICAL: 1)

┌────────────────────────┬────────────────┬──────────┬────────┬───────────────────┬───────────────────────────────────────────────────────────┬──────────────────────────────────────────────────────────────┐
│        Library         │ Vulnerability  │ Severity │ Status │ Installed Version │                       Fixed Version                       │                            Title                             │
├────────────────────────┼────────────────┼──────────┼────────┼───────────────────┼───────────────────────────────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ golang.org/x/crypto    │ CVE-2026-56855 │ HIGH     │ fixed  │ v0.55.0           │ 0.56.0                                                    │ golang.org/x/crypto/ssh: golang.org/x/crypto/ssh: Denial of  │
│                        │                │          │        │                   │                                                           │ Service via crafted messages                                 │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-56855                   │
│                        ├────────────────┤          │        │                   │                                                           ├──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-78662 │          │        │                   │                                                           │ golang.org/x/crypto/ssh: golang.org/x/crypto/ssh: Denial of  │
│                        │                │          │        │                   │                                                           │ Service via channel request flooding                         │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-78662                   │
├────────────────────────┼────────────────┤          │        ├───────────────────┼───────────────────────────────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ golang.org/x/net       │ CVE-2026-78659 │          │        │ v0.58.0           │ 0.60.0                                                    │ When "Trailer" headers are sent by a client, the HTTP server │
│                        │                │          │        │                   │                                                           │ internall...                                                 │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-78659                   │
│                        ├────────────────┤          │        │                   │                                                           ├──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-78660 │          │        │                   │                                                           │ Historically, we have been rather lax about malformed        │
│                        │                │          │        │                   │                                                           │ framing-related ...                                          │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-78660                   │
│                        ├────────────────┤          │        │                   │                                                           ├──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-78669 │          │        │                   │                                                           │ net/http: net/http/internal/http2: golang.org/x/net/http2:   │
│                        │                │          │        │                   │                                                           │ net/http: Denial of Service via excessive HTTP/2 SETTINGS    │
│                        │                │          │        │                   │                                                           │ frames...                                                    │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-78669                   │
├────────────────────────┼────────────────┼──────────┤        ├───────────────────┼───────────────────────────────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ google.golang.org/grpc │ CVE-2026-84303 │ CRITICAL │        │ v1.82.1           │ 1.83.1                                                    │ gRPC-Go is the Go language implementation of gRPC. Prior to  │
│                        │                │          │        │                   │                                                           │ 1.83.1, th...                                                │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-84303                   │
│                        ├────────────────┼──────────┤        │                   │                                                           ├──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-84304 │ HIGH     │        │                   │                                                           │ google.golang.org/grpc: gRPC-Go: Denial of Service via       │
│                        │                │          │        │                   │                                                           │ HTTP/2 DATA Frame Fragmentation                              │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-84304                   │
│                        ├────────────────┤          │        │                   ├───────────────────────────────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-84445 │          │        │                   │ 1.82.2, 1.83.2, 1.84.0-dev.0.20260825144003-d5a41119e0e3, │ google.golang.org/grpc: gRPC-Go: Denial of Service via       │
│                        │                │          │        │                   │ 1.85.0-dev.0.20260825072537-93e31b48545e                  │ malformed RPC requests                                       │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-84445                   │
├────────────────────────┼────────────────┤          │        ├───────────────────┼───────────────────────────────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ stdlib                 │ CVE-2026-56866 │          │        │ v1.25.14          │ 1.26.9, 1.27.2                                            │ net/http: golang: golang: Cross-user response poisoning via  │
│                        │                │          │        │                   │                                                           │ desynchronized HTTP CONNECT connections                      │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-56866                   │
│                        ├────────────────┤          │        │                   │                                                           ├──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-78659 │          │        │                   │                                                           │ When "Trailer" headers are sent by a client, the HTTP server │
│                        │                │          │        │                   │                                                           │ internall...                                                 │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-78659                   │
│                        ├────────────────┤          │        │                   │                                                           ├──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-78660 │          │        │                   │                                                           │ Historically, we have been rather lax about malformed        │
│                        │                │          │        │                   │                                                           │ framing-related ...                                          │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-78660                   │
│                        ├────────────────┤          │        │                   │                                                           ├──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-78667 │          │        │                   │                                                           │ net/http: golang: golang: Denial of Service via crafted HTTP │
│                        │                │          │        │                   │                                                           │ Range headers                                                │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-78667                   │
│                        ├────────────────┤          │        │                   │                                                           ├──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-78669 │          │        │                   │                                                           │ net/http: net/http/internal/http2: golang.org/x/net/http2:   │
│                        │                │          │        │                   │                                                           │ net/http: Denial of Service via excessive HTTP/2 SETTINGS    │
│                        │                │          │        │                   │                                                           │ frames...                                                    │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-78669                   │
│                        ├────────────────┤          │        │                   │                                                           ├──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-94440 │          │        │                   │                                                           │ Parsing a multipart form can bypass memory limits and read   │
│                        │                │          │        │                   │                                                           │ an arbitrar...                                               │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-94440                   │
│                        ├────────────────┤          │        │                   │                                                           ├──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-97031 │          │        │                   │                                                           │ crypto/tls: golang: crypto/tls: Denial of Service via        │
│                        │                │          │        │                   │                                                           │ multiple ECH outer extension references...                   │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-97031                   │
└────────────────────────┴────────────────┴──────────┴────────┴───────────────────┴───────────────────────────────────────────────────────────┴──────────────────────────────────────────────────────────────┘
```

## Scan Results: `registry.rancher.com/rancher/mirrored-calico-pod2daemon-flexvol:v3.32.2`

```text

usr/local/bin/flexvol (gobinary)
================================
Total: 7 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 7, CRITICAL: 0)

┌─────────┬────────────────┬──────────┬────────┬───────────────────┬────────────────┬──────────────────────────────────────────────────────────────┐
│ Library │ Vulnerability  │ Severity │ Status │ Installed Version │ Fixed Version  │                            Title                             │
├─────────┼────────────────┼──────────┼────────┼───────────────────┼────────────────┼──────────────────────────────────────────────────────────────┤
│ stdlib  │ CVE-2026-56866 │ HIGH     │ fixed  │ v1.25.14          │ 1.26.9, 1.27.2 │ net/http: golang: golang: Cross-user response poisoning via  │
│         │                │          │        │                   │                │ desynchronized HTTP CONNECT connections                      │
│         │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-56866                   │
│         ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│         │ CVE-2026-78659 │          │        │                   │                │ When "Trailer" headers are sent by a client, the HTTP server │
│         │                │          │        │                   │                │ internall...                                                 │
│         │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-78659                   │
│         ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│         │ CVE-2026-78660 │          │        │                   │                │ Historically, we have been rather lax about malformed        │
│         │                │          │        │                   │                │ framing-related ...                                          │
│         │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-78660                   │
│         ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│         │ CVE-2026-78667 │          │        │                   │                │ net/http: golang: golang: Denial of Service via crafted HTTP │
│         │                │          │        │                   │                │ Range headers                                                │
│         │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-78667                   │
│         ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│         │ CVE-2026-78669 │          │        │                   │                │ net/http: net/http/internal/http2: golang.org/x/net/http2:   │
│         │                │          │        │                   │                │ net/http: Denial of Service via excessive HTTP/2 SETTINGS    │
│         │                │          │        │                   │                │ frames...                                                    │
│         │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-78669                   │
│         ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│         │ CVE-2026-94440 │          │        │                   │                │ Parsing a multipart form can bypass memory limits and read   │
│         │                │          │        │                   │                │ an arbitrar...                                               │
│         │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-94440                   │
│         ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│         │ CVE-2026-97031 │          │        │                   │                │ crypto/tls: golang: crypto/tls: Denial of Service via        │
│         │                │          │        │                   │                │ multiple ECH outer extension references...                   │
│         │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-97031                   │
└─────────┴────────────────┴──────────┴────────┴───────────────────┴────────────────┴──────────────────────────────────────────────────────────────┘
```

## Scan Results: `registry.rancher.com/rancher/mirrored-calico-cni:v3.32.2`

```text

opt/cni/bin/calico (gobinary)
=============================
Total: 5 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 5, CRITICAL: 0)

┌────────────────────────┬────────────────┬──────────┬────────┬───────────────────┬───────────────────────────────────────────────────────────┬──────────────────────────────────────────────────────────────┐
│        Library         │ Vulnerability  │ Severity │ Status │ Installed Version │                       Fixed Version                       │                            Title                             │
├────────────────────────┼────────────────┼──────────┼────────┼───────────────────┼───────────────────────────────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ golang.org/x/net       │ CVE-2026-78659 │ HIGH     │ fixed  │ v0.58.0           │ 0.60.0                                                    │ When "Trailer" headers are sent by a client, the HTTP server │
│                        │                │          │        │                   │                                                           │ internall...                                                 │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-78659                   │
│                        ├────────────────┤          │        │                   │                                                           ├──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-78660 │          │        │                   │                                                           │ Historically, we have been rather lax about malformed        │
│                        │                │          │        │                   │                                                           │ framing-related ...                                          │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-78660                   │
│                        ├────────────────┤          │        │                   │                                                           ├──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-78669 │          │        │                   │                                                           │ net/http: net/http/internal/http2: golang.org/x/net/http2:   │
│                        │                │          │        │                   │                                                           │ net/http: Denial of Service via excessive HTTP/2 SETTINGS    │
│                        │                │          │        │                   │                                                           │ frames...                                                    │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-78669                   │
├────────────────────────┼────────────────┤          │        ├───────────────────┼───────────────────────────────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ google.golang.org/grpc │ CVE-2026-84304 │          │        │ v1.82.1           │ 1.83.1                                                    │ google.golang.org/grpc: gRPC-Go: Denial of Service via       │
│                        │                │          │        │                   │                                                           │ HTTP/2 DATA Frame Fragmentation                              │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-84304                   │
│                        ├────────────────┤          │        │                   ├───────────────────────────────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-84445 │          │        │                   │ 1.82.2, 1.83.2, 1.84.0-dev.0.20260825144003-d5a41119e0e3, │ google.golang.org/grpc: gRPC-Go: Denial of Service via       │
│                        │                │          │        │                   │ 1.85.0-dev.0.20260825072537-93e31b48545e                  │ malformed RPC requests                                       │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-84445                   │
└────────────────────────┴────────────────┴──────────┴────────┴───────────────────┴───────────────────────────────────────────────────────────┴──────────────────────────────────────────────────────────────┘

opt/cni/bin/install (gobinary)
==============================
Total: 3 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 3, CRITICAL: 0)

┌──────────────────┬────────────────┬──────────┬────────┬───────────────────┬───────────────┬──────────────────────────────────────────────────────────────┐
│     Library      │ Vulnerability  │ Severity │ Status │ Installed Version │ Fixed Version │                            Title                             │
├──────────────────┼────────────────┼──────────┼────────┼───────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ golang.org/x/net │ CVE-2026-78659 │ HIGH     │ fixed  │ v0.58.0           │ 0.60.0        │ When "Trailer" headers are sent by a client, the HTTP server │
│                  │                │          │        │                   │               │ internall...                                                 │
│                  │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-78659                   │
│                  ├────────────────┤          │        │                   │               ├──────────────────────────────────────────────────────────────┤
│                  │ CVE-2026-78660 │          │        │                   │               │ Historically, we have been rather lax about malformed        │
│                  │                │          │        │                   │               │ framing-related ...                                          │
│                  │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-78660                   │
│                  ├────────────────┤          │        │                   │               ├──────────────────────────────────────────────────────────────┤
│                  │ CVE-2026-78669 │          │        │                   │               │ net/http: net/http/internal/http2: golang.org/x/net/http2:   │
│                  │                │          │        │                   │               │ net/http: Denial of Service via excessive HTTP/2 SETTINGS    │
│                  │                │          │        │                   │               │ frames...                                                    │
│                  │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-78669                   │
└──────────────────┴────────────────┴──────────┴────────┴───────────────────┴───────────────┴──────────────────────────────────────────────────────────────┘
```

## Scan Results: `registry.rancher.com/rancher/mirrored-calico-apiserver:v3.32.2`

```text

code/apiserver (gobinary)
=========================
Total: 5 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 5, CRITICAL: 0)

┌────────────────────────┬────────────────┬──────────┬────────┬───────────────────┬───────────────────────────────────────────────────────────┬──────────────────────────────────────────────────────────────┐
│        Library         │ Vulnerability  │ Severity │ Status │ Installed Version │                       Fixed Version                       │                            Title                             │
├────────────────────────┼────────────────┼──────────┼────────┼───────────────────┼───────────────────────────────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ golang.org/x/net       │ CVE-2026-78659 │ HIGH     │ fixed  │ v0.58.0           │ 0.60.0                                                    │ When "Trailer" headers are sent by a client, the HTTP server │
│                        │                │          │        │                   │                                                           │ internall...                                                 │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-78659                   │
│                        ├────────────────┤          │        │                   │                                                           ├──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-78660 │          │        │                   │                                                           │ Historically, we have been rather lax about malformed        │
│                        │                │          │        │                   │                                                           │ framing-related ...                                          │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-78660                   │
│                        ├────────────────┤          │        │                   │                                                           ├──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-78669 │          │        │                   │                                                           │ net/http: net/http/internal/http2: golang.org/x/net/http2:   │
│                        │                │          │        │                   │                                                           │ net/http: Denial of Service via excessive HTTP/2 SETTINGS    │
│                        │                │          │        │                   │                                                           │ frames...                                                    │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-78669                   │
├────────────────────────┼────────────────┤          │        ├───────────────────┼───────────────────────────────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ google.golang.org/grpc │ CVE-2026-84304 │          │        │ v1.82.1           │ 1.83.1                                                    │ google.golang.org/grpc: gRPC-Go: Denial of Service via       │
│                        │                │          │        │                   │                                                           │ HTTP/2 DATA Frame Fragmentation                              │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-84304                   │
│                        ├────────────────┤          │        │                   ├───────────────────────────────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-84445 │          │        │                   │ 1.82.2, 1.83.2, 1.84.0-dev.0.20260825144003-d5a41119e0e3, │ google.golang.org/grpc: gRPC-Go: Denial of Service via       │
│                        │                │          │        │                   │ 1.85.0-dev.0.20260825072537-93e31b48545e                  │ malformed RPC requests                                       │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-84445                   │
└────────────────────────┴────────────────┴──────────┴────────┴───────────────────┴───────────────────────────────────────────────────────────┴──────────────────────────────────────────────────────────────┘
```

## Scan Results: `registry.rancher.com/rancher/mirrored-calico-csi:v3.32.2`

```text

usr/bin/csi-driver (gobinary)
=============================
Total: 13 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 12, CRITICAL: 1)

┌────────────────────────┬────────────────┬──────────┬────────┬───────────────────┬───────────────────────────────────────────────────────────┬──────────────────────────────────────────────────────────────┐
│        Library         │ Vulnerability  │ Severity │ Status │ Installed Version │                       Fixed Version                       │                            Title                             │
├────────────────────────┼────────────────┼──────────┼────────┼───────────────────┼───────────────────────────────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ golang.org/x/net       │ CVE-2026-78659 │ HIGH     │ fixed  │ v0.58.0           │ 0.60.0                                                    │ When "Trailer" headers are sent by a client, the HTTP server │
│                        │                │          │        │                   │                                                           │ internall...                                                 │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-78659                   │
│                        ├────────────────┤          │        │                   │                                                           ├──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-78660 │          │        │                   │                                                           │ Historically, we have been rather lax about malformed        │
│                        │                │          │        │                   │                                                           │ framing-related ...                                          │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-78660                   │
│                        ├────────────────┤          │        │                   │                                                           ├──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-78669 │          │        │                   │                                                           │ net/http: net/http/internal/http2: golang.org/x/net/http2:   │
│                        │                │          │        │                   │                                                           │ net/http: Denial of Service via excessive HTTP/2 SETTINGS    │
│                        │                │          │        │                   │                                                           │ frames...                                                    │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-78669                   │
├────────────────────────┼────────────────┼──────────┤        ├───────────────────┼───────────────────────────────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ google.golang.org/grpc │ CVE-2026-84303 │ CRITICAL │        │ v1.82.1           │ 1.83.1                                                    │ gRPC-Go is the Go language implementation of gRPC. Prior to  │
│                        │                │          │        │                   │                                                           │ 1.83.1, th...                                                │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-84303                   │
│                        ├────────────────┼──────────┤        │                   │                                                           ├──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-84304 │ HIGH     │        │                   │                                                           │ google.golang.org/grpc: gRPC-Go: Denial of Service via       │
│                        │                │          │        │                   │                                                           │ HTTP/2 DATA Frame Fragmentation                              │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-84304                   │
│                        ├────────────────┤          │        │                   ├───────────────────────────────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-84445 │          │        │                   │ 1.82.2, 1.83.2, 1.84.0-dev.0.20260825144003-d5a41119e0e3, │ google.golang.org/grpc: gRPC-Go: Denial of Service via       │
│                        │                │          │        │                   │ 1.85.0-dev.0.20260825072537-93e31b48545e                  │ malformed RPC requests                                       │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-84445                   │
├────────────────────────┼────────────────┤          │        ├───────────────────┼───────────────────────────────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ stdlib                 │ CVE-2026-56866 │          │        │ v1.25.14          │ 1.26.9, 1.27.2                                            │ net/http: golang: golang: Cross-user response poisoning via  │
│                        │                │          │        │                   │                                                           │ desynchronized HTTP CONNECT connections                      │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-56866                   │
│                        ├────────────────┤          │        │                   │                                                           ├──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-78659 │          │        │                   │                                                           │ When "Trailer" headers are sent by a client, the HTTP server │
│                        │                │          │        │                   │                                                           │ internall...                                                 │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-78659                   │
│                        ├────────────────┤          │        │                   │                                                           ├──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-78660 │          │        │                   │                                                           │ Historically, we have been rather lax about malformed        │
│                        │                │          │        │                   │                                                           │ framing-related ...                                          │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-78660                   │
│                        ├────────────────┤          │        │                   │                                                           ├──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-78667 │          │        │                   │                                                           │ net/http: golang: golang: Denial of Service via crafted HTTP │
│                        │                │          │        │                   │                                                           │ Range headers                                                │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-78667                   │
│                        ├────────────────┤          │        │                   │                                                           ├──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-78669 │          │        │                   │                                                           │ net/http: net/http/internal/http2: golang.org/x/net/http2:   │
│                        │                │          │        │                   │                                                           │ net/http: Denial of Service via excessive HTTP/2 SETTINGS    │
│                        │                │          │        │                   │                                                           │ frames...                                                    │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-78669                   │
│                        ├────────────────┤          │        │                   │                                                           ├──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-94440 │          │        │                   │                                                           │ Parsing a multipart form can bypass memory limits and read   │
│                        │                │          │        │                   │                                                           │ an arbitrar...                                               │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-94440                   │
│                        ├────────────────┤          │        │                   │                                                           ├──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-97031 │          │        │                   │                                                           │ crypto/tls: golang: crypto/tls: Denial of Service via        │
│                        │                │          │        │                   │                                                           │ multiple ECH outer extension references...                   │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-97031                   │
└────────────────────────┴────────────────┴──────────┴────────┴───────────────────┴───────────────────────────────────────────────────────────┴──────────────────────────────────────────────────────────────┘
```

## Scan Results: `registry.rancher.com/rancher/mirrored-calico-node-driver-registrar:v3.32.2`

```text

usr/bin/node-driver-registrar (gobinary)
========================================
Total: 14 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 13, CRITICAL: 1)

┌────────────────────────┬────────────────┬──────────┬────────┬───────────────────┬───────────────────────────────────────────────────────────┬──────────────────────────────────────────────────────────────┐
│        Library         │ Vulnerability  │ Severity │ Status │ Installed Version │                       Fixed Version                       │                            Title                             │
├────────────────────────┼────────────────┼──────────┼────────┼───────────────────┼───────────────────────────────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ golang.org/x/net       │ CVE-2026-78659 │ HIGH     │ fixed  │ v0.56.0           │ 0.60.0                                                    │ When "Trailer" headers are sent by a client, the HTTP server │
│                        │                │          │        │                   │                                                           │ internall...                                                 │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-78659                   │
│                        ├────────────────┤          │        │                   │                                                           ├──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-78660 │          │        │                   │                                                           │ Historically, we have been rather lax about malformed        │
│                        │                │          │        │                   │                                                           │ framing-related ...                                          │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-78660                   │
│                        ├────────────────┤          │        │                   │                                                           ├──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-78669 │          │        │                   │                                                           │ net/http: net/http/internal/http2: golang.org/x/net/http2:   │
│                        │                │          │        │                   │                                                           │ net/http: Denial of Service via excessive HTTP/2 SETTINGS    │
│                        │                │          │        │                   │                                                           │ frames...                                                    │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-78669                   │
├────────────────────────┼────────────────┤          │        ├───────────────────┼───────────────────────────────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ golang.org/x/text      │ CVE-2026-56851 │          │        │ v0.39.0           │ 0.41.0                                                    │ golang.org/x/text: golang.org/x/text: Denial of Service via  │
│                        │                │          │        │                   │                                                           │ out-of-bounds slice error in Nickname profile...             │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-56851                   │
├────────────────────────┼────────────────┼──────────┤        ├───────────────────┼───────────────────────────────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ google.golang.org/grpc │ CVE-2026-84303 │ CRITICAL │        │ v1.82.1           │ 1.83.1                                                    │ gRPC-Go is the Go language implementation of gRPC. Prior to  │
│                        │                │          │        │                   │                                                           │ 1.83.1, th...                                                │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-84303                   │
│                        ├────────────────┼──────────┤        │                   │                                                           ├──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-84304 │ HIGH     │        │                   │                                                           │ google.golang.org/grpc: gRPC-Go: Denial of Service via       │
│                        │                │          │        │                   │                                                           │ HTTP/2 DATA Frame Fragmentation                              │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-84304                   │
│                        ├────────────────┤          │        │                   ├───────────────────────────────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-84445 │          │        │                   │ 1.82.2, 1.83.2, 1.84.0-dev.0.20260825144003-d5a41119e0e3, │ google.golang.org/grpc: gRPC-Go: Denial of Service via       │
│                        │                │          │        │                   │ 1.85.0-dev.0.20260825072537-93e31b48545e                  │ malformed RPC requests                                       │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-84445                   │
├────────────────────────┼────────────────┤          │        ├───────────────────┼───────────────────────────────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ stdlib                 │ CVE-2026-56866 │          │        │ v1.25.14          │ 1.26.9, 1.27.2                                            │ net/http: golang: golang: Cross-user response poisoning via  │
│                        │                │          │        │                   │                                                           │ desynchronized HTTP CONNECT connections                      │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-56866                   │
│                        ├────────────────┤          │        │                   │                                                           ├──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-78659 │          │        │                   │                                                           │ When "Trailer" headers are sent by a client, the HTTP server │
│                        │                │          │        │                   │                                                           │ internall...                                                 │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-78659                   │
│                        ├────────────────┤          │        │                   │                                                           ├──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-78660 │          │        │                   │                                                           │ Historically, we have been rather lax about malformed        │
│                        │                │          │        │                   │                                                           │ framing-related ...                                          │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-78660                   │
│                        ├────────────────┤          │        │                   │                                                           ├──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-78667 │          │        │                   │                                                           │ net/http: golang: golang: Denial of Service via crafted HTTP │
│                        │                │          │        │                   │                                                           │ Range headers                                                │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-78667                   │
│                        ├────────────────┤          │        │                   │                                                           ├──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-78669 │          │        │                   │                                                           │ net/http: net/http/internal/http2: golang.org/x/net/http2:   │
│                        │                │          │        │                   │                                                           │ net/http: Denial of Service via excessive HTTP/2 SETTINGS    │
│                        │                │          │        │                   │                                                           │ frames...                                                    │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-78669                   │
│                        ├────────────────┤          │        │                   │                                                           ├──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-94440 │          │        │                   │                                                           │ Parsing a multipart form can bypass memory limits and read   │
│                        │                │          │        │                   │                                                           │ an arbitrar...                                               │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-94440                   │
│                        ├────────────────┤          │        │                   │                                                           ├──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-97031 │          │        │                   │                                                           │ crypto/tls: golang: crypto/tls: Denial of Service via        │
│                        │                │          │        │                   │                                                           │ multiple ECH outer extension references...                   │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-97031                   │
└────────────────────────┴────────────────┴──────────┴────────┴───────────────────┴───────────────────────────────────────────────────────────┴──────────────────────────────────────────────────────────────┘
```

## Scan Results: `registry.rancher.com/rancher/mirrored-calico-envoy-gateway:v3.32.2`

```text

usr/local/bin/envoy-gateway (gobinary)
======================================
Total: 17 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 16, CRITICAL: 1)

┌────────────────────────┬────────────────┬──────────┬────────┬───────────────────┬───────────────────────────────────────────────────────────┬──────────────────────────────────────────────────────────────┐
│        Library         │ Vulnerability  │ Severity │ Status │ Installed Version │                       Fixed Version                       │                            Title                             │
├────────────────────────┼────────────────┼──────────┼────────┼───────────────────┼───────────────────────────────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ golang.org/x/crypto    │ CVE-2026-56854 │ HIGH     │ fixed  │ v0.54.0           │ 0.55.0                                                    │ golang.org/x/crypto/ssh: golang.org/x/crypto/ssh:            │
│                        │                │          │        │                   │                                                           │ Authentication bypass due to unenforced source-address       │
│                        │                │          │        │                   │                                                           │ restrictions                                                 │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-56854                   │
│                        ├────────────────┤          │        │                   ├───────────────────────────────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-56855 │          │        │                   │ 0.56.0                                                    │ golang.org/x/crypto/ssh: golang.org/x/crypto/ssh: Denial of  │
│                        │                │          │        │                   │                                                           │ Service via crafted messages                                 │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-56855                   │
│                        ├────────────────┤          │        │                   │                                                           ├──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-78662 │          │        │                   │                                                           │ golang.org/x/crypto/ssh: golang.org/x/crypto/ssh: Denial of  │
│                        │                │          │        │                   │                                                           │ Service via channel request flooding                         │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-78662                   │
├────────────────────────┼────────────────┤          │        ├───────────────────┼───────────────────────────────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ golang.org/x/net       │ CVE-2026-78659 │          │        │ v0.57.0           │ 0.60.0                                                    │ When "Trailer" headers are sent by a client, the HTTP server │
│                        │                │          │        │                   │                                                           │ internall...                                                 │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-78659                   │
│                        ├────────────────┤          │        │                   │                                                           ├──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-78660 │          │        │                   │                                                           │ Historically, we have been rather lax about malformed        │
│                        │                │          │        │                   │                                                           │ framing-related ...                                          │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-78660                   │
│                        ├────────────────┤          │        │                   │                                                           ├──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-78669 │          │        │                   │                                                           │ net/http: net/http/internal/http2: golang.org/x/net/http2:   │
│                        │                │          │        │                   │                                                           │ net/http: Denial of Service via excessive HTTP/2 SETTINGS    │
│                        │                │          │        │                   │                                                           │ frames...                                                    │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-78669                   │
├────────────────────────┼────────────────┤          │        ├───────────────────┼───────────────────────────────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ golang.org/x/text      │ CVE-2026-56851 │          │        │ v0.40.0           │ 0.41.0                                                    │ golang.org/x/text: golang.org/x/text: Denial of Service via  │
│                        │                │          │        │                   │                                                           │ out-of-bounds slice error in Nickname profile...             │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-56851                   │
├────────────────────────┼────────────────┼──────────┤        ├───────────────────┼───────────────────────────────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ google.golang.org/grpc │ CVE-2026-84303 │ CRITICAL │        │ v1.82.1           │ 1.83.1                                                    │ gRPC-Go is the Go language implementation of gRPC. Prior to  │
│                        │                │          │        │                   │                                                           │ 1.83.1, th...                                                │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-84303                   │
│                        ├────────────────┼──────────┤        │                   │                                                           ├──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-84304 │ HIGH     │        │                   │                                                           │ google.golang.org/grpc: gRPC-Go: Denial of Service via       │
│                        │                │          │        │                   │                                                           │ HTTP/2 DATA Frame Fragmentation                              │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-84304                   │
│                        ├────────────────┤          │        │                   ├───────────────────────────────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-84445 │          │        │                   │ 1.82.2, 1.83.2, 1.84.0-dev.0.20260825144003-d5a41119e0e3, │ google.golang.org/grpc: gRPC-Go: Denial of Service via       │
│                        │                │          │        │                   │ 1.85.0-dev.0.20260825072537-93e31b48545e                  │ malformed RPC requests                                       │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-84445                   │
├────────────────────────┼────────────────┤          │        ├───────────────────┼───────────────────────────────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ stdlib                 │ CVE-2026-56866 │          │        │ v1.26.6           │ 1.26.9, 1.27.2                                            │ net/http: golang: golang: Cross-user response poisoning via  │
│                        │                │          │        │                   │                                                           │ desynchronized HTTP CONNECT connections                      │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-56866                   │
│                        ├────────────────┤          │        │                   │                                                           ├──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-78659 │          │        │                   │                                                           │ When "Trailer" headers are sent by a client, the HTTP server │
│                        │                │          │        │                   │                                                           │ internall...                                                 │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-78659                   │
│                        ├────────────────┤          │        │                   │                                                           ├──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-78660 │          │        │                   │                                                           │ Historically, we have been rather lax about malformed        │
│                        │                │          │        │                   │                                                           │ framing-related ...                                          │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-78660                   │
│                        ├────────────────┤          │        │                   │                                                           ├──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-78667 │          │        │                   │                                                           │ net/http: golang: golang: Denial of Service via crafted HTTP │
│                        │                │          │        │                   │                                                           │ Range headers                                                │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-78667                   │
│                        ├────────────────┤          │        │                   │                                                           ├──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-78669 │          │        │                   │                                                           │ net/http: net/http/internal/http2: golang.org/x/net/http2:   │
│                        │                │          │        │                   │                                                           │ net/http: Denial of Service via excessive HTTP/2 SETTINGS    │
│                        │                │          │        │                   │                                                           │ frames...                                                    │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-78669                   │
│                        ├────────────────┤          │        │                   │                                                           ├──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-94440 │          │        │                   │                                                           │ Parsing a multipart form can bypass memory limits and read   │
│                        │                │          │        │                   │                                                           │ an arbitrar...                                               │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-94440                   │
│                        ├────────────────┤          │        │                   │                                                           ├──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-97031 │          │        │                   │                                                           │ crypto/tls: golang: crypto/tls: Denial of Service via        │
│                        │                │          │        │                   │                                                           │ multiple ECH outer extension references...                   │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-97031                   │
└────────────────────────┴────────────────┴──────────┴────────┴───────────────────┴───────────────────────────────────────────────────────────┴──────────────────────────────────────────────────────────────┘
```

## Scan Results: `registry.rancher.com/rancher/mirrored-calico-envoy-proxy:v3.32.2`

```text
```

## Scan Results: `registry.rancher.com/rancher/mirrored-calico-envoy-ratelimit:v3.32.2`

```text

bin/ratelimit (gobinary)
========================
Total: 14 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 13, CRITICAL: 1)

┌────────────────────────┬────────────────┬──────────┬────────┬───────────────────┬───────────────────────────────────────────────────────────┬──────────────────────────────────────────────────────────────┐
│        Library         │ Vulnerability  │ Severity │ Status │ Installed Version │                       Fixed Version                       │                            Title                             │
├────────────────────────┼────────────────┼──────────┼────────┼───────────────────┼───────────────────────────────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ golang.org/x/net       │ CVE-2026-78659 │ HIGH     │ fixed  │ v0.56.0           │ 0.60.0                                                    │ When "Trailer" headers are sent by a client, the HTTP server │
│                        │                │          │        │                   │                                                           │ internall...                                                 │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-78659                   │
│                        ├────────────────┤          │        │                   │                                                           ├──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-78660 │          │        │                   │                                                           │ Historically, we have been rather lax about malformed        │
│                        │                │          │        │                   │                                                           │ framing-related ...                                          │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-78660                   │
│                        ├────────────────┤          │        │                   │                                                           ├──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-78669 │          │        │                   │                                                           │ net/http: net/http/internal/http2: golang.org/x/net/http2:   │
│                        │                │          │        │                   │                                                           │ net/http: Denial of Service via excessive HTTP/2 SETTINGS    │
│                        │                │          │        │                   │                                                           │ frames...                                                    │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-78669                   │
├────────────────────────┼────────────────┤          │        ├───────────────────┼───────────────────────────────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ golang.org/x/text      │ CVE-2026-56851 │          │        │ v0.39.0           │ 0.41.0                                                    │ golang.org/x/text: golang.org/x/text: Denial of Service via  │
│                        │                │          │        │                   │                                                           │ out-of-bounds slice error in Nickname profile...             │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-56851                   │
├────────────────────────┼────────────────┼──────────┤        ├───────────────────┼───────────────────────────────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ google.golang.org/grpc │ CVE-2026-84303 │ CRITICAL │        │ v1.82.1           │ 1.83.1                                                    │ gRPC-Go is the Go language implementation of gRPC. Prior to  │
│                        │                │          │        │                   │                                                           │ 1.83.1, th...                                                │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-84303                   │
│                        ├────────────────┼──────────┤        │                   │                                                           ├──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-84304 │ HIGH     │        │                   │                                                           │ google.golang.org/grpc: gRPC-Go: Denial of Service via       │
│                        │                │          │        │                   │                                                           │ HTTP/2 DATA Frame Fragmentation                              │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-84304                   │
│                        ├────────────────┤          │        │                   ├───────────────────────────────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-84445 │          │        │                   │ 1.82.2, 1.83.2, 1.84.0-dev.0.20260825144003-d5a41119e0e3, │ google.golang.org/grpc: gRPC-Go: Denial of Service via       │
│                        │                │          │        │                   │ 1.85.0-dev.0.20260825072537-93e31b48545e                  │ malformed RPC requests                                       │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-84445                   │
├────────────────────────┼────────────────┤          │        ├───────────────────┼───────────────────────────────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ stdlib                 │ CVE-2026-56866 │          │        │ v1.26.6           │ 1.26.9, 1.27.2                                            │ net/http: golang: golang: Cross-user response poisoning via  │
│                        │                │          │        │                   │                                                           │ desynchronized HTTP CONNECT connections                      │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-56866                   │
│                        ├────────────────┤          │        │                   │                                                           ├──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-78659 │          │        │                   │                                                           │ When "Trailer" headers are sent by a client, the HTTP server │
│                        │                │          │        │                   │                                                           │ internall...                                                 │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-78659                   │
│                        ├────────────────┤          │        │                   │                                                           ├──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-78660 │          │        │                   │                                                           │ Historically, we have been rather lax about malformed        │
│                        │                │          │        │                   │                                                           │ framing-related ...                                          │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-78660                   │
│                        ├────────────────┤          │        │                   │                                                           ├──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-78667 │          │        │                   │                                                           │ net/http: golang: golang: Denial of Service via crafted HTTP │
│                        │                │          │        │                   │                                                           │ Range headers                                                │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-78667                   │
│                        ├────────────────┤          │        │                   │                                                           ├──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-78669 │          │        │                   │                                                           │ net/http: net/http/internal/http2: golang.org/x/net/http2:   │
│                        │                │          │        │                   │                                                           │ net/http: Denial of Service via excessive HTTP/2 SETTINGS    │
│                        │                │          │        │                   │                                                           │ frames...                                                    │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-78669                   │
│                        ├────────────────┤          │        │                   │                                                           ├──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-94440 │          │        │                   │                                                           │ Parsing a multipart form can bypass memory limits and read   │
│                        │                │          │        │                   │                                                           │ an arbitrar...                                               │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-94440                   │
│                        ├────────────────┤          │        │                   │                                                           ├──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-97031 │          │        │                   │                                                           │ crypto/tls: golang: crypto/tls: Denial of Service via        │
│                        │                │          │        │                   │                                                           │ multiple ECH outer extension references...                   │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-97031                   │
└────────────────────────┴────────────────┴──────────┴────────┴───────────────────┴───────────────────────────────────────────────────────────┴──────────────────────────────────────────────────────────────┘
```

## Scan Results: `registry.rancher.com/rancher/mirrored-calico-goldmane:v3.32.2`

```text

goldmane (gobinary)
===================
Total: 5 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 5, CRITICAL: 0)

┌────────────────────────┬────────────────┬──────────┬────────┬───────────────────┬───────────────────────────────────────────────────────────┬──────────────────────────────────────────────────────────────┐
│        Library         │ Vulnerability  │ Severity │ Status │ Installed Version │                       Fixed Version                       │                            Title                             │
├────────────────────────┼────────────────┼──────────┼────────┼───────────────────┼───────────────────────────────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ golang.org/x/net       │ CVE-2026-78659 │ HIGH     │ fixed  │ v0.58.0           │ 0.60.0                                                    │ When "Trailer" headers are sent by a client, the HTTP server │
│                        │                │          │        │                   │                                                           │ internall...                                                 │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-78659                   │
│                        ├────────────────┤          │        │                   │                                                           ├──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-78660 │          │        │                   │                                                           │ Historically, we have been rather lax about malformed        │
│                        │                │          │        │                   │                                                           │ framing-related ...                                          │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-78660                   │
│                        ├────────────────┤          │        │                   │                                                           ├──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-78669 │          │        │                   │                                                           │ net/http: net/http/internal/http2: golang.org/x/net/http2:   │
│                        │                │          │        │                   │                                                           │ net/http: Denial of Service via excessive HTTP/2 SETTINGS    │
│                        │                │          │        │                   │                                                           │ frames...                                                    │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-78669                   │
├────────────────────────┼────────────────┤          │        ├───────────────────┼───────────────────────────────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ google.golang.org/grpc │ CVE-2026-84304 │          │        │ v1.82.1           │ 1.83.1                                                    │ google.golang.org/grpc: gRPC-Go: Denial of Service via       │
│                        │                │          │        │                   │                                                           │ HTTP/2 DATA Frame Fragmentation                              │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-84304                   │
│                        ├────────────────┤          │        │                   ├───────────────────────────────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-84445 │          │        │                   │ 1.82.2, 1.83.2, 1.84.0-dev.0.20260825144003-d5a41119e0e3, │ google.golang.org/grpc: gRPC-Go: Denial of Service via       │
│                        │                │          │        │                   │ 1.85.0-dev.0.20260825072537-93e31b48545e                  │ malformed RPC requests                                       │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-84445                   │
└────────────────────────┴────────────────┴──────────┴────────┴───────────────────┴───────────────────────────────────────────────────────────┴──────────────────────────────────────────────────────────────┘

health (gobinary)
=================
Total: 5 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 5, CRITICAL: 0)

┌────────────────────────┬────────────────┬──────────┬────────┬───────────────────┬───────────────────────────────────────────────────────────┬──────────────────────────────────────────────────────────────┐
│        Library         │ Vulnerability  │ Severity │ Status │ Installed Version │                       Fixed Version                       │                            Title                             │
├────────────────────────┼────────────────┼──────────┼────────┼───────────────────┼───────────────────────────────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ golang.org/x/net       │ CVE-2026-78659 │ HIGH     │ fixed  │ v0.58.0           │ 0.60.0                                                    │ When "Trailer" headers are sent by a client, the HTTP server │
│                        │                │          │        │                   │                                                           │ internall...                                                 │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-78659                   │
│                        ├────────────────┤          │        │                   │                                                           ├──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-78660 │          │        │                   │                                                           │ Historically, we have been rather lax about malformed        │
│                        │                │          │        │                   │                                                           │ framing-related ...                                          │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-78660                   │
│                        ├────────────────┤          │        │                   │                                                           ├──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-78669 │          │        │                   │                                                           │ net/http: net/http/internal/http2: golang.org/x/net/http2:   │
│                        │                │          │        │                   │                                                           │ net/http: Denial of Service via excessive HTTP/2 SETTINGS    │
│                        │                │          │        │                   │                                                           │ frames...                                                    │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-78669                   │
├────────────────────────┼────────────────┤          │        ├───────────────────┼───────────────────────────────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ google.golang.org/grpc │ CVE-2026-84304 │          │        │ v1.82.1           │ 1.83.1                                                    │ google.golang.org/grpc: gRPC-Go: Denial of Service via       │
│                        │                │          │        │                   │                                                           │ HTTP/2 DATA Frame Fragmentation                              │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-84304                   │
│                        ├────────────────┤          │        │                   ├───────────────────────────────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-84445 │          │        │                   │ 1.82.2, 1.83.2, 1.84.0-dev.0.20260825144003-d5a41119e0e3, │ google.golang.org/grpc: gRPC-Go: Denial of Service via       │
│                        │                │          │        │                   │ 1.85.0-dev.0.20260825072537-93e31b48545e                  │ malformed RPC requests                                       │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-84445                   │
└────────────────────────┴────────────────┴──────────┴────────┴───────────────────┴───────────────────────────────────────────────────────────┴──────────────────────────────────────────────────────────────┘
```

## Scan Results: `registry.rancher.com/rancher/mirrored-calico-whisker:v3.32.2`

```text
```

## Scan Results: `registry.rancher.com/rancher/mirrored-calico-whisker-backend:v3.32.2`

```text

whisker-backend (gobinary)
==========================
Total: 5 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 5, CRITICAL: 0)

┌────────────────────────┬────────────────┬──────────┬────────┬───────────────────┬───────────────────────────────────────────────────────────┬──────────────────────────────────────────────────────────────┐
│        Library         │ Vulnerability  │ Severity │ Status │ Installed Version │                       Fixed Version                       │                            Title                             │
├────────────────────────┼────────────────┼──────────┼────────┼───────────────────┼───────────────────────────────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ golang.org/x/net       │ CVE-2026-78659 │ HIGH     │ fixed  │ v0.58.0           │ 0.60.0                                                    │ When "Trailer" headers are sent by a client, the HTTP server │
│                        │                │          │        │                   │                                                           │ internall...                                                 │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-78659                   │
│                        ├────────────────┤          │        │                   │                                                           ├──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-78660 │          │        │                   │                                                           │ Historically, we have been rather lax about malformed        │
│                        │                │          │        │                   │                                                           │ framing-related ...                                          │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-78660                   │
│                        ├────────────────┤          │        │                   │                                                           ├──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-78669 │          │        │                   │                                                           │ net/http: net/http/internal/http2: golang.org/x/net/http2:   │
│                        │                │          │        │                   │                                                           │ net/http: Denial of Service via excessive HTTP/2 SETTINGS    │
│                        │                │          │        │                   │                                                           │ frames...                                                    │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-78669                   │
├────────────────────────┼────────────────┤          │        ├───────────────────┼───────────────────────────────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ google.golang.org/grpc │ CVE-2026-84304 │          │        │ v1.82.1           │ 1.83.1                                                    │ google.golang.org/grpc: gRPC-Go: Denial of Service via       │
│                        │                │          │        │                   │                                                           │ HTTP/2 DATA Frame Fragmentation                              │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-84304                   │
│                        ├────────────────┤          │        │                   ├───────────────────────────────────────────────────────────┼──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-84445 │          │        │                   │ 1.82.2, 1.83.2, 1.84.0-dev.0.20260825144003-d5a41119e0e3, │ google.golang.org/grpc: gRPC-Go: Denial of Service via       │
│                        │                │          │        │                   │ 1.85.0-dev.0.20260825072537-93e31b48545e                  │ malformed RPC requests                                       │
│                        │                │          │        │                   │                                                           │ https://avd.aquasec.com/nvd/cve-2026-84445                   │
└────────────────────────┴────────────────┴──────────┴────────┴───────────────────┴───────────────────────────────────────────────────────────┴──────────────────────────────────────────────────────────────┘
```

## Scan Results: `registry.rancher.com/rancher/hardened-cloud-provider-vsphere:v1.36.0-build20261012`

```text

vsphere-cloud-controller-manager (gobinary)
===========================================
Total: 1 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 1, CRITICAL: 0)

┌───────────────────┬────────────────┬──────────┬────────┬───────────────────┬───────────────┬─────────────────────────────────────────────────────────────┐
│      Library      │ Vulnerability  │ Severity │ Status │ Installed Version │ Fixed Version │                            Title                            │
├───────────────────┼────────────────┼──────────┼────────┼───────────────────┼───────────────┼─────────────────────────────────────────────────────────────┤
│ golang.org/x/text │ CVE-2026-56851 │ HIGH     │ fixed  │ v0.39.0           │ 0.41.0        │ golang.org/x/text: golang.org/x/text: Denial of Service via │
│                   │                │          │        │                   │               │ out-of-bounds slice error in Nickname profile...            │
│                   │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-56851                  │
└───────────────────┴────────────────┴──────────┴────────┴───────────────────┴───────────────┴─────────────────────────────────────────────────────────────┘
```

## Scan Results: `registry.rancher.com/rancher/hardened-vsphere-csi-driver:v3.7.3-build20261012`

```text

vsphere-csi (gobinary)
======================
Total: 1 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 1, CRITICAL: 0)

┌───────────────────┬────────────────┬──────────┬────────┬───────────────────┬───────────────┬─────────────────────────────────────────────────────────────┐
│      Library      │ Vulnerability  │ Severity │ Status │ Installed Version │ Fixed Version │                            Title                            │
├───────────────────┼────────────────┼──────────┼────────┼───────────────────┼───────────────┼─────────────────────────────────────────────────────────────┤
│ golang.org/x/text │ CVE-2026-56851 │ HIGH     │ fixed  │ v0.39.0           │ 0.41.0        │ golang.org/x/text: golang.org/x/text: Denial of Service via │
│                   │                │          │        │                   │               │ out-of-bounds slice error in Nickname profile...            │
│                   │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-56851                  │
└───────────────────┴────────────────┴──────────┴────────┴───────────────────┴───────────────┴─────────────────────────────────────────────────────────────┘
```

## Scan Results: `registry.rancher.com/rancher/hardened-vsphere-csi-syncer:v3.7.3-build20261012`

```text

syncer (gobinary)
=================
Total: 1 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 1, CRITICAL: 0)

┌───────────────────┬────────────────┬──────────┬────────┬───────────────────┬───────────────┬─────────────────────────────────────────────────────────────┐
│      Library      │ Vulnerability  │ Severity │ Status │ Installed Version │ Fixed Version │                            Title                            │
├───────────────────┼────────────────┼──────────┼────────┼───────────────────┼───────────────┼─────────────────────────────────────────────────────────────┤
│ golang.org/x/text │ CVE-2026-56851 │ HIGH     │ fixed  │ v0.39.0           │ 0.41.0        │ golang.org/x/text: golang.org/x/text: Denial of Service via │
│                   │                │          │        │                   │               │ out-of-bounds slice error in Nickname profile...            │
│                   │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-56851                  │
└───────────────────┴────────────────┴──────────┴────────┴───────────────────┴───────────────┴─────────────────────────────────────────────────────────────┘
```

## Scan Results: `registry.rancher.com/rancher/hardened-csi-node-driver-registrar:v2.13.0-build20261012`

```text
```

## Scan Results: `registry.rancher.com/rancher/hardened-csi-resizer:v1.12.0-build20261012`

```text

csi-resizer (gobinary)
======================
Total: 1 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 1, CRITICAL: 0)

┌───────────────────┬────────────────┬──────────┬────────┬───────────────────┬───────────────┬─────────────────────────────────────────────────────────────┐
│      Library      │ Vulnerability  │ Severity │ Status │ Installed Version │ Fixed Version │                            Title                            │
├───────────────────┼────────────────┼──────────┼────────┼───────────────────┼───────────────┼─────────────────────────────────────────────────────────────┤
│ golang.org/x/text │ CVE-2026-56851 │ HIGH     │ fixed  │ v0.39.0           │ 0.41.0        │ golang.org/x/text: golang.org/x/text: Denial of Service via │
│                   │                │          │        │                   │               │ out-of-bounds slice error in Nickname profile...            │
│                   │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-56851                  │
└───────────────────┴────────────────┴──────────┴────────┴───────────────────┴───────────────┴─────────────────────────────────────────────────────────────┘
```

## Scan Results: `registry.rancher.com/rancher/hardened-livenessprobe:v2.15.0-build20261012`

```text
```

## Scan Results: `registry.rancher.com/rancher/hardened-csi-attacher:v4.9.0-build20261012`

```text

csi-attacher (gobinary)
=======================
Total: 1 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 1, CRITICAL: 0)

┌───────────────────┬────────────────┬──────────┬────────┬───────────────────┬───────────────┬─────────────────────────────────────────────────────────────┐
│      Library      │ Vulnerability  │ Severity │ Status │ Installed Version │ Fixed Version │                            Title                            │
├───────────────────┼────────────────┼──────────┼────────┼───────────────────┼───────────────┼─────────────────────────────────────────────────────────────┤
│ golang.org/x/text │ CVE-2026-56851 │ HIGH     │ fixed  │ v0.39.0           │ 0.41.0        │ golang.org/x/text: golang.org/x/text: Denial of Service via │
│                   │                │          │        │                   │               │ out-of-bounds slice error in Nickname profile...            │
│                   │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-56851                  │
└───────────────────┴────────────────┴──────────┴────────┴───────────────────┴───────────────┴─────────────────────────────────────────────────────────────┘
```

## Scan Results: `registry.rancher.com/rancher/hardened-csi-provisioner:v4.0.1-build20261012`

```text

csi-provisioner (gobinary)
==========================
Total: 1 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 1, CRITICAL: 0)

┌───────────────────┬────────────────┬──────────┬────────┬───────────────────┬───────────────┬─────────────────────────────────────────────────────────────┐
│      Library      │ Vulnerability  │ Severity │ Status │ Installed Version │ Fixed Version │                            Title                            │
├───────────────────┼────────────────┼──────────┼────────┼───────────────────┼───────────────┼─────────────────────────────────────────────────────────────┤
│ golang.org/x/text │ CVE-2026-56851 │ HIGH     │ fixed  │ v0.39.0           │ 0.41.0        │ golang.org/x/text: golang.org/x/text: Denial of Service via │
│                   │                │          │        │                   │               │ out-of-bounds slice error in Nickname profile...            │
│                   │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-56851                  │
└───────────────────┴────────────────┴──────────┴────────┴───────────────────┴───────────────┴─────────────────────────────────────────────────────────────┘
```

## Scan Results: `registry.rancher.com/rancher/hardened-csi-snapshotter:v8.6.0-build20261012`

```text

csi-snapshotter (gobinary)
==========================
Total: 1 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 1, CRITICAL: 0)

┌───────────────────┬────────────────┬──────────┬────────┬───────────────────┬───────────────┬─────────────────────────────────────────────────────────────┐
│      Library      │ Vulnerability  │ Severity │ Status │ Installed Version │ Fixed Version │                            Title                            │
├───────────────────┼────────────────┼──────────┼────────┼───────────────────┼───────────────┼─────────────────────────────────────────────────────────────┤
│ golang.org/x/text │ CVE-2026-56851 │ HIGH     │ fixed  │ v0.39.0           │ 0.41.0        │ golang.org/x/text: golang.org/x/text: Denial of Service via │
│                   │                │          │        │                   │               │ out-of-bounds slice error in Nickname profile...            │
│                   │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-56851                  │
└───────────────────┴────────────────┴──────────┴────────┴───────────────────┴───────────────┴─────────────────────────────────────────────────────────────┘
```

## Scan Results: `registry.rancher.com/rancher/hardened-multus-cni:v4.3.1-build20261016`

```text
```

## Scan Results: `registry.rancher.com/rancher/hardened-multus-thick:v4.3.1-build20261016`

```text
```

## Scan Results: `registry.rancher.com/rancher/hardened-multus-dynamic-networks-controller:v0.3.8-build20261012`

```text
```

## Scan Results: `registry.rancher.com/rancher/hardened-cni-plugins:v1.9.1-build20261015`

```text
```

## Scan Results: `registry.rancher.com/rancher/hardened-whereabouts:v0.9.4-build20261016`

```text
```

## Scan Results: `registry.rancher.com/rancher/mirrored-library-busybox:1.36.1`

```text
```

## Scan Results: `registry.rancher.com/rancher/harvester-cloud-provider:v0.2.9`

```text
```

## Scan Results: `registry.rancher.com/rancher/mirrored-kube-vip-kube-vip-iptables:v1.2.4`

```text

kube-vip (gobinary)
===================
Total: 11 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 11, CRITICAL: 0)

┌─────────────────────┬────────────────┬──────────┬────────┬───────────────────┬────────────────┬──────────────────────────────────────────────────────────────┐
│       Library       │ Vulnerability  │ Severity │ Status │ Installed Version │ Fixed Version  │                            Title                             │
├─────────────────────┼────────────────┼──────────┼────────┼───────────────────┼────────────────┼──────────────────────────────────────────────────────────────┤
│ golang.org/x/crypto │ CVE-2026-56855 │ HIGH     │ fixed  │ v0.55.0           │ 0.56.0         │ golang.org/x/crypto/ssh: golang.org/x/crypto/ssh: Denial of  │
│                     │                │          │        │                   │                │ Service via crafted messages                                 │
│                     │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-56855                   │
│                     ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                     │ CVE-2026-78662 │          │        │                   │                │ golang.org/x/crypto/ssh: golang.org/x/crypto/ssh: Denial of  │
│                     │                │          │        │                   │                │ Service via channel request flooding                         │
│                     │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-78662                   │
├─────────────────────┼────────────────┤          │        ├───────────────────┼────────────────┼──────────────────────────────────────────────────────────────┤
│ golang.org/x/net    │ CVE-2026-78659 │          │        │ v0.58.0           │ 0.60.0         │ When "Trailer" headers are sent by a client, the HTTP server │
│                     │                │          │        │                   │                │ internall...                                                 │
│                     │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-78659                   │
│                     ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                     │ CVE-2026-78660 │          │        │                   │                │ Historically, we have been rather lax about malformed        │
│                     │                │          │        │                   │                │ framing-related ...                                          │
│                     │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-78660                   │
│                     ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                     │ CVE-2026-78669 │          │        │                   │                │ net/http: net/http/internal/http2: golang.org/x/net/http2:   │
│                     │                │          │        │                   │                │ net/http: Denial of Service via excessive HTTP/2 SETTINGS    │
│                     │                │          │        │                   │                │ frames...                                                    │
│                     │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-78669                   │
├─────────────────────┼────────────────┤          │        ├───────────────────┼────────────────┼──────────────────────────────────────────────────────────────┤
│ stdlib              │ CVE-2026-56866 │          │        │ v1.27.1           │ 1.26.9, 1.27.2 │ net/http: golang: golang: Cross-user response poisoning via  │
│                     │                │          │        │                   │                │ desynchronized HTTP CONNECT connections                      │
│                     │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-56866                   │
│                     ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                     │ CVE-2026-78659 │          │        │                   │                │ When "Trailer" headers are sent by a client, the HTTP server │
│                     │                │          │        │                   │                │ internall...                                                 │
│                     │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-78659                   │
│                     ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                     │ CVE-2026-78660 │          │        │                   │                │ Historically, we have been rather lax about malformed        │
│                     │                │          │        │                   │                │ framing-related ...                                          │
│                     │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-78660                   │
│                     ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                     │ CVE-2026-78669 │          │        │                   │                │ net/http: net/http/internal/http2: golang.org/x/net/http2:   │
│                     │                │          │        │                   │                │ net/http: Denial of Service via excessive HTTP/2 SETTINGS    │
│                     │                │          │        │                   │                │ frames...                                                    │
│                     │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-78669                   │
│                     ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                     │ CVE-2026-94440 │          │        │                   │                │ Parsing a multipart form can bypass memory limits and read   │
│                     │                │          │        │                   │                │ an arbitrar...                                               │
│                     │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-94440                   │
│                     ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                     │ CVE-2026-97031 │          │        │                   │                │ crypto/tls: golang: crypto/tls: Denial of Service via        │
│                     │                │          │        │                   │                │ multiple ECH outer extension references...                   │
│                     │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-97031                   │
└─────────────────────┴────────────────┴──────────┴────────┴───────────────────┴────────────────┴──────────────────────────────────────────────────────────────┘
```

## Scan Results: `registry.rancher.com/rancher/harvester-csi-driver:v0.2.10`

```text

registry.rancher.com/rancher/harvester-csi-driver:v0.2.10 (sles 16.0)
=====================================================================
Total: 15 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 15, CRITICAL: 0)

┌───────────────┬──────────────────────┬──────────┬────────┬───────────────────┬───────────────────┬────────────────────────────────┐
│    Library    │    Vulnerability     │ Severity │ Status │ Installed Version │   Fixed Version   │             Title              │
├───────────────┼──────────────────────┼──────────┼────────┼───────────────────┼───────────────────┼────────────────────────────────┤
│ glibc         │ SUSE-SU-2026:23934-1 │ HIGH     │ fixed  │ 2.40-160000.6.1   │ 2.40-160000.7.1   │ Security update for glibc      │
├───────────────┼──────────────────────┤          │        ├───────────────────┼───────────────────┼────────────────────────────────┤
│ libblkid1     │ SUSE-SU-2026:23861-1 │          │        │ 2.41.1-160000.4.1 │ 2.41.1-160000.5.1 │ Security update for util-linux │
│               ├──────────────────────┤          │        │                   │                   │                                │
│               │ SUSE-SU-2026:23870-1 │          │        │                   │                   │                                │
├───────────────┼──────────────────────┤          │        │                   │                   │                                │
│ libfdisk1     │ SUSE-SU-2026:23861-1 │          │        │                   │                   │                                │
│               ├──────────────────────┤          │        │                   │                   │                                │
│               │ SUSE-SU-2026:23870-1 │          │        │                   │                   │                                │
├───────────────┼──────────────────────┤          │        │                   │                   │                                │
│ libmount1     │ SUSE-SU-2026:23861-1 │          │        │                   │                   │                                │
│               ├──────────────────────┤          │        │                   │                   │                                │
│               │ SUSE-SU-2026:23870-1 │          │        │                   │                   │                                │
├───────────────┼──────────────────────┤          │        │                   │                   │                                │
│ libsmartcols1 │ SUSE-SU-2026:23861-1 │          │        │                   │                   │                                │
│               ├──────────────────────┤          │        │                   │                   │                                │
│               │ SUSE-SU-2026:23870-1 │          │        │                   │                   │                                │
├───────────────┼──────────────────────┤          │        │                   │                   │                                │
│ libuuid1      │ SUSE-SU-2026:23861-1 │          │        │                   │                   │                                │
│               ├──────────────────────┤          │        │                   │                   │                                │
│               │ SUSE-SU-2026:23870-1 │          │        │                   │                   │                                │
├───────────────┼──────────────────────┤          │        ├───────────────────┼───────────────────┼────────────────────────────────┤
│ rpcbind       │ SUSE-SU-2026:23946-1 │          │        │ 1.2.9-160000.2.1  │ 1.2.9-160000.3.1  │ Security update for rpcbind    │
├───────────────┼──────────────────────┤          │        ├───────────────────┼───────────────────┼────────────────────────────────┤
│ rpm           │ SUSE-SU-2026:23787-1 │          │        │ 4.20.1-160000.2.2 │ 4.20.1-160000.3.1 │ Security update for rpm        │
├───────────────┼──────────────────────┤          │        ├───────────────────┼───────────────────┼────────────────────────────────┤
│ util-linux    │ SUSE-SU-2026:23861-1 │          │        │ 2.41.1-160000.4.1 │ 2.41.1-160000.5.1 │ Security update for util-linux │
│               ├──────────────────────┤          │        │                   │                   │                                │
│               │ SUSE-SU-2026:23870-1 │          │        │                   │                   │                                │
└───────────────┴──────────────────────┴──────────┴────────┴───────────────────┴───────────────────┴────────────────────────────────┘

usr/bin/harvester-csi-driver (gobinary)
=======================================
Total: 9 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 9, CRITICAL: 0)

┌──────────────────┬────────────────┬──────────┬────────┬───────────────────┬────────────────┬──────────────────────────────────────────────────────────────┐
│     Library      │ Vulnerability  │ Severity │ Status │ Installed Version │ Fixed Version  │                            Title                             │
├──────────────────┼────────────────┼──────────┼────────┼───────────────────┼────────────────┼──────────────────────────────────────────────────────────────┤
│ golang.org/x/net │ CVE-2026-78659 │ HIGH     │ fixed  │ v0.58.0           │ 0.60.0         │ When "Trailer" headers are sent by a client, the HTTP server │
│                  │                │          │        │                   │                │ internall...                                                 │
│                  │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-78659                   │
│                  ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                  │ CVE-2026-78660 │          │        │                   │                │ Historically, we have been rather lax about malformed        │
│                  │                │          │        │                   │                │ framing-related ...                                          │
│                  │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-78660                   │
│                  ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                  │ CVE-2026-78669 │          │        │                   │                │ net/http: net/http/internal/http2: golang.org/x/net/http2:   │
│                  │                │          │        │                   │                │ net/http: Denial of Service via excessive HTTP/2 SETTINGS    │
│                  │                │          │        │                   │                │ frames...                                                    │
│                  │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-78669                   │
├──────────────────┼────────────────┤          │        ├───────────────────┼────────────────┼──────────────────────────────────────────────────────────────┤
│ stdlib           │ CVE-2026-56866 │          │        │ v1.26.8           │ 1.26.9, 1.27.2 │ net/http: golang: golang: Cross-user response poisoning via  │
│                  │                │          │        │                   │                │ desynchronized HTTP CONNECT connections                      │
│                  │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-56866                   │
│                  ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                  │ CVE-2026-78659 │          │        │                   │                │ When "Trailer" headers are sent by a client, the HTTP server │
│                  │                │          │        │                   │                │ internall...                                                 │
│                  │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-78659                   │
│                  ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                  │ CVE-2026-78660 │          │        │                   │                │ Historically, we have been rather lax about malformed        │
│                  │                │          │        │                   │                │ framing-related ...                                          │
│                  │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-78660                   │
│                  ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                  │ CVE-2026-78669 │          │        │                   │                │ net/http: net/http/internal/http2: golang.org/x/net/http2:   │
│                  │                │          │        │                   │                │ net/http: Denial of Service via excessive HTTP/2 SETTINGS    │
│                  │                │          │        │                   │                │ frames...                                                    │
│                  │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-78669                   │
│                  ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                  │ CVE-2026-94440 │          │        │                   │                │ Parsing a multipart form can bypass memory limits and read   │
│                  │                │          │        │                   │                │ an arbitrar...                                               │
│                  │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-94440                   │
│                  ├────────────────┤          │        │                   │                ├──────────────────────────────────────────────────────────────┤
│                  │ CVE-2026-97031 │          │        │                   │                │ crypto/tls: golang: crypto/tls: Denial of Service via        │
│                  │                │          │        │                   │                │ multiple ECH outer extension references...                   │
│                  │                │          │        │                   │                │ https://avd.aquasec.com/nvd/cve-2026-97031                   │
└──────────────────┴────────────────┴──────────┴────────┴───────────────────┴────────────────┴──────────────────────────────────────────────────────────────┘
```

## Scan Results: `registry.rancher.com/rancher/mirrored-longhornio-csi-node-driver-registrar:v2.16.0-20260428`

```text

csi-node-driver-registrar (gobinary)
====================================
Total: 18 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 18, CRITICAL: 0)

┌──────────────────────────┬─────────────────────┬──────────┬────────┬───────────────────┬──────────────────────────────┬──────────────────────────────────────────────────────────────┐
│         Library          │    Vulnerability    │ Severity │ Status │ Installed Version │        Fixed Version         │                            Title                             │
├──────────────────────────┼─────────────────────┼──────────┼────────┼───────────────────┼──────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ go.opentelemetry.io/otel │ CVE-2026-29181      │ HIGH     │ fixed  │ v1.40.0           │ 1.41.0                       │ github.com/open-telemetry/opentelemetry-go:                  │
│                          │                     │          │        │                   │                              │ OpenTelemetry-Go: Denial of Service via crafted multi-value  │
│                          │                     │          │        │                   │                              │ baggage headers                                              │
│                          │                     │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-29181                   │
├──────────────────────────┼─────────────────────┤          │        ├───────────────────┼──────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ golang.org/x/net         │ CVE-2026-78659      │          │        │ v0.49.0           │ 0.60.0                       │ When "Trailer" headers are sent by a client, the HTTP server │
│                          │                     │          │        │                   │                              │ internall...                                                 │
│                          │                     │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-78659                   │
│                          ├─────────────────────┤          │        │                   │                              ├──────────────────────────────────────────────────────────────┤
│                          │ CVE-2026-78660      │          │        │                   │                              │ Historically, we have been rather lax about malformed        │
│                          │                     │          │        │                   │                              │ framing-related ...                                          │
│                          │                     │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-78660                   │
│                          ├─────────────────────┤          │        │                   │                              ├──────────────────────────────────────────────────────────────┤
│                          │ CVE-2026-78669      │          │        │                   │                              │ net/http: net/http/internal/http2: golang.org/x/net/http2:   │
│                          │                     │          │        │                   │                              │ net/http: Denial of Service via excessive HTTP/2 SETTINGS    │
│                          │                     │          │        │                   │                              │ frames...                                                    │
│                          │                     │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-78669                   │
├──────────────────────────┼─────────────────────┤          │        ├───────────────────┼──────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ google.golang.org/grpc   │ CVE-2026-84304      │          │        │ v1.79.3           │ 1.83.1                       │ google.golang.org/grpc: gRPC-Go: Denial of Service via       │
│                          │                     │          │        │                   │                              │ HTTP/2 DATA Frame Fragmentation                              │
│                          │                     │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-84304                   │
│                          ├─────────────────────┤          │        │                   ├──────────────────────────────┼──────────────────────────────────────────────────────────────┤
│                          │ GHSA-hrxh-6v49-42gf │          │        │                   │ 1.82.1                       │ gRPC-Go: xDS RBAC and HTTP/2 Vulnerabilities                 │
│                          │                     │          │        │                   │                              │ https://github.com/advisories/GHSA-hrxh-6v49-42gf            │
├──────────────────────────┼─────────────────────┤          │        ├───────────────────┼──────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ stdlib                   │ CVE-2026-33814      │          │        │ v1.25.9           │ 1.25.10, 1.26.3              │ net/http/internal/http2: golang: golang.org/x/net: Go        │
│                          │                     │          │        │                   │                              │ HTTP/2: Denial of Service via malformed                      │
│                          │                     │          │        │                   │                              │ SETTINGS_MAX_FRAME_SIZE frame...                             │
│                          │                     │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-33814                   │
│                          ├─────────────────────┤          │        │                   ├──────────────────────────────┼──────────────────────────────────────────────────────────────┤
│                          │ CVE-2026-33818      │          │        │                   │ 1.25.13, 1.26.6, 1.27.0-rc.3 │ encoding/asn1: golang: Go encoding/asn1: Denial of Service   │
│                          │                     │          │        │                   │                              │ via excessive recursion in Unmarshal...                      │
│                          │                     │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-33818                   │
│                          ├─────────────────────┤          │        │                   │                              ├──────────────────────────────────────────────────────────────┤
│                          │ CVE-2026-39821      │          │        │                   │                              │ golang.org/x/net/idna: golang: net/http:                     │
│                          │                     │          │        │                   │                              │ golang.org/x/net/idna: Privilege escalation via incorrect    │
│                          │                     │          │        │                   │                              │ Punycode label processing                                    │
│                          │                     │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-39821                   │
│                          ├─────────────────────┤          │        │                   ├──────────────────────────────┼──────────────────────────────────────────────────────────────┤
│                          │ CVE-2026-39836      │          │        │                   │ 1.25.10, 1.26.3              │ net: golang: Go net package: Denial of Service via NUL byte  │
│                          │                     │          │        │                   │                              │ in...                                                        │
│                          │                     │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-39836                   │
│                          ├─────────────────────┤          │        │                   ├──────────────────────────────┼──────────────────────────────────────────────────────────────┤
│                          │ CVE-2026-56853      │          │        │                   │ 1.25.13, 1.26.6, 1.27.0-rc.3 │ net/http: golang: Go net/http: Unencrypted HTTP/2            │
│                          │                     │          │        │                   │                              │ connections vulnerable to Denial of Service...               │
│                          │                     │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-56853                   │
│                          ├─────────────────────┤          │        │                   │                              ├──────────────────────────────────────────────────────────────┤
│                          │ CVE-2026-56862      │          │        │                   │                              │ crypto/tls: golang: Golang crypto/tls: Denial of Service via │
│                          │                     │          │        │                   │                              │ indefinite KeyUpdate messages                                │
│                          │                     │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-56862                   │
│                          ├─────────────────────┤          │        │                   ├──────────────────────────────┼──────────────────────────────────────────────────────────────┤
│                          │ CVE-2026-56866      │          │        │                   │ 1.26.9, 1.27.2               │ net/http: golang: golang: Cross-user response poisoning via  │
│                          │                     │          │        │                   │                              │ desynchronized HTTP CONNECT connections                      │
│                          │                     │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-56866                   │
│                          ├─────────────────────┤          │        │                   │                              ├──────────────────────────────────────────────────────────────┤
│                          │ CVE-2026-78659      │          │        │                   │                              │ When "Trailer" headers are sent by a client, the HTTP server │
│                          │                     │          │        │                   │                              │ internall...                                                 │
│                          │                     │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-78659                   │
│                          ├─────────────────────┤          │        │                   │                              ├──────────────────────────────────────────────────────────────┤
│                          │ CVE-2026-78660      │          │        │                   │                              │ Historically, we have been rather lax about malformed        │
│                          │                     │          │        │                   │                              │ framing-related ...                                          │
│                          │                     │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-78660                   │
│                          ├─────────────────────┤          │        │                   │                              ├──────────────────────────────────────────────────────────────┤
│                          │ CVE-2026-78669      │          │        │                   │                              │ net/http: net/http/internal/http2: golang.org/x/net/http2:   │
│                          │                     │          │        │                   │                              │ net/http: Denial of Service via excessive HTTP/2 SETTINGS    │
│                          │                     │          │        │                   │                              │ frames...                                                    │
│                          │                     │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-78669                   │
│                          ├─────────────────────┤          │        │                   │                              ├──────────────────────────────────────────────────────────────┤
│                          │ CVE-2026-94440      │          │        │                   │                              │ Parsing a multipart form can bypass memory limits and read   │
│                          │                     │          │        │                   │                              │ an arbitrar...                                               │
│                          │                     │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-94440                   │
│                          ├─────────────────────┤          │        │                   │                              ├──────────────────────────────────────────────────────────────┤
│                          │ CVE-2026-97031      │          │        │                   │                              │ crypto/tls: golang: crypto/tls: Denial of Service via        │
│                          │                     │          │        │                   │                              │ multiple ECH outer extension references...                   │
│                          │                     │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-97031                   │
└──────────────────────────┴─────────────────────┴──────────┴────────┴───────────────────┴──────────────────────────────┴──────────────────────────────────────────────────────────────┘
```

## Scan Results: `registry.rancher.com/rancher/mirrored-longhornio-csi-resizer:v2.1.0-20260428`

```text

csi-resizer (gobinary)
======================
Total: 20 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 20, CRITICAL: 0)

┌────────────────────────┬─────────────────────┬──────────┬────────┬───────────────────┬──────────────────────────────┬──────────────────────────────────────────────────────────────┐
│        Library         │    Vulnerability    │ Severity │ Status │ Installed Version │        Fixed Version         │                            Title                             │
├────────────────────────┼─────────────────────┼──────────┼────────┼───────────────────┼──────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ golang.org/x/net       │ CVE-2026-33814      │ HIGH     │ fixed  │ v0.48.0           │ 0.53.0                       │ net/http/internal/http2: golang: golang.org/x/net: Go        │
│                        │                     │          │        │                   │                              │ HTTP/2: Denial of Service via malformed                      │
│                        │                     │          │        │                   │                              │ SETTINGS_MAX_FRAME_SIZE frame...                             │
│                        │                     │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-33814                   │
│                        ├─────────────────────┤          │        │                   ├──────────────────────────────┼──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-39821      │          │        │                   │ 0.55.0                       │ golang.org/x/net/idna: golang: net/http:                     │
│                        │                     │          │        │                   │                              │ golang.org/x/net/idna: Privilege escalation via incorrect    │
│                        │                     │          │        │                   │                              │ Punycode label processing                                    │
│                        │                     │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-39821                   │
│                        ├─────────────────────┤          │        │                   ├──────────────────────────────┼──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-78659      │          │        │                   │ 0.60.0                       │ When "Trailer" headers are sent by a client, the HTTP server │
│                        │                     │          │        │                   │                              │ internall...                                                 │
│                        │                     │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-78659                   │
│                        ├─────────────────────┤          │        │                   │                              ├──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-78660      │          │        │                   │                              │ Historically, we have been rather lax about malformed        │
│                        │                     │          │        │                   │                              │ framing-related ...                                          │
│                        │                     │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-78660                   │
│                        ├─────────────────────┤          │        │                   │                              ├──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-78669      │          │        │                   │                              │ net/http: net/http/internal/http2: golang.org/x/net/http2:   │
│                        │                     │          │        │                   │                              │ net/http: Denial of Service via excessive HTTP/2 SETTINGS    │
│                        │                     │          │        │                   │                              │ frames...                                                    │
│                        │                     │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-78669                   │
├────────────────────────┼─────────────────────┤          │        ├───────────────────┼──────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ google.golang.org/grpc │ CVE-2026-84304      │          │        │ v1.79.3           │ 1.83.1                       │ google.golang.org/grpc: gRPC-Go: Denial of Service via       │
│                        │                     │          │        │                   │                              │ HTTP/2 DATA Frame Fragmentation                              │
│                        │                     │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-84304                   │
│                        ├─────────────────────┤          │        │                   ├──────────────────────────────┼──────────────────────────────────────────────────────────────┤
│                        │ GHSA-hrxh-6v49-42gf │          │        │                   │ 1.82.1                       │ gRPC-Go: xDS RBAC and HTTP/2 Vulnerabilities                 │
│                        │                     │          │        │                   │                              │ https://github.com/advisories/GHSA-hrxh-6v49-42gf            │
├────────────────────────┼─────────────────────┤          │        ├───────────────────┼──────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ stdlib                 │ CVE-2026-33814      │          │        │ v1.25.9           │ 1.25.10, 1.26.3              │ net/http/internal/http2: golang: golang.org/x/net: Go        │
│                        │                     │          │        │                   │                              │ HTTP/2: Denial of Service via malformed                      │
│                        │                     │          │        │                   │                              │ SETTINGS_MAX_FRAME_SIZE frame...                             │
│                        │                     │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-33814                   │
│                        ├─────────────────────┤          │        │                   ├──────────────────────────────┼──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-33818      │          │        │                   │ 1.25.13, 1.26.6, 1.27.0-rc.3 │ encoding/asn1: golang: Go encoding/asn1: Denial of Service   │
│                        │                     │          │        │                   │                              │ via excessive recursion in Unmarshal...                      │
│                        │                     │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-33818                   │
│                        ├─────────────────────┤          │        │                   │                              ├──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-39821      │          │        │                   │                              │ golang.org/x/net/idna: golang: net/http:                     │
│                        │                     │          │        │                   │                              │ golang.org/x/net/idna: Privilege escalation via incorrect    │
│                        │                     │          │        │                   │                              │ Punycode label processing                                    │
│                        │                     │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-39821                   │
│                        ├─────────────────────┤          │        │                   ├──────────────────────────────┼──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-42499      │          │        │                   │ 1.25.10, 1.26.3              │ net/mail: golang: net/mail: Denial of Service via            │
│                        │                     │          │        │                   │                              │ pathological email address parsing                           │
│                        │                     │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-42499                   │
│                        ├─────────────────────┤          │        │                   ├──────────────────────────────┼──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-56853      │          │        │                   │ 1.25.13, 1.26.6, 1.27.0-rc.3 │ net/http: golang: Go net/http: Unencrypted HTTP/2            │
│                        │                     │          │        │                   │                              │ connections vulnerable to Denial of Service...               │
│                        │                     │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-56853                   │
│                        ├─────────────────────┤          │        │                   │                              ├──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-56859      │          │        │                   │                              │ encoding/xml: golang: Go: Denial of Service via XML decoding │
│                        │                     │          │        │                   │                              │ recursion depth issue...                                     │
│                        │                     │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-56859                   │
│                        ├─────────────────────┤          │        │                   │                              ├──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-56862      │          │        │                   │                              │ crypto/tls: golang: Golang crypto/tls: Denial of Service via │
│                        │                     │          │        │                   │                              │ indefinite KeyUpdate messages                                │
│                        │                     │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-56862                   │
│                        ├─────────────────────┤          │        │                   ├──────────────────────────────┼──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-56866      │          │        │                   │ 1.26.9, 1.27.2               │ net/http: golang: golang: Cross-user response poisoning via  │
│                        │                     │          │        │                   │                              │ desynchronized HTTP CONNECT connections                      │
│                        │                     │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-56866                   │
│                        ├─────────────────────┤          │        │                   │                              ├──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-78659      │          │        │                   │                              │ When "Trailer" headers are sent by a client, the HTTP server │
│                        │                     │          │        │                   │                              │ internall...                                                 │
│                        │                     │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-78659                   │
│                        ├─────────────────────┤          │        │                   │                              ├──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-78660      │          │        │                   │                              │ Historically, we have been rather lax about malformed        │
│                        │                     │          │        │                   │                              │ framing-related ...                                          │
│                        │                     │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-78660                   │
│                        ├─────────────────────┤          │        │                   │                              ├──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-78669      │          │        │                   │                              │ net/http: net/http/internal/http2: golang.org/x/net/http2:   │
│                        │                     │          │        │                   │                              │ net/http: Denial of Service via excessive HTTP/2 SETTINGS    │
│                        │                     │          │        │                   │                              │ frames...                                                    │
│                        │                     │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-78669                   │
│                        ├─────────────────────┤          │        │                   │                              ├──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-94440      │          │        │                   │                              │ Parsing a multipart form can bypass memory limits and read   │
│                        │                     │          │        │                   │                              │ an arbitrar...                                               │
│                        │                     │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-94440                   │
│                        ├─────────────────────┤          │        │                   │                              ├──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-97031      │          │        │                   │                              │ crypto/tls: golang: crypto/tls: Denial of Service via        │
│                        │                     │          │        │                   │                              │ multiple ECH outer extension references...                   │
│                        │                     │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-97031                   │
└────────────────────────┴─────────────────────┴──────────┴────────┴───────────────────┴──────────────────────────────┴──────────────────────────────────────────────────────────────┘
```

## Scan Results: `registry.rancher.com/rancher/mirrored-longhornio-csi-provisioner:v5.3.0-20260428`

```text

csi-provisioner (gobinary)
==========================
Total: 20 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 20, CRITICAL: 0)

┌──────────────────────────┬─────────────────────┬──────────┬────────┬───────────────────┬──────────────────────────────┬──────────────────────────────────────────────────────────────┐
│         Library          │    Vulnerability    │ Severity │ Status │ Installed Version │        Fixed Version         │                            Title                             │
├──────────────────────────┼─────────────────────┼──────────┼────────┼───────────────────┼──────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ go.opentelemetry.io/otel │ CVE-2026-29181      │ HIGH     │ fixed  │ v1.39.0           │ 1.41.0                       │ github.com/open-telemetry/opentelemetry-go:                  │
│                          │                     │          │        │                   │                              │ OpenTelemetry-Go: Denial of Service via crafted multi-value  │
│                          │                     │          │        │                   │                              │ baggage headers                                              │
│                          │                     │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-29181                   │
├──────────────────────────┼─────────────────────┤          │        ├───────────────────┼──────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ golang.org/x/net         │ CVE-2026-33814      │          │        │ v0.48.0           │ 0.53.0                       │ net/http/internal/http2: golang: golang.org/x/net: Go        │
│                          │                     │          │        │                   │                              │ HTTP/2: Denial of Service via malformed                      │
│                          │                     │          │        │                   │                              │ SETTINGS_MAX_FRAME_SIZE frame...                             │
│                          │                     │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-33814                   │
│                          ├─────────────────────┤          │        │                   ├──────────────────────────────┼──────────────────────────────────────────────────────────────┤
│                          │ CVE-2026-39821      │          │        │                   │ 0.55.0                       │ golang.org/x/net/idna: golang: net/http:                     │
│                          │                     │          │        │                   │                              │ golang.org/x/net/idna: Privilege escalation via incorrect    │
│                          │                     │          │        │                   │                              │ Punycode label processing                                    │
│                          │                     │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-39821                   │
│                          ├─────────────────────┤          │        │                   ├──────────────────────────────┼──────────────────────────────────────────────────────────────┤
│                          │ CVE-2026-78659      │          │        │                   │ 0.60.0                       │ When "Trailer" headers are sent by a client, the HTTP server │
│                          │                     │          │        │                   │                              │ internall...                                                 │
│                          │                     │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-78659                   │
│                          ├─────────────────────┤          │        │                   │                              ├──────────────────────────────────────────────────────────────┤
│                          │ CVE-2026-78660      │          │        │                   │                              │ Historically, we have been rather lax about malformed        │
│                          │                     │          │        │                   │                              │ framing-related ...                                          │
│                          │                     │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-78660                   │
│                          ├─────────────────────┤          │        │                   │                              ├──────────────────────────────────────────────────────────────┤
│                          │ CVE-2026-78669      │          │        │                   │                              │ net/http: net/http/internal/http2: golang.org/x/net/http2:   │
│                          │                     │          │        │                   │                              │ net/http: Denial of Service via excessive HTTP/2 SETTINGS    │
│                          │                     │          │        │                   │                              │ frames...                                                    │
│                          │                     │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-78669                   │
├──────────────────────────┼─────────────────────┤          │        ├───────────────────┼──────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ google.golang.org/grpc   │ CVE-2026-84304      │          │        │ v1.79.3           │ 1.83.1                       │ google.golang.org/grpc: gRPC-Go: Denial of Service via       │
│                          │                     │          │        │                   │                              │ HTTP/2 DATA Frame Fragmentation                              │
│                          │                     │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-84304                   │
│                          ├─────────────────────┤          │        │                   ├──────────────────────────────┼──────────────────────────────────────────────────────────────┤
│                          │ GHSA-hrxh-6v49-42gf │          │        │                   │ 1.82.1                       │ gRPC-Go: xDS RBAC and HTTP/2 Vulnerabilities                 │
│                          │                     │          │        │                   │                              │ https://github.com/advisories/GHSA-hrxh-6v49-42gf            │
├──────────────────────────┼─────────────────────┤          │        ├───────────────────┼──────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ stdlib                   │ CVE-2026-33814      │          │        │ v1.25.9           │ 1.25.10, 1.26.3              │ net/http/internal/http2: golang: golang.org/x/net: Go        │
│                          │                     │          │        │                   │                              │ HTTP/2: Denial of Service via malformed                      │
│                          │                     │          │        │                   │                              │ SETTINGS_MAX_FRAME_SIZE frame...                             │
│                          │                     │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-33814                   │
│                          ├─────────────────────┤          │        │                   ├──────────────────────────────┼──────────────────────────────────────────────────────────────┤
│                          │ CVE-2026-33818      │          │        │                   │ 1.25.13, 1.26.6, 1.27.0-rc.3 │ encoding/asn1: golang: Go encoding/asn1: Denial of Service   │
│                          │                     │          │        │                   │                              │ via excessive recursion in Unmarshal...                      │
│                          │                     │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-33818                   │
│                          ├─────────────────────┤          │        │                   │                              ├──────────────────────────────────────────────────────────────┤
│                          │ CVE-2026-39821      │          │        │                   │                              │ golang.org/x/net/idna: golang: net/http:                     │
│                          │                     │          │        │                   │                              │ golang.org/x/net/idna: Privilege escalation via incorrect    │
│                          │                     │          │        │                   │                              │ Punycode label processing                                    │
│                          │                     │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-39821                   │
│                          ├─────────────────────┤          │        │                   │                              ├──────────────────────────────────────────────────────────────┤
│                          │ CVE-2026-56853      │          │        │                   │                              │ net/http: golang: Go net/http: Unencrypted HTTP/2            │
│                          │                     │          │        │                   │                              │ connections vulnerable to Denial of Service...               │
│                          │                     │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-56853                   │
│                          ├─────────────────────┤          │        │                   │                              ├──────────────────────────────────────────────────────────────┤
│                          │ CVE-2026-56859      │          │        │                   │                              │ encoding/xml: golang: Go: Denial of Service via XML decoding │
│                          │                     │          │        │                   │                              │ recursion depth issue...                                     │
│                          │                     │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-56859                   │
│                          ├─────────────────────┤          │        │                   │                              ├──────────────────────────────────────────────────────────────┤
│                          │ CVE-2026-56862      │          │        │                   │                              │ crypto/tls: golang: Golang crypto/tls: Denial of Service via │
│                          │                     │          │        │                   │                              │ indefinite KeyUpdate messages                                │
│                          │                     │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-56862                   │
│                          ├─────────────────────┤          │        │                   ├──────────────────────────────┼──────────────────────────────────────────────────────────────┤
│                          │ CVE-2026-56866      │          │        │                   │ 1.26.9, 1.27.2               │ net/http: golang: golang: Cross-user response poisoning via  │
│                          │                     │          │        │                   │                              │ desynchronized HTTP CONNECT connections                      │
│                          │                     │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-56866                   │
│                          ├─────────────────────┤          │        │                   │                              ├──────────────────────────────────────────────────────────────┤
│                          │ CVE-2026-78659      │          │        │                   │                              │ When "Trailer" headers are sent by a client, the HTTP server │
│                          │                     │          │        │                   │                              │ internall...                                                 │
│                          │                     │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-78659                   │
│                          ├─────────────────────┤          │        │                   │                              ├──────────────────────────────────────────────────────────────┤
│                          │ CVE-2026-78660      │          │        │                   │                              │ Historically, we have been rather lax about malformed        │
│                          │                     │          │        │                   │                              │ framing-related ...                                          │
│                          │                     │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-78660                   │
│                          ├─────────────────────┤          │        │                   │                              ├──────────────────────────────────────────────────────────────┤
│                          │ CVE-2026-78669      │          │        │                   │                              │ net/http: net/http/internal/http2: golang.org/x/net/http2:   │
│                          │                     │          │        │                   │                              │ net/http: Denial of Service via excessive HTTP/2 SETTINGS    │
│                          │                     │          │        │                   │                              │ frames...                                                    │
│                          │                     │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-78669                   │
│                          ├─────────────────────┤          │        │                   │                              ├──────────────────────────────────────────────────────────────┤
│                          │ CVE-2026-94440      │          │        │                   │                              │ Parsing a multipart form can bypass memory limits and read   │
│                          │                     │          │        │                   │                              │ an arbitrar...                                               │
│                          │                     │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-94440                   │
│                          ├─────────────────────┤          │        │                   │                              ├──────────────────────────────────────────────────────────────┤
│                          │ CVE-2026-97031      │          │        │                   │                              │ crypto/tls: golang: crypto/tls: Denial of Service via        │
│                          │                     │          │        │                   │                              │ multiple ECH outer extension references...                   │
│                          │                     │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-97031                   │
└──────────────────────────┴─────────────────────┴──────────┴────────┴───────────────────┴──────────────────────────────┴──────────────────────────────────────────────────────────────┘
```

## Scan Results: `registry.rancher.com/rancher/mirrored-longhornio-csi-attacher:v4.11.0-20260428`

```text

csi-attacher (gobinary)
=======================
Total: 20 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 20, CRITICAL: 0)

┌────────────────────────┬─────────────────────┬──────────┬────────┬───────────────────┬──────────────────────────────┬──────────────────────────────────────────────────────────────┐
│        Library         │    Vulnerability    │ Severity │ Status │ Installed Version │        Fixed Version         │                            Title                             │
├────────────────────────┼─────────────────────┼──────────┼────────┼───────────────────┼──────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ golang.org/x/net       │ CVE-2026-33814      │ HIGH     │ fixed  │ v0.48.0           │ 0.53.0                       │ net/http/internal/http2: golang: golang.org/x/net: Go        │
│                        │                     │          │        │                   │                              │ HTTP/2: Denial of Service via malformed                      │
│                        │                     │          │        │                   │                              │ SETTINGS_MAX_FRAME_SIZE frame...                             │
│                        │                     │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-33814                   │
│                        ├─────────────────────┤          │        │                   ├──────────────────────────────┼──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-39821      │          │        │                   │ 0.55.0                       │ golang.org/x/net/idna: golang: net/http:                     │
│                        │                     │          │        │                   │                              │ golang.org/x/net/idna: Privilege escalation via incorrect    │
│                        │                     │          │        │                   │                              │ Punycode label processing                                    │
│                        │                     │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-39821                   │
│                        ├─────────────────────┤          │        │                   ├──────────────────────────────┼──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-78659      │          │        │                   │ 0.60.0                       │ When "Trailer" headers are sent by a client, the HTTP server │
│                        │                     │          │        │                   │                              │ internall...                                                 │
│                        │                     │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-78659                   │
│                        ├─────────────────────┤          │        │                   │                              ├──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-78660      │          │        │                   │                              │ Historically, we have been rather lax about malformed        │
│                        │                     │          │        │                   │                              │ framing-related ...                                          │
│                        │                     │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-78660                   │
│                        ├─────────────────────┤          │        │                   │                              ├──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-78669      │          │        │                   │                              │ net/http: net/http/internal/http2: golang.org/x/net/http2:   │
│                        │                     │          │        │                   │                              │ net/http: Denial of Service via excessive HTTP/2 SETTINGS    │
│                        │                     │          │        │                   │                              │ frames...                                                    │
│                        │                     │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-78669                   │
├────────────────────────┼─────────────────────┤          │        ├───────────────────┼──────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ google.golang.org/grpc │ CVE-2026-84304      │          │        │ v1.79.3           │ 1.83.1                       │ google.golang.org/grpc: gRPC-Go: Denial of Service via       │
│                        │                     │          │        │                   │                              │ HTTP/2 DATA Frame Fragmentation                              │
│                        │                     │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-84304                   │
│                        ├─────────────────────┤          │        │                   ├──────────────────────────────┼──────────────────────────────────────────────────────────────┤
│                        │ GHSA-hrxh-6v49-42gf │          │        │                   │ 1.82.1                       │ gRPC-Go: xDS RBAC and HTTP/2 Vulnerabilities                 │
│                        │                     │          │        │                   │                              │ https://github.com/advisories/GHSA-hrxh-6v49-42gf            │
├────────────────────────┼─────────────────────┤          │        ├───────────────────┼──────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ stdlib                 │ CVE-2026-33814      │          │        │ v1.25.9           │ 1.25.10, 1.26.3              │ net/http/internal/http2: golang: golang.org/x/net: Go        │
│                        │                     │          │        │                   │                              │ HTTP/2: Denial of Service via malformed                      │
│                        │                     │          │        │                   │                              │ SETTINGS_MAX_FRAME_SIZE frame...                             │
│                        │                     │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-33814                   │
│                        ├─────────────────────┤          │        │                   ├──────────────────────────────┼──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-33818      │          │        │                   │ 1.25.13, 1.26.6, 1.27.0-rc.3 │ encoding/asn1: golang: Go encoding/asn1: Denial of Service   │
│                        │                     │          │        │                   │                              │ via excessive recursion in Unmarshal...                      │
│                        │                     │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-33818                   │
│                        ├─────────────────────┤          │        │                   │                              ├──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-39821      │          │        │                   │                              │ golang.org/x/net/idna: golang: net/http:                     │
│                        │                     │          │        │                   │                              │ golang.org/x/net/idna: Privilege escalation via incorrect    │
│                        │                     │          │        │                   │                              │ Punycode label processing                                    │
│                        │                     │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-39821                   │
│                        ├─────────────────────┤          │        │                   ├──────────────────────────────┼──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-42499      │          │        │                   │ 1.25.10, 1.26.3              │ net/mail: golang: net/mail: Denial of Service via            │
│                        │                     │          │        │                   │                              │ pathological email address parsing                           │
│                        │                     │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-42499                   │
│                        ├─────────────────────┤          │        │                   ├──────────────────────────────┼──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-56853      │          │        │                   │ 1.25.13, 1.26.6, 1.27.0-rc.3 │ net/http: golang: Go net/http: Unencrypted HTTP/2            │
│                        │                     │          │        │                   │                              │ connections vulnerable to Denial of Service...               │
│                        │                     │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-56853                   │
│                        ├─────────────────────┤          │        │                   │                              ├──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-56859      │          │        │                   │                              │ encoding/xml: golang: Go: Denial of Service via XML decoding │
│                        │                     │          │        │                   │                              │ recursion depth issue...                                     │
│                        │                     │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-56859                   │
│                        ├─────────────────────┤          │        │                   │                              ├──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-56862      │          │        │                   │                              │ crypto/tls: golang: Golang crypto/tls: Denial of Service via │
│                        │                     │          │        │                   │                              │ indefinite KeyUpdate messages                                │
│                        │                     │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-56862                   │
│                        ├─────────────────────┤          │        │                   ├──────────────────────────────┼──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-56866      │          │        │                   │ 1.26.9, 1.27.2               │ net/http: golang: golang: Cross-user response poisoning via  │
│                        │                     │          │        │                   │                              │ desynchronized HTTP CONNECT connections                      │
│                        │                     │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-56866                   │
│                        ├─────────────────────┤          │        │                   │                              ├──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-78659      │          │        │                   │                              │ When "Trailer" headers are sent by a client, the HTTP server │
│                        │                     │          │        │                   │                              │ internall...                                                 │
│                        │                     │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-78659                   │
│                        ├─────────────────────┤          │        │                   │                              ├──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-78660      │          │        │                   │                              │ Historically, we have been rather lax about malformed        │
│                        │                     │          │        │                   │                              │ framing-related ...                                          │
│                        │                     │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-78660                   │
│                        ├─────────────────────┤          │        │                   │                              ├──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-78669      │          │        │                   │                              │ net/http: net/http/internal/http2: golang.org/x/net/http2:   │
│                        │                     │          │        │                   │                              │ net/http: Denial of Service via excessive HTTP/2 SETTINGS    │
│                        │                     │          │        │                   │                              │ frames...                                                    │
│                        │                     │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-78669                   │
│                        ├─────────────────────┤          │        │                   │                              ├──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-94440      │          │        │                   │                              │ Parsing a multipart form can bypass memory limits and read   │
│                        │                     │          │        │                   │                              │ an arbitrar...                                               │
│                        │                     │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-94440                   │
│                        ├─────────────────────┤          │        │                   │                              ├──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-97031      │          │        │                   │                              │ crypto/tls: golang: crypto/tls: Denial of Service via        │
│                        │                     │          │        │                   │                              │ multiple ECH outer extension references...                   │
│                        │                     │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-97031                   │
└────────────────────────┴─────────────────────┴──────────┴────────┴───────────────────┴──────────────────────────────┴──────────────────────────────────────────────────────────────┘
```

## Scan Results: `registry.rancher.com/rancher/mirrored-longhornio-csi-snapshotter:v8.5.0-20260428`

```text

csi-snapshotter (gobinary)
==========================
Total: 20 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 20, CRITICAL: 0)

┌────────────────────────┬─────────────────────┬──────────┬────────┬───────────────────┬──────────────────────────────┬──────────────────────────────────────────────────────────────┐
│        Library         │    Vulnerability    │ Severity │ Status │ Installed Version │        Fixed Version         │                            Title                             │
├────────────────────────┼─────────────────────┼──────────┼────────┼───────────────────┼──────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ golang.org/x/net       │ CVE-2026-33814      │ HIGH     │ fixed  │ v0.49.0           │ 0.53.0                       │ net/http/internal/http2: golang: golang.org/x/net: Go        │
│                        │                     │          │        │                   │                              │ HTTP/2: Denial of Service via malformed                      │
│                        │                     │          │        │                   │                              │ SETTINGS_MAX_FRAME_SIZE frame...                             │
│                        │                     │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-33814                   │
│                        ├─────────────────────┤          │        │                   ├──────────────────────────────┼──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-39821      │          │        │                   │ 0.55.0                       │ golang.org/x/net/idna: golang: net/http:                     │
│                        │                     │          │        │                   │                              │ golang.org/x/net/idna: Privilege escalation via incorrect    │
│                        │                     │          │        │                   │                              │ Punycode label processing                                    │
│                        │                     │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-39821                   │
│                        ├─────────────────────┤          │        │                   ├──────────────────────────────┼──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-78659      │          │        │                   │ 0.60.0                       │ When "Trailer" headers are sent by a client, the HTTP server │
│                        │                     │          │        │                   │                              │ internall...                                                 │
│                        │                     │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-78659                   │
│                        ├─────────────────────┤          │        │                   │                              ├──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-78660      │          │        │                   │                              │ Historically, we have been rather lax about malformed        │
│                        │                     │          │        │                   │                              │ framing-related ...                                          │
│                        │                     │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-78660                   │
│                        ├─────────────────────┤          │        │                   │                              ├──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-78669      │          │        │                   │                              │ net/http: net/http/internal/http2: golang.org/x/net/http2:   │
│                        │                     │          │        │                   │                              │ net/http: Denial of Service via excessive HTTP/2 SETTINGS    │
│                        │                     │          │        │                   │                              │ frames...                                                    │
│                        │                     │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-78669                   │
├────────────────────────┼─────────────────────┤          │        ├───────────────────┼──────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ google.golang.org/grpc │ CVE-2026-84304      │          │        │ v1.79.3           │ 1.83.1                       │ google.golang.org/grpc: gRPC-Go: Denial of Service via       │
│                        │                     │          │        │                   │                              │ HTTP/2 DATA Frame Fragmentation                              │
│                        │                     │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-84304                   │
│                        ├─────────────────────┤          │        │                   ├──────────────────────────────┼──────────────────────────────────────────────────────────────┤
│                        │ GHSA-hrxh-6v49-42gf │          │        │                   │ 1.82.1                       │ gRPC-Go: xDS RBAC and HTTP/2 Vulnerabilities                 │
│                        │                     │          │        │                   │                              │ https://github.com/advisories/GHSA-hrxh-6v49-42gf            │
├────────────────────────┼─────────────────────┤          │        ├───────────────────┼──────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ stdlib                 │ CVE-2026-33818      │          │        │ v1.25.9           │ 1.25.13, 1.26.6, 1.27.0-rc.3 │ encoding/asn1: golang: Go encoding/asn1: Denial of Service   │
│                        │                     │          │        │                   │                              │ via excessive recursion in Unmarshal...                      │
│                        │                     │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-33818                   │
│                        ├─────────────────────┤          │        │                   ├──────────────────────────────┼──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-39820      │          │        │                   │ 1.25.10, 1.26.3              │ net/mail: golang: Go net/mail: Denial of Service via crafted │
│                        │                     │          │        │                   │                              │ email inputs                                                 │
│                        │                     │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-39820                   │
│                        ├─────────────────────┤          │        │                   ├──────────────────────────────┼──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-39821      │          │        │                   │ 1.25.13, 1.26.6, 1.27.0-rc.3 │ golang.org/x/net/idna: golang: net/http:                     │
│                        │                     │          │        │                   │                              │ golang.org/x/net/idna: Privilege escalation via incorrect    │
│                        │                     │          │        │                   │                              │ Punycode label processing                                    │
│                        │                     │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-39821                   │
│                        ├─────────────────────┤          │        │                   ├──────────────────────────────┼──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-42499      │          │        │                   │ 1.25.10, 1.26.3              │ net/mail: golang: net/mail: Denial of Service via            │
│                        │                     │          │        │                   │                              │ pathological email address parsing                           │
│                        │                     │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-42499                   │
│                        ├─────────────────────┤          │        │                   ├──────────────────────────────┼──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-56853      │          │        │                   │ 1.25.13, 1.26.6, 1.27.0-rc.3 │ net/http: golang: Go net/http: Unencrypted HTTP/2            │
│                        │                     │          │        │                   │                              │ connections vulnerable to Denial of Service...               │
│                        │                     │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-56853                   │
│                        ├─────────────────────┤          │        │                   │                              ├──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-56859      │          │        │                   │                              │ encoding/xml: golang: Go: Denial of Service via XML decoding │
│                        │                     │          │        │                   │                              │ recursion depth issue...                                     │
│                        │                     │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-56859                   │
│                        ├─────────────────────┤          │        │                   │                              ├──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-56862      │          │        │                   │                              │ crypto/tls: golang: Golang crypto/tls: Denial of Service via │
│                        │                     │          │        │                   │                              │ indefinite KeyUpdate messages                                │
│                        │                     │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-56862                   │
│                        ├─────────────────────┤          │        │                   ├──────────────────────────────┼──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-56866      │          │        │                   │ 1.26.9, 1.27.2               │ net/http: golang: golang: Cross-user response poisoning via  │
│                        │                     │          │        │                   │                              │ desynchronized HTTP CONNECT connections                      │
│                        │                     │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-56866                   │
│                        ├─────────────────────┤          │        │                   │                              ├──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-78659      │          │        │                   │                              │ When "Trailer" headers are sent by a client, the HTTP server │
│                        │                     │          │        │                   │                              │ internall...                                                 │
│                        │                     │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-78659                   │
│                        ├─────────────────────┤          │        │                   │                              ├──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-78660      │          │        │                   │                              │ Historically, we have been rather lax about malformed        │
│                        │                     │          │        │                   │                              │ framing-related ...                                          │
│                        │                     │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-78660                   │
│                        ├─────────────────────┤          │        │                   │                              ├──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-78669      │          │        │                   │                              │ net/http: net/http/internal/http2: golang.org/x/net/http2:   │
│                        │                     │          │        │                   │                              │ net/http: Denial of Service via excessive HTTP/2 SETTINGS    │
│                        │                     │          │        │                   │                              │ frames...                                                    │
│                        │                     │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-78669                   │
│                        ├─────────────────────┤          │        │                   │                              ├──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-94440      │          │        │                   │                              │ Parsing a multipart form can bypass memory limits and read   │
│                        │                     │          │        │                   │                              │ an arbitrar...                                               │
│                        │                     │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-94440                   │
│                        ├─────────────────────┤          │        │                   │                              ├──────────────────────────────────────────────────────────────┤
│                        │ CVE-2026-97031      │          │        │                   │                              │ crypto/tls: golang: crypto/tls: Denial of Service via        │
│                        │                     │          │        │                   │                              │ multiple ECH outer extension references...                   │
│                        │                     │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-97031                   │
└────────────────────────┴─────────────────────┴──────────┴────────┴───────────────────┴──────────────────────────────┴──────────────────────────────────────────────────────────────┘
```

<!--OPTIONAL-END-->

## Summary

### CVEs by Severity

| Severity | Count |
| --- | ---: |
| CRITICAL | 0 |
| HIGH | 82 |
| **Total** | **82** |

### Images with CVEs (4)

| Image | CRITICAL | HIGH |
| --- | ---: | ---: |
| `registry.rancher.com/rancher/hardened-kubernetes:v1.36.5-rke2r1-build20260923` | 0 | 60 |
| `registry.rancher.com/rancher/hardened-etcd:v3.6.14-k3s3-build20260915` | 0 | 18 |
| `registry.rancher.com/rancher/klipper-helm:v0.13.3-build20261014` | 0 | 3 |
| `registry.rancher.com/rancher/hardened-snapshot-controller:v8.7.0-build20261015` | 0 | 1 |

### CVE-free Images (14)

- `registry.rancher.com/rancher/hardened-calico:v3.32.2-build20261012`
- `registry.rancher.com/rancher/hardened-flannel:v0.28.10-build20261009`
- `registry.rancher.com/rancher/kube-webhook-certgen:v1.15.1-prime16`
- `registry.rancher.com/rancher/nginx-ingress-controller:v1.15.1-prime16`
- `registry.rancher.com/rancher/rke2-runtime:v1.36.5-dev.`
- `registry.rancher.com/rancher/hardened-coredns:v1.14.7-build20261016`
- `registry.rancher.com/rancher/hardened-cluster-autoscaler:v1.11.0-build20261016`
- `registry.rancher.com/rancher/hardened-dns-node-cache:1.27.2-r1-build20261016`
- `registry.rancher.com/rancher/hardened-k8s-metrics-server:v0.9.0-build20261012`
- `registry.rancher.com/rancher/hardened-addon-resizer:1.8.23-build20261012`
- `registry.rancher.com/rancher/klipper-lb:v0.4.17`
- `registry.rancher.com/rancher/rke2-cloud-provider:v1.36.6-0.20261016153003-c2fdd7c56c2c-build20261016`
- `registry.rancher.com/rancher/hardened-traefik:v3.7.15-build20261016`
- `registry.rancher.com/rancher/hardened-cni-plugins:v1.9.1-build20261012`

