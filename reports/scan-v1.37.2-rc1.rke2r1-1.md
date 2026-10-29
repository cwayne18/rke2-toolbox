# Trivy Scan Report

<!-- scan-source-ref: release:v1.37.2-rc1+rke2r1 -->
<!-- scan-source-desc: release v1.37.2-rc1+rke2r1 -->
<!-- suse-cvss-rescore: enabled -->
> Go binary CVE severities reflect SUSE's CVSS re-scoring where it differs from Trivy.

## Images Scanned

- `docker.io/rancher/rke2-runtime:v1.37.2-rc1-rke2r1`
- `docker.io/rancher/hardened-kubernetes:v1.37.2-rke2r1-build20261029`
- `docker.io/rancher/hardened-coredns:v1.14.7-build20261020`
- `docker.io/rancher/hardened-cluster-autoscaler:v1.11.0-build20261020`
- `docker.io/rancher/hardened-dns-node-cache:1.27.2-r1-build20261022`
- `docker.io/rancher/hardened-etcd:v3.7.1-k3s3-build20261020`
- `docker.io/rancher/hardened-k8s-metrics-server:v0.9.0-build20261020`
- `docker.io/rancher/hardened-addon-resizer:1.8.24-build20261021`
- `docker.io/rancher/klipper-helm:v0.13.3-build20261021`
- `docker.io/rancher/klipper-lb:v0.4.17`
- `docker.io/rancher/mirrored-pause:3.10.2`
- `docker.io/rancher/rke2-cloud-provider:v1.37.2-0.20261016152943-06368081f0b2-build20261021`
- `docker.io/rancher/rke2-security-responder:v0.1.9`
- `docker.io/rancher/hardened-snapshot-controller:v8.7.0-build20261021`
- `docker.io/rancher/hardened-traefik:v3.7.16-build20261028`
- `docker.io/rancher/hardened-calico:v3.32.2-build20261022`
- `docker.io/rancher/hardened-flannel:v0.28.10-build20261022`

## Scan Results: `docker.io/rancher/rke2-runtime:v1.37.2-rc1-rke2r1`

```text
```

## Scan Results: `docker.io/rancher/hardened-kubernetes:v1.37.2-rke2r1-build20261029`

```text
```

## Scan Results: `docker.io/rancher/hardened-coredns:v1.14.7-build20261020`

```text
```

## Scan Results: `docker.io/rancher/hardened-cluster-autoscaler:v1.11.0-build20261020`

```text
```

## Scan Results: `docker.io/rancher/hardened-dns-node-cache:1.27.2-r1-build20261022`

```text
```

## Scan Results: `docker.io/rancher/hardened-etcd:v3.7.1-k3s3-build20261020`

```text

usr/local/bin/etcd (gobinary)
=============================
Total: 1 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 1, CRITICAL: 0)

┌───────────────────┬────────────────┬──────────┬────────┬───────────────────┬───────────────┬─────────────────────────────────────────────────────────────┐
│      Library      │ Vulnerability  │ Severity │ Status │ Installed Version │ Fixed Version │                            Title                            │
├───────────────────┼────────────────┼──────────┼────────┼───────────────────┼───────────────┼─────────────────────────────────────────────────────────────┤
│ golang.org/x/text │ CVE-2026-56851 │ HIGH     │ fixed  │ v0.39.0           │ 0.41.0        │ golang.org/x/text: golang.org/x/text: Denial of Service via │
│                   │                │          │        │                   │               │ out-of-bounds slice error in Nickname profile...            │
│                   │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-56851                  │
└───────────────────┴────────────────┴──────────┴────────┴───────────────────┴───────────────┴─────────────────────────────────────────────────────────────┘

usr/local/bin/etcdctl (gobinary)
================================
Total: 1 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 1, CRITICAL: 0)

┌───────────────────┬────────────────┬──────────┬────────┬───────────────────┬───────────────┬─────────────────────────────────────────────────────────────┐
│      Library      │ Vulnerability  │ Severity │ Status │ Installed Version │ Fixed Version │                            Title                            │
├───────────────────┼────────────────┼──────────┼────────┼───────────────────┼───────────────┼─────────────────────────────────────────────────────────────┤
│ golang.org/x/text │ CVE-2026-56851 │ HIGH     │ fixed  │ v0.39.0           │ 0.41.0        │ golang.org/x/text: golang.org/x/text: Denial of Service via │
│                   │                │          │        │                   │               │ out-of-bounds slice error in Nickname profile...            │
│                   │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-56851                  │
└───────────────────┴────────────────┴──────────┴────────┴───────────────────┴───────────────┴─────────────────────────────────────────────────────────────┘
```

