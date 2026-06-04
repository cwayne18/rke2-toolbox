# Trivy Scan Report

## Images Scanned

- `docker.io/rancher/rke2-runtime:v1.36.1-rke2r2`
- `docker.io/rancher/hardened-kubernetes:v1.36.1-rke2r2-build20260521`
- `docker.io/rancher/hardened-coredns:v1.14.3-build20260511`
- `docker.io/rancher/hardened-cluster-autoscaler:v1.10.3-build20260511`
- `docker.io/rancher/hardened-dns-node-cache:1.26.8-build20260511`
- `docker.io/rancher/hardened-etcd:v3.6.7-k3s1-build20260512`
- `docker.io/rancher/hardened-k8s-metrics-server:v0.8.1-build20260513`
- `docker.io/rancher/hardened-addon-resizer:1.8.23-build20260511`
- `docker.io/rancher/klipper-helm:v0.10.0-build20260513`
- `docker.io/rancher/klipper-lb:v0.4.17`
- `docker.io/rancher/mirrored-pause:3.6`
- `docker.io/rancher/rke2-cloud-provider:v1.36.1-0.20260508014929-7bbbf7c9b258-build20260515`
- `docker.io/rancher/hardened-snapshot-controller:v8.5.0-build20260513`
- `docker.io/rancher/hardened-traefik:v3.6.16-build20260512`
- `docker.io/rancher/hardened-calico:v3.32.0-build20260511`
- `docker.io/rancher/hardened-flannel:v0.28.4-build20260511`

## Scan Results: `docker.io/rancher/rke2-runtime:v1.36.1-rke2r2`

```text

bin/containerd (gobinary)
=========================
Total: 1 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 1, CRITICAL: 0)

┌─────────────────────────────────────┬────────────────┬──────────┬────────┬───────────────────┬─────────────────────┬────────────────────────────────────────────────────────┐
│               Library               │ Vulnerability  │ Severity │ Status │ Installed Version │    Fixed Version    │                         Title                          │
├─────────────────────────────────────┼────────────────┼──────────┼────────┼───────────────────┼─────────────────────┼────────────────────────────────────────────────────────┤
│ github.com/containerd/containerd/v2 │ CVE-2026-46680 │ HIGH     │ fixed  │ v2.2.3-k3s1       │ 2.0.9, 2.2.4, 2.3.1 │ containerd user ID handling bypass allows runAsNonRoot │
│                                     │                │          │        │                   │                     │ evasion                                                │
│                                     │                │          │        │                   │                     │ https://avd.aquasec.com/nvd/cve-2026-46680             │
└─────────────────────────────────────┴────────────────┴──────────┴────────┴───────────────────┴─────────────────────┴────────────────────────────────────────────────────────┘

bin/containerd-shim-runc-v2 (gobinary)
======================================
Total: 1 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 1, CRITICAL: 0)

┌─────────────────────────────────────┬────────────────┬──────────┬────────┬───────────────────┬─────────────────────┬────────────────────────────────────────────────────────┐
│               Library               │ Vulnerability  │ Severity │ Status │ Installed Version │    Fixed Version    │                         Title                          │
├─────────────────────────────────────┼────────────────┼──────────┼────────┼───────────────────┼─────────────────────┼────────────────────────────────────────────────────────┤
│ github.com/containerd/containerd/v2 │ CVE-2026-46680 │ HIGH     │ fixed  │ v2.2.3-k3s1       │ 2.0.9, 2.2.4, 2.3.1 │ containerd user ID handling bypass allows runAsNonRoot │
│                                     │                │          │        │                   │                     │ evasion                                                │
│                                     │                │          │        │                   │                     │ https://avd.aquasec.com/nvd/cve-2026-46680             │
└─────────────────────────────────────┴────────────────┴──────────┴────────┴───────────────────┴─────────────────────┴────────────────────────────────────────────────────────┘

bin/ctr (gobinary)
==================
Total: 1 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 1, CRITICAL: 0)

┌─────────────────────────────────────┬────────────────┬──────────┬────────┬───────────────────┬─────────────────────┬────────────────────────────────────────────────────────┐
│               Library               │ Vulnerability  │ Severity │ Status │ Installed Version │    Fixed Version    │                         Title                          │
├─────────────────────────────────────┼────────────────┼──────────┼────────┼───────────────────┼─────────────────────┼────────────────────────────────────────────────────────┤
│ github.com/containerd/containerd/v2 │ CVE-2026-46680 │ HIGH     │ fixed  │ v2.2.3-k3s1       │ 2.0.9, 2.2.4, 2.3.1 │ containerd user ID handling bypass allows runAsNonRoot │
│                                     │                │          │        │                   │                     │ evasion                                                │
│                                     │                │          │        │                   │                     │ https://avd.aquasec.com/nvd/cve-2026-46680             │
└─────────────────────────────────────┴────────────────┴──────────┴────────┴───────────────────┴─────────────────────┴────────────────────────────────────────────────────────┘
```

