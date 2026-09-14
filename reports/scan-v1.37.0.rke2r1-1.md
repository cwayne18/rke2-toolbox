# Trivy Scan Report

<!-- scan-source-ref: release:v1.37.0+rke2r1 -->
<!-- scan-source-desc: release v1.37.0+rke2r1 -->
<!-- suse-cvss-rescore: enabled -->
> Go binary CVE severities reflect SUSE's CVSS re-scoring where it differs from Trivy.

## Images Scanned

- `docker.io/rancher/rke2-runtime:v1.37.0-rke2r1`
- `docker.io/rancher/hardened-kubernetes:v1.37.0-rke2r1-build20260909`
- `docker.io/rancher/hardened-coredns:v1.14.7-build20260909`
- `docker.io/rancher/hardened-cluster-autoscaler:v1.10.3-build20260819`
- `docker.io/rancher/hardened-dns-node-cache:1.26.8-build20260909`
- `docker.io/rancher/hardened-etcd:v3.7.1-k3s1-build20260910`
- `docker.io/rancher/hardened-k8s-metrics-server:v0.9.0-build20260909`
- `docker.io/rancher/hardened-addon-resizer:1.8.23-build20260909`
- `docker.io/rancher/klipper-helm:v0.13.3-build20260909`
- `docker.io/rancher/klipper-lb:v0.4.17`
- `docker.io/rancher/mirrored-pause:3.10.2`
- `docker.io/rancher/rke2-cloud-provider:v1.35.1-0.20260817230842-2a1e2e8cf41b-build20260910`
- `docker.io/rancher/rke2-security-responder:v0.1.5`
- `docker.io/rancher/hardened-snapshot-controller:v8.6.0-build20260909`
- `docker.io/rancher/hardened-traefik:v3.7.13-build20260910`
- `docker.io/rancher/hardened-calico:v3.32.2-build20260909`
- `docker.io/rancher/hardened-flannel:v0.28.9-build20260909`

## Scan Results: `docker.io/rancher/rke2-runtime:v1.37.0-rke2r1`

```text

bin/containerd (gobinary)
=========================
Total: 2 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 2, CRITICAL: 0)

┌─────────────────────┬────────────────┬──────────┬────────┬───────────────────┬───────────────┬─────────────────────────────────────────────────────────────┐
│       Library       │ Vulnerability  │ Severity │ Status │ Installed Version │ Fixed Version │                            Title                            │
├─────────────────────┼────────────────┼──────────┼────────┼───────────────────┼───────────────┼─────────────────────────────────────────────────────────────┤
│ golang.org/x/crypto │ CVE-2026-56855 │ HIGH     │ fixed  │ v0.55.0           │ 0.56.0        │ golang.org/x/crypto/ssh: golang.org/x/crypto/ssh: Denial of │
│                     │                │          │        │                   │               │ Service via crafted messages                                │
│                     │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-56855                  │
│                     ├────────────────┤          │        │                   │               ├─────────────────────────────────────────────────────────────┤
│                     │ CVE-2026-78662 │          │        │                   │               │ golang.org/x/crypto/ssh: golang.org/x/crypto/ssh: Denial of │
│                     │                │          │        │                   │               │ Service via channel request flooding                        │
│                     │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-78662                  │
└─────────────────────┴────────────────┴──────────┴────────┴───────────────────┴───────────────┴─────────────────────────────────────────────────────────────┘

bin/kubelet (gobinary)
======================
Total: 2 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 2, CRITICAL: 0)

┌─────────────────────┬────────────────┬──────────┬────────┬───────────────────┬───────────────┬─────────────────────────────────────────────────────────────┐
│       Library       │ Vulnerability  │ Severity │ Status │ Installed Version │ Fixed Version │                            Title                            │
├─────────────────────┼────────────────┼──────────┼────────┼───────────────────┼───────────────┼─────────────────────────────────────────────────────────────┤
│ golang.org/x/crypto │ CVE-2026-56855 │ HIGH     │ fixed  │ v0.55.0           │ 0.56.0        │ golang.org/x/crypto/ssh: golang.org/x/crypto/ssh: Denial of │
│                     │                │          │        │                   │               │ Service via crafted messages                                │
│                     │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-56855                  │
│                     ├────────────────┤          │        │                   │               ├─────────────────────────────────────────────────────────────┤
│                     │ CVE-2026-78662 │          │        │                   │               │ golang.org/x/crypto/ssh: golang.org/x/crypto/ssh: Denial of │
│                     │                │          │        │                   │               │ Service via channel request flooding                        │
│                     │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-78662                  │
└─────────────────────┴────────────────┴──────────┴────────┴───────────────────┴───────────────┴─────────────────────────────────────────────────────────────┘
```

## Scan Results: `docker.io/rancher/hardened-kubernetes:v1.37.0-rke2r1-build20260909`