## Scan Results: `docker.io/rancher/hardened-k8s-metrics-server:v0.9.0-build20261020`

```text
```

## Scan Results: `docker.io/rancher/hardened-addon-resizer:1.8.24-build20261021`

```text
```

## Scan Results: `docker.io/rancher/klipper-helm:v0.13.3-build20261021`

```text
```

## Scan Results: `docker.io/rancher/klipper-lb:v0.4.17`

```text
```

## Scan Results: `docker.io/rancher/mirrored-pause:3.10.2`

```text
```

## Scan Results: `docker.io/rancher/rke2-cloud-provider:v1.37.2-0.20261016152943-06368081f0b2-build20261021`

```text
```

## Scan Results: `docker.io/rancher/rke2-security-responder:v0.1.9`

```text
```

## Scan Results: `docker.io/rancher/hardened-snapshot-controller:v8.7.0-build20261021`

```text
```

## Scan Results: `docker.io/rancher/hardened-traefik:v3.7.16-build20261028`

```text
```

## Scan Results: `docker.io/rancher/hardened-calico:v3.32.2-build20261022`

```text

opt/cni/bin/calico (gobinary)
=============================
Total: 1 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 1, CRITICAL: 0)

┌───────────────────────────────┬────────────────┬──────────┬────────┬───────────────────┬───────────────┬──────────────────────────────────────────────────────────────┐
│            Library            │ Vulnerability  │ Severity │ Status │ Installed Version │ Fixed Version │                            Title                             │
├───────────────────────────────┼────────────────┼──────────┼────────┼───────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ github.com/klauspost/compress │ CVE-2026-63209 │ HIGH     │ fixed  │ v1.18.0           │ 1.18.7        │ github.com/klauspost/compress: klauspost/compress: Denial of │
│                               │                │          │        │                   │               │ Service via integer overflow in dictionary processing        │
│                               │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-63209                   │
└───────────────────────────────┴────────────────┴──────────┴────────┴───────────────────┴───────────────┴──────────────────────────────────────────────────────────────┘

opt/cni/bin/calico-ipam (gobinary)
==================================
Total: 1 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 1, CRITICAL: 0)

┌───────────────────────────────┬────────────────┬──────────┬────────┬───────────────────┬───────────────┬──────────────────────────────────────────────────────────────┐
│            Library            │ Vulnerability  │ Severity │ Status │ Installed Version │ Fixed Version │                            Title                             │
├───────────────────────────────┼────────────────┼──────────┼────────┼───────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ github.com/klauspost/compress │ CVE-2026-63209 │ HIGH     │ fixed  │ v1.18.0           │ 1.18.7        │ github.com/klauspost/compress: klauspost/compress: Denial of │
│                               │                │          │        │                   │               │ Service via integer overflow in dictionary processing        │
│                               │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-63209                   │
└───────────────────────────────┴────────────────┴──────────┴────────┴───────────────────┴───────────────┴──────────────────────────────────────────────────────────────┘
```

## Scan Results: `docker.io/rancher/hardened-flannel:v0.28.10-build20261022`

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
| `docker.io/rancher/hardened-etcd:v3.7.1-k3s3-build20261020` | 0 | 2 |
| `docker.io/rancher/hardened-calico:v3.32.2-build20261022` | 0 | 2 |

### CVE-free Images (15)

- `docker.io/rancher/rke2-runtime:v1.37.2-rc1-rke2r1`
- `docker.io/rancher/hardened-kubernetes:v1.37.2-rke2r1-build20261029`
- `docker.io/rancher/hardened-coredns:v1.14.7-build20261020`
- `docker.io/rancher/hardened-cluster-autoscaler:v1.11.0-build20261020`
- `docker.io/rancher/hardened-dns-node-cache:1.27.2-r1-build20261022`
- `docker.io/rancher/hardened-k8s-metrics-server:v0.9.0-build20261020`
- `docker.io/rancher/hardened-addon-resizer:1.8.24-build20261021`
- `docker.io/rancher/klipper-helm:v0.13.3-build20261021`
- `docker.io/rancher/klipper-lb:v0.4.17`
- `docker.io/rancher/mirrored-pause:3.10.2`
- `docker.io/rancher/rke2-cloud-provider:v1.37.2-0.20261016152943-06368081f0b2-build20261021`
- `docker.io/rancher/rke2-security-responder:v0.1.9`
- `docker.io/rancher/hardened-snapshot-controller:v8.7.0-build20261021`
- `docker.io/rancher/hardened-traefik:v3.7.16-build20261028`
- `docker.io/rancher/hardened-flannel:v0.28.10-build20261022`