## Scan Results: `docker.io/rancher/hardened-kubernetes:v1.36.1-rke2r2-build20260521`

```text

docker.io/rancher/hardened-kubernetes:v1.36.1-rke2r2-build20260521 (sles 16.0)
==============================================================================
Total: 4 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 4, CRITICAL: 0)

┌───────────────────┬──────────────────────┬──────────┬────────┬───────────────────┬──────────────────┬───────────────────────────┐
│      Library      │    Vulnerability     │ Severity │ Status │ Installed Version │  Fixed Version   │           Title           │
├───────────────────┼──────────────────────┼──────────┼────────┼───────────────────┼──────────────────┼───────────────────────────┤
│ glibc             │ SUSE-SU-2026:21807-1 │ HIGH     │ fixed  │ 2.40-160000.4.1   │ 2.40-160000.5.1  │ Security update for glibc │
├───────────────────┤                      │          │        │                   │                  │                           │
│ glibc-locale-base │                      │          │        │                   │                  │                           │
├───────────────────┼──────────────────────┤          │        ├───────────────────┼──────────────────┼───────────────────────────┤
│ liblzma5          │ SUSE-SU-2026:21848-1 │          │        │ 5.8.1-160000.2.2  │ 5.8.1-160000.3.1 │ Security update for xz    │
├───────────────────┤                      │          │        │                   │                  │                           │
│ xz                │                      │          │        │                   │                  │                           │
└───────────────────┴──────────────────────┴──────────┴────────┴───────────────────┴──────────────────┴───────────────────────────┘
```

## Scan Results: `docker.io/rancher/hardened-coredns:v1.14.3-build20260511`

```text
```

## Scan Results: `docker.io/rancher/hardened-cluster-autoscaler:v1.10.3-build20260511`

```text
```

## Scan Results: `docker.io/rancher/hardened-dns-node-cache:1.26.8-build20260511`

```text
```

## Scan Results: `docker.io/rancher/hardened-etcd:v3.6.7-k3s1-build20260512`

```text
```

## Scan Results: `docker.io/rancher/hardened-k8s-metrics-server:v0.8.1-build20260513`

```text
```

## Scan Results: `docker.io/rancher/hardened-addon-resizer:1.8.23-build20260511`

```text
```

## Scan Results: `docker.io/rancher/klipper-helm:v0.10.0-build20260513`

```text

home/klipper-helm/.local/share/helm/plugins/helm-mapkubeapis/bin/mapkubeapis (gobinary)
=======================================================================================
Total: 1 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 1, CRITICAL: 0)

┌──────────────────────────────────┬────────────────┬──────────┬────────┬───────────────────┬───────────────┬────────────────────────────────────────────────────────┐
│             Library              │ Vulnerability  │ Severity │ Status │ Installed Version │ Fixed Version │                         Title                          │
├──────────────────────────────────┼────────────────┼──────────┼────────┼───────────────────┼───────────────┼────────────────────────────────────────────────────────┤
│ github.com/containerd/containerd │ CVE-2026-46680 │ HIGH     │ fixed  │ v1.7.30           │ 1.7.32        │ containerd user ID handling bypass allows runAsNonRoot │
│                                  │                │          │        │                   │               │ evasion                                                │
│                                  │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-46680             │
└──────────────────────────────────┴────────────────┴──────────┴────────┴───────────────────┴───────────────┴────────────────────────────────────────────────────────┘

home/klipper-helm/.local/share/helm/plugins/helm-set-status/helm-set-status (gobinary)
======================================================================================
Total: 1 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 1, CRITICAL: 0)

┌──────────────────────────────────┬────────────────┬──────────┬────────┬───────────────────┬───────────────┬────────────────────────────────────────────────────────┐
│             Library              │ Vulnerability  │ Severity │ Status │ Installed Version │ Fixed Version │                         Title                          │
├──────────────────────────────────┼────────────────┼──────────┼────────┼───────────────────┼───────────────┼────────────────────────────────────────────────────────┤
│ github.com/containerd/containerd │ CVE-2026-46680 │ HIGH     │ fixed  │ v1.7.30           │ 1.7.32        │ containerd user ID handling bypass allows runAsNonRoot │
│                                  │                │          │        │                   │               │ evasion                                                │
│                                  │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-46680             │
└──────────────────────────────────┴────────────────┴──────────┴────────┴───────────────────┴───────────────┴────────────────────────────────────────────────────────┘

usr/bin/helm (gobinary)
=======================
Total: 1 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 1, CRITICAL: 0)

┌──────────────────────────────────┬────────────────┬──────────┬────────┬───────────────────┬───────────────┬────────────────────────────────────────────────────────┐
│             Library              │ Vulnerability  │ Severity │ Status │ Installed Version │ Fixed Version │                         Title                          │
├──────────────────────────────────┼────────────────┼──────────┼────────┼───────────────────┼───────────────┼────────────────────────────────────────────────────────┤
│ github.com/containerd/containerd │ CVE-2026-46680 │ HIGH     │ fixed  │ v1.7.30           │ 1.7.32        │ containerd user ID handling bypass allows runAsNonRoot │
│                                  │                │          │        │                   │               │ evasion                                                │
│                                  │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-46680             │
└──────────────────────────────────┴────────────────┴──────────┴────────┴───────────────────┴───────────────┴────────────────────────────────────────────────────────┘
```