```text

usr/local/bin/kube-apiserver (gobinary)
=======================================
Total: 2 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 2, CRITICAL: 0)

┌─────────────────────┬────────────────┬──────────┬────────┬───────────────────┬───────────────┬─────────────────────────────────────────────────────────────┐
│       Library       │ Vulnerability  │ Severity │ Status │ Installed Version │ Fixed Version │                            Title                            │
├─────────────────────┼────────────────┼──────────┼────────┼───────────────────┼───────────────┼─────────────────────────────────────────────────────────────┤
│ golang.org/x/crypto │ CVE-2026-56855 │ HIGH     │ fixed  │ v0.55.0           │ 0.56.0        │ golang.org/x/crypto/ssh: golang.org/x/crypto/ssh: Denial of │
│                     │                │          │        │                   │               │ Service via crafted messages                                │
│                     │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-56855                  │
│                     ├────────────────┤          │        │                   │               ├─────────────────────────────────────────────────────────────┤
│                     │ CVE-2026-78662 │          │        │                   │               │ golang.org/x/crypto/ssh: golang.org/x/crypto/ssh: Denial of │
│                     │                │          │        │                   │               │ Service via channel request flooding                        │
│                     │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-78662                  │
└─────────────────────┴────────────────┴──────────┴────────┴───────────────────┴───────────────┴─────────────────────────────────────────────────────────────┘

usr/local/bin/kube-controller-manager (gobinary)
================================================
Total: 2 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 2, CRITICAL: 0)

┌─────────────────────┬────────────────┬──────────┬────────┬───────────────────┬───────────────┬─────────────────────────────────────────────────────────────┐
│       Library       │ Vulnerability  │ Severity │ Status │ Installed Version │ Fixed Version │                            Title                            │
├─────────────────────┼────────────────┼──────────┼────────┼───────────────────┼───────────────┼─────────────────────────────────────────────────────────────┤
│ golang.org/x/crypto │ CVE-2026-56855 │ HIGH     │ fixed  │ v0.55.0           │ 0.56.0        │ golang.org/x/crypto/ssh: golang.org/x/crypto/ssh: Denial of │
│                     │                │          │        │                   │               │ Service via crafted messages                                │
│                     │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-56855                  │
│                     ├────────────────┤          │        │                   │               ├─────────────────────────────────────────────────────────────┤
│                     │ CVE-2026-78662 │          │        │                   │               │ golang.org/x/crypto/ssh: golang.org/x/crypto/ssh: Denial of │
│                     │                │          │        │                   │               │ Service via channel request flooding                        │
│                     │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-78662                  │
└─────────────────────┴────────────────┴──────────┴────────┴───────────────────┴───────────────┴─────────────────────────────────────────────────────────────┘

usr/local/bin/kube-proxy (gobinary)
===================================
Total: 2 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 2, CRITICAL: 0)

┌─────────────────────┬────────────────┬──────────┬────────┬───────────────────┬───────────────┬─────────────────────────────────────────────────────────────┐
│       Library       │ Vulnerability  │ Severity │ Status │ Installed Version │ Fixed Version │                            Title                            │
├─────────────────────┼────────────────┼──────────┼────────┼───────────────────┼───────────────┼─────────────────────────────────────────────────────────────┤
│ golang.org/x/crypto │ CVE-2026-56855 │ HIGH     │ fixed  │ v0.55.0           │ 0.56.0        │ golang.org/x/crypto/ssh: golang.org/x/crypto/ssh: Denial of │
│                     │                │          │        │                   │               │ Service via crafted messages                                │
│                     │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-56855                  │
│                     ├────────────────┤          │        │                   │               ├─────────────────────────────────────────────────────────────┤
│                     │ CVE-2026-78662 │          │        │                   │               │ golang.org/x/crypto/ssh: golang.org/x/crypto/ssh: Denial of │
│                     │                │          │        │                   │               │ Service via channel request flooding                        │
│                     │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-78662                  │
└─────────────────────┴────────────────┴──────────┴────────┴───────────────────┴───────────────┴─────────────────────────────────────────────────────────────┘

usr/local/bin/kube-scheduler (gobinary)
=======================================
Total: 2 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 2, CRITICAL: 0)

┌─────────────────────┬────────────────┬──────────┬────────┬───────────────────┬───────────────┬─────────────────────────────────────────────────────────────┐
│       Library       │ Vulnerability  │ Severity │ Status │ Installed Version │ Fixed Version │                            Title                            │
├─────────────────────┼────────────────┼──────────┼────────┼───────────────────┼───────────────┼─────────────────────────────────────────────────────────────┤
│ golang.org/x/crypto │ CVE-2026-56855 │ HIGH     │ fixed  │ v0.55.0           │ 0.56.0        │ golang.org/x/crypto/ssh: golang.org/x/crypto/ssh: Denial of │
│                     │                │          │        │                   │               │ Service via crafted messages                                │
│                     │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-56855                  │
│                     ├────────────────┤          │        │                   │               ├─────────────────────────────────────────────────────────────┤
│                     │ CVE-2026-78662 │          │        │                   │               │ golang.org/x/crypto/ssh: golang.org/x/crypto/ssh: Denial of │
│                     │                │          │        │                   │               │ Service via channel request flooding                        │
│                     │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-78662                  │
└─────────────────────┴────────────────┴──────────┴────────┴───────────────────┴───────────────┴─────────────────────────────────────────────────────────────┘

usr/local/bin/kubelet (gobinary)
================================
Total: 2 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 2, CRITICAL: 0)

┌─────────────────────┬────────────────┬──────────┬────────┬───────────────────┬───────────────┬─────────────────────────────────────────────────────────────┐
│       Library       │ Vulnerability  │ Severity │ Status │ Installed Version │ Fixed Version │                            Title                            │
├─────────────────────┼────────────────┼──────────┼────────┼───────────────────┼───────────────┼─────────────────────────────────────────────────────────────┤
│ golang.org/x/crypto │ CVE-2026-56855 │ HIGH     │ fixed  │ v0.55.0           │ 0.56.0        │ golang.org/x/crypto/ssh: golang.org/x/crypto/ssh: Denial of │
│                     │                │          │        │                   │               │ Service via crafted messages                                │
│                     │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-56855                  │
│                     ├────────────────┤          │        │                   │               ├─────────────────────────────────────────────────────────────┤
│                     │ CVE-2026-78662 │          │        │                   │               │ golang.org/x/crypto/ssh: golang.org/x/crypto/ssh: Denial of │
│                     │                │          │        │                   │               │ Service via channel request flooding                        │
│                     │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-78662                  │
└─────────────────────┴────────────────┴──────────┴────────┴───────────────────┴───────────────┴─────────────────────────────────────────────────────────────┘
```

