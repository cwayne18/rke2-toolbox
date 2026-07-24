# Trivy Scan Report

<!-- scan-source-ref: release:v1.36.3-rc2+rke2r1 -->
<!-- scan-source-desc: release v1.36.3-rc2+rke2r1 -->
## Images Scanned

- `docker.io/rancher/rke2-runtime:v1.36.3-rc2-rke2r1`
- `docker.io/rancher/hardened-kubernetes:v1.36.3-rke2r1-build20260723`
- `docker.io/rancher/hardened-coredns:v1.14.6-build20260722`
- `docker.io/rancher/hardened-cluster-autoscaler:v1.10.3-build20260717`
- `docker.io/rancher/hardened-dns-node-cache:1.26.8-build20260722`
- `docker.io/rancher/hardened-etcd:v3.6.14-k3s1-build20260723`
- `docker.io/rancher/hardened-k8s-metrics-server:v0.9.0-build20260722`
- `docker.io/rancher/hardened-addon-resizer:1.8.23-build20260717`
- `docker.io/rancher/klipper-helm:v0.13.2-build20260716`
- `docker.io/rancher/klipper-lb:v0.4.17`
- `docker.io/rancher/mirrored-pause:3.10.2`
- `docker.io/rancher/rke2-cloud-provider:v1.36.2-0.20260610225606-10b320a3ba51-build20260709`
- `docker.io/rancher/hardened-snapshot-controller:v8.6.0-build20260722`
- `docker.io/rancher/hardened-traefik:v3.7.8-build20260717`
- `docker.io/rancher/hardened-calico:v3.32.1-build20260722`
- `docker.io/rancher/hardened-flannel:v0.28.8-build20260722`

## Scan Results: `docker.io/rancher/rke2-runtime:v1.36.3-rc2-rke2r1`

```text

bin/crictl (gobinary)
=====================
Total: 3 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 3, CRITICAL: 0)

┌──────────────────┬────────────────┬──────────┬────────┬───────────────────┬───────────────┬──────────────────────────────────────────────────────────────┐
│     Library      │ Vulnerability  │ Severity │ Status │ Installed Version │ Fixed Version │                            Title                             │
├──────────────────┼────────────────┼──────────┼────────┼───────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ golang.org/x/net │ CVE-2026-25681 │ HIGH     │ fixed  │ v0.53.0           │ 0.55.0        │ golang.org/x/net/html: golang.org/x/net/html: Arbitrary code │
│                  │                │          │        │                   │               │ execution via Cross-Site Scripting                           │
│                  │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-25681                   │
│                  ├────────────────┤          │        │                   │               ├──────────────────────────────────────────────────────────────┤
│                  │ CVE-2026-27136 │          │        │                   │               │ golang.org/x/net/html: golang: golang.org/x/net/html:        │
│                  │                │          │        │                   │               │ Cross-Site Scripting via HTML parsing bypass                 │
│                  │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-27136                   │
│                  ├────────────────┤          │        │                   │               ├──────────────────────────────────────────────────────────────┤
│                  │ CVE-2026-39821 │          │        │                   │               │ golang.org/x/net/idna: golang: net/http:                     │
│                  │                │          │        │                   │               │ golang.org/x/net/idna: Privilege escalation via incorrect    │
│                  │                │          │        │                   │               │ Punycode label processing                                    │
│                  │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-39821                   │
└──────────────────┴────────────────┴──────────┴────────┴───────────────────┴───────────────┴──────────────────────────────────────────────────────────────┘
```

## Scan Results: `docker.io/rancher/hardened-kubernetes:v1.36.3-rke2r1-build20260723`

```text
```

## Scan Results: `docker.io/rancher/hardened-coredns:v1.14.6-build20260722`

```text
```

## Scan Results: `docker.io/rancher/hardened-cluster-autoscaler:v1.10.3-build20260717`

```text
```

## Scan Results: `docker.io/rancher/hardened-dns-node-cache:1.26.8-build20260722`

```text
```