## Scan Results: `docker.io/rancher/klipper-lb:v0.4.17`

```text
```

## Scan Results: `docker.io/rancher/mirrored-pause:3.6`

```text
```

## Scan Results: `docker.io/rancher/rke2-cloud-provider:v1.36.1-0.20260508014929-7bbbf7c9b258-build20260515`

```text
```

## Scan Results: `docker.io/rancher/hardened-snapshot-controller:v8.5.0-build20260513`

```text
```

## Scan Results: `docker.io/rancher/hardened-traefik:v3.6.16-build20260512`

```text
```

## Scan Results: `docker.io/rancher/hardened-calico:v3.32.0-build20260511`

```text

docker.io/rancher/hardened-calico:v3.32.0-build20260511 (sles 15.7)
===================================================================
Total: 1 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 1, CRITICAL: 0)

┌──────────┬─────────────────────┬──────────┬────────┬────────────────────┬────────────────────┬────────────────────────┐
│ Library  │    Vulnerability    │ Severity │ Status │ Installed Version  │   Fixed Version    │         Title          │
├──────────┼─────────────────────┼──────────┼────────┼────────────────────┼────────────────────┼────────────────────────┤
│ liblzma5 │ SUSE-SU-2026:2051-1 │ HIGH     │ fixed  │ 5.4.1-150600.3.3.1 │ 5.4.1-150600.3.6.1 │ Security update for xz │
└──────────┴─────────────────────┴──────────┴────────┴────────────────────┴────────────────────┴────────────────────────┘
```

## Scan Results: `docker.io/rancher/hardened-flannel:v0.28.4-build20260511`

```text
```

## Summary

### CVEs by Severity

| Severity | Count |
| --- | ---: |
| CRITICAL | 0 |
| HIGH | 11 |
| **Total** | **11** |

### Images with CVEs (4)

| Image | CRITICAL | HIGH |
| --- | ---: | ---: |
| `docker.io/rancher/rke2-runtime:v1.36.1-rke2r2` | 0 | 3 |
| `docker.io/rancher/hardened-kubernetes:v1.36.1-rke2r2-build20260521` | 0 | 4 |
| `docker.io/rancher/klipper-helm:v0.10.0-build20260513` | 0 | 3 |
| `docker.io/rancher/hardened-calico:v3.32.0-build20260511` | 0 | 1 |

### CVE-free Images (12)

- `docker.io/rancher/hardened-coredns:v1.14.3-build20260511`
- `docker.io/rancher/hardened-cluster-autoscaler:v1.10.3-build20260511`
- `docker.io/rancher/hardened-dns-node-cache:1.26.8-build20260511`
- `docker.io/rancher/hardened-etcd:v3.6.7-k3s1-build20260512`
- `docker.io/rancher/hardened-k8s-metrics-server:v0.8.1-build20260513`
- `docker.io/rancher/hardened-addon-resizer:1.8.23-build20260511`
- `docker.io/rancher/klipper-lb:v0.4.17`
- `docker.io/rancher/mirrored-pause:3.6`
- `docker.io/rancher/rke2-cloud-provider:v1.36.1-0.20260508014929-7bbbf7c9b258-build20260515`
- `docker.io/rancher/hardened-snapshot-controller:v8.5.0-build20260513`
- `docker.io/rancher/hardened-traefik:v3.6.16-build20260512`
- `docker.io/rancher/hardened-flannel:v0.28.4-build20260511`

