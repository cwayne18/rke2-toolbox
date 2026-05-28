# Trivy Scan Report

## Images Scanned

- `docker.io/rancher/rke2-runtime:v1.36.1-rc3-rke2r2`
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

## Scan Results: `docker.io/rancher/rke2-runtime:v1.36.1-rc3-rke2r2`

```text

bin/containerd (gobinary)
=========================
Total: 3 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 3, CRITICAL: 0)

┌─────────────────────────────────────┬────────────────┬──────────┬──────────┬──────────────────────┬─────────────────────┬───────────────────────────────────────────────────────────┐
│               Library               │ Vulnerability  │ Severity │  Status  │  Installed Version   │    Fixed Version    │                           Title                           │
├─────────────────────────────────────┼────────────────┼──────────┼──────────┼──────────────────────┼─────────────────────┼───────────────────────────────────────────────────────────┤
│ github.com/containerd/containerd/v2 │ CVE-2026-46680 │ HIGH     │ fixed    │ v2.2.3-k3s1          │ 2.0.9, 2.2.4, 2.3.1 │ containerd user ID handling bypass allows runAsNonRoot    │
│                                     │                │          │          │                      │                     │ evasion                                                   │
│                                     │                │          │          │                      │                     │ https://avd.aquasec.com/nvd/cve-2026-46680                │
├─────────────────────────────────────┼────────────────┤          ├──────────┼──────────────────────┼─────────────────────┼───────────────────────────────────────────────────────────┤
│ github.com/docker/docker            │ CVE-2026-41567 │          │ affected │ v27.3.1+incompatible │                     │ Docker: `PUT /containers/{id}/archive` executes container │
│                                     │                │          │          │                      │                     │ binary on the host                                        │
│                                     │                │          │          │                      │                     │ https://avd.aquasec.com/nvd/cve-2026-41567                │
│                                     ├────────────────┤          │          │                      ├─────────────────────┼───────────────────────────────────────────────────────────┤
│                                     │ CVE-2026-42306 │          │          │                      │                     │ Docker: Race condition in docker cp allows bind mount     │
│                                     │                │          │          │                      │                     │ redirection to host...                                    │
│                                     │                │          │          │                      │                     │ https://avd.aquasec.com/nvd/cve-2026-42306                │
└─────────────────────────────────────┴────────────────┴──────────┴──────────┴──────────────────────┴─────────────────────┴───────────────────────────────────────────────────────────┘

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

bin/crictl (gobinary)
=====================
Total: 2 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 2, CRITICAL: 0)

┌──────────────────────────┬────────────────┬──────────┬──────────┬──────────────────────┬───────────────┬───────────────────────────────────────────────────────────┐
│         Library          │ Vulnerability  │ Severity │  Status  │  Installed Version   │ Fixed Version │                           Title                           │
├──────────────────────────┼────────────────┼──────────┼──────────┼──────────────────────┼───────────────┼───────────────────────────────────────────────────────────┤
│ github.com/docker/docker │ CVE-2026-41567 │ HIGH     │ affected │ v27.1.1+incompatible │               │ Docker: `PUT /containers/{id}/archive` executes container │
│                          │                │          │          │                      │               │ binary on the host                                        │
│                          │                │          │          │                      │               │ https://avd.aquasec.com/nvd/cve-2026-41567                │
│                          ├────────────────┤          │          │                      ├───────────────┼───────────────────────────────────────────────────────────┤
│                          │ CVE-2026-42306 │          │          │                      │               │ Docker: Race condition in docker cp allows bind mount     │
│                          │                │          │          │                      │               │ redirection to host...                                    │
│                          │                │          │          │                      │               │ https://avd.aquasec.com/nvd/cve-2026-42306                │
└──────────────────────────┴────────────────┴──────────┴──────────┴──────────────────────┴───────────────┴───────────────────────────────────────────────────────────┘

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
```

## Scan Results: `docker.io/rancher/hardened-coredns:v1.14.3-build20260511`

```text

docker.io/rancher/hardened-coredns:v1.14.3-build20260511 (sles 15.7)
====================================================================
Total: 1 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 1, CRITICAL: 0)

┌─────────┬─────────────────────┬──────────┬────────┬───────────────────────┬───────────────────────┬─────────────────────────────┐
│ Library │    Vulnerability    │ Severity │ Status │   Installed Version   │     Fixed Version     │            Title            │
├─────────┼─────────────────────┼──────────┼────────┼───────────────────────┼───────────────────────┼─────────────────────────────┤
│ busybox │ SUSE-SU-2026:2054-1 │ HIGH     │ fixed  │ 1.37.0-150700.18.15.1 │ 1.37.0-150700.18.18.1 │ Security update for busybox │
└─────────┴─────────────────────┴──────────┴────────┴───────────────────────┴───────────────────────┴─────────────────────────────┘
```