## Scan Results: `docker.io/rancher/hardened-coredns:v1.14.7-build20260909`

```text
```

## Scan Results: `docker.io/rancher/hardened-cluster-autoscaler:v1.10.3-build20260819`

```text
```

## Scan Results: `docker.io/rancher/hardened-dns-node-cache:1.26.8-build20260909`

```text
```

## Scan Results: `docker.io/rancher/hardened-etcd:v3.7.1-k3s1-build20260910`

```text
```

## Scan Results: `docker.io/rancher/hardened-k8s-metrics-server:v0.9.0-build20260909`

```text
```

## Scan Results: `docker.io/rancher/hardened-addon-resizer:1.8.23-build20260909`

```text
```

## Scan Results: `docker.io/rancher/klipper-helm:v0.13.3-build20260909`

```text
```

## Scan Results: `docker.io/rancher/klipper-lb:v0.4.17`

```text
```

## Scan Results: `docker.io/rancher/mirrored-pause:3.10.2`

```text
```

## Scan Results: `docker.io/rancher/rke2-cloud-provider:v1.35.1-0.20260817230842-2a1e2e8cf41b-build20260910`

```text
```

## Scan Results: `docker.io/rancher/rke2-security-responder:v0.1.5`

```text
```

## Scan Results: `docker.io/rancher/hardened-snapshot-controller:v8.6.0-build20260909`

```text
```

## Scan Results: `docker.io/rancher/hardened-traefik:v3.7.13-build20260910`

```text
```

## Scan Results: `docker.io/rancher/hardened-calico:v3.32.2-build20260909`

```text
```

## Scan Results: `docker.io/rancher/hardened-flannel:v0.28.9-build20260909`

```text
```

## Summary

### CVEs by Severity

| Severity | Count |
| --- | ---: |
| CRITICAL | 0 |
| HIGH | 14 |
| **Total** | **14** |

### Images with CVEs (2)

| Image | CRITICAL | HIGH |
| --- | ---: | ---: |
| `docker.io/rancher/rke2-runtime:v1.37.0-rke2r1` | 0 | 4 |
| `docker.io/rancher/hardened-kubernetes:v1.37.0-rke2r1-build20260909` | 0 | 10 |

### CVE-free Images (15)

- `docker.io/rancher/hardened-coredns:v1.14.7-build20260909`
- `docker.io/rancher/hardened-cluster-autoscaler:v1.10.3-build20260819`
- `docker.io/rancher/hardened-dns-node-cache:1.26.8-build20260909`
- `docker.io/rancher/hardened-etcd:v3.7.1-k3s1-build20260910`
- `docker.io/rancher/hardened-k8s-metrics-server:v0.9.0-build20260909`
- `docker.io/rancher/hardened-addon-resizer:1.8.23-build20260909`
- `docker.io/rancher/klipper-helm:v0.13.3-build20260909`
- `docker.io/rancher/klipper-lb:v0.4.17`
- `docker.io/rancher/mirrored-pause:3.10.2`
- `docker.io/rancher/rke2-cloud-provider:v1.35.1-0.20260817230842-2a1e2e8cf41b-build20260910`
- `docker.io/rancher/rke2-security-responder:v0.1.5`
- `docker.io/rancher/hardened-snapshot-controller:v8.6.0-build20260909`
- `docker.io/rancher/hardened-traefik:v3.7.13-build20260910`
- `docker.io/rancher/hardened-calico:v3.32.2-build20260909`
- `docker.io/rancher/hardened-flannel:v0.28.9-build20260909`