## Scan Results: `docker.io/rancher/hardened-etcd:v3.6.14-k3s1-build20260723`

```text
```

## Scan Results: `docker.io/rancher/hardened-k8s-metrics-server:v0.9.0-build20260722`

```text
```

## Scan Results: `docker.io/rancher/hardened-addon-resizer:1.8.23-build20260717`

```text
```

## Scan Results: `docker.io/rancher/klipper-helm:v0.13.2-build20260716`

```text
```

## Scan Results: `docker.io/rancher/klipper-lb:v0.4.17`

```text
```

## Scan Results: `docker.io/rancher/mirrored-pause:3.10.2`

```text
```

## Scan Results: `docker.io/rancher/rke2-cloud-provider:v1.36.2-0.20260610225606-10b320a3ba51-build20260709`

```text

usr/local/bin/rke2-cloud-provider (gobinary)
============================================
Total: 1 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 1, CRITICAL: 0)

┌────────────────────────┬─────────────────────┬──────────┬────────┬───────────────────┬───────────────┬───────────────────────────────────────────────────┐
│        Library         │    Vulnerability    │ Severity │ Status │ Installed Version │ Fixed Version │                       Title                       │
├────────────────────────┼─────────────────────┼──────────┼────────┼───────────────────┼───────────────┼───────────────────────────────────────────────────┤
│ google.golang.org/grpc │ GHSA-hrxh-6v49-42gf │ HIGH     │ fixed  │ v1.79.3           │ 1.82.1        │ gRPC-Go: xDS RBAC and HTTP/2 Vulnerabilities      │
│                        │                     │          │        │                   │               │ https://github.com/advisories/GHSA-hrxh-6v49-42gf │
└────────────────────────┴─────────────────────┴──────────┴────────┴───────────────────┴───────────────┴───────────────────────────────────────────────────┘
```

## Scan Results: `docker.io/rancher/hardened-snapshot-controller:v8.6.0-build20260722`

```text
```

## Scan Results: `docker.io/rancher/hardened-traefik:v3.7.8-build20260717`

```text
```

## Scan Results: `docker.io/rancher/hardened-calico:v3.32.1-build20260722`

```text
```

## Scan Results: `docker.io/rancher/hardened-flannel:v0.28.8-build20260722`

```text
```

## Summary

### CVEs by Severity

| Severity | Count |
| --- | ---: |
| CRITICAL | 0 |
| HIGH | 4 |
| **Total** | **4** |

### Images with CVEs (2)

| Image | CRITICAL | HIGH |
| --- | ---: | ---: |
| `docker.io/rancher/rke2-runtime:v1.36.3-rc2-rke2r1` | 0 | 3 |
| `docker.io/rancher/rke2-cloud-provider:v1.36.2-0.20260610225606-10b320a3ba51-build20260709` | 0 | 1 |

### CVE-free Images (14)

- `docker.io/rancher/hardened-kubernetes:v1.36.3-rke2r1-build20260723`
- `docker.io/rancher/hardened-coredns:v1.14.6-build20260722`
- `docker.io/rancher/hardened-cluster-autoscaler:v1.10.3-build20260717`
- `docker.io/rancher/hardened-dns-node-cache:1.26.8-build20260722`
- `docker.io/rancher/hardened-etcd:v3.6.14-k3s1-build20260723`
- `docker.io/rancher/hardened-k8s-metrics-server:v0.9.0-build20260722`
- `docker.io/rancher/hardened-addon-resizer:1.8.23-build20260717`
- `docker.io/rancher/klipper-helm:v0.13.2-build20260716`
- `docker.io/rancher/klipper-lb:v0.4.17`
- `docker.io/rancher/mirrored-pause:3.10.2`
- `docker.io/rancher/hardened-snapshot-controller:v8.6.0-build20260722`
- `docker.io/rancher/hardened-traefik:v3.7.8-build20260717`
- `docker.io/rancher/hardened-calico:v3.32.1-build20260722`
- `docker.io/rancher/hardened-flannel:v0.28.8-build20260722`