## Scan Results: `docker.io/rancher/hardened-cluster-autoscaler:v1.10.3-build20260511`

```text
```

## Scan Results: `docker.io/rancher/hardened-dns-node-cache:1.26.8-build20260511`

```text

docker.io/rancher/hardened-dns-node-cache:1.26.8-build20260511 (sles 15.7)
==========================================================================
Total: 1 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 1, CRITICAL: 0)

┌─────────┬─────────────────────┬──────────┬────────┬───────────────────────┬───────────────────────┬─────────────────────────────┐
│ Library │    Vulnerability    │ Severity │ Status │   Installed Version   │     Fixed Version     │            Title            │
├─────────┼─────────────────────┼──────────┼────────┼───────────────────────┼───────────────────────┼─────────────────────────────┤
│ busybox │ SUSE-SU-2026:2054-1 │ HIGH     │ fixed  │ 1.37.0-150700.18.15.1 │ 1.37.0-150700.18.18.1 │ Security update for busybox │
└─────────┴─────────────────────┴──────────┴────────┴───────────────────────┴───────────────────────┴─────────────────────────────┘
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

docker.io/rancher/hardened-flannel:v0.28.4-build20260511 (sles 15.7)
====================================================================
Total: 1 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 1, CRITICAL: 0)

┌─────────┬─────────────────────┬──────────┬────────┬───────────────────────┬───────────────────────┬─────────────────────────────┐
│ Library │    Vulnerability    │ Severity │ Status │   Installed Version   │     Fixed Version     │            Title            │
├─────────┼─────────────────────┼──────────┼────────┼───────────────────────┼───────────────────────┼─────────────────────────────┤
│ busybox │ SUSE-SU-2026:2054-1 │ HIGH     │ fixed  │ 1.37.0-150700.18.15.1 │ 1.37.0-150700.18.18.1 │ Security update for busybox │
└─────────┴─────────────────────┴──────────┴────────┴───────────────────────┴───────────────────────┴─────────────────────────────┘
```

## Summary

### CVEs by Severity

| Severity | Count |
| --- | ---: |
| CRITICAL | 0 |
| HIGH | 14 |
| **Total** | **14** |

### Scan Coverage

| Metric | Count |
| --- | ---: |
| Images scanned | 16 |
| Binaries scanned | 55 |
| **Total scanned targets** | **71** |

### Images with CVEs (6)

| Image | CRITICAL | HIGH |
| --- | ---: | ---: |
| `docker.io/rancher/rke2-runtime:v1.36.1-rc3-rke2r2` | 0 | 7 |
| `docker.io/rancher/hardened-coredns:v1.14.3-build20260511` | 0 | 1 |
| `docker.io/rancher/hardened-dns-node-cache:1.26.8-build20260511` | 0 | 1 |
| `docker.io/rancher/klipper-helm:v0.10.0-build20260513` | 0 | 3 |
| `docker.io/rancher/hardened-calico:v3.32.0-build20260511` | 0 | 1 |
| `docker.io/rancher/hardened-flannel:v0.28.4-build20260511` | 0 | 1 |

### CVE-free Images (10)

- `docker.io/rancher/hardened-kubernetes:v1.36.1-rke2r2-build20260521`
- `docker.io/rancher/hardened-cluster-autoscaler:v1.10.3-build20260511`
- `docker.io/rancher/hardened-etcd:v3.6.7-k3s1-build20260512`
- `docker.io/rancher/hardened-k8s-metrics-server:v0.8.1-build20260513`
- `docker.io/rancher/hardened-addon-resizer:1.8.23-build20260511`
- `docker.io/rancher/klipper-lb:v0.4.17`
- `docker.io/rancher/mirrored-pause:3.6`
- `docker.io/rancher/rke2-cloud-provider:v1.36.1-0.20260508014929-7bbbf7c9b258-build20260515`
- `docker.io/rancher/hardened-snapshot-controller:v8.5.0-build20260513`
- `docker.io/rancher/hardened-traefik:v3.6.16-build20260512`

