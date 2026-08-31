# Trivy Scan Report

<!-- scan-source-ref: release:v1.36.4+rke2r1 -->
<!-- scan-source-desc: release v1.36.4+rke2r1 -->
<!-- suse-cvss-rescore: enabled -->
> Go binary CVE severities reflect SUSE's CVSS re-scoring where it differs from Trivy.

## Images Scanned

- `docker.io/rancher/rke2-runtime:v1.36.4-rke2r1`
- `docker.io/rancher/hardened-kubernetes:v1.36.4-rke2r1-build20260821`
- `docker.io/rancher/hardened-coredns:v1.14.7-build20260819`
- `docker.io/rancher/hardened-cluster-autoscaler:v1.10.3-build20260819`
- `docker.io/rancher/hardened-dns-node-cache:1.26.8-build20260819`
- `docker.io/rancher/hardened-etcd:v3.6.14-k3s1-build20260819`
- `docker.io/rancher/hardened-k8s-metrics-server:v0.9.0-build20260819`
- `docker.io/rancher/hardened-addon-resizer:1.8.23-build20260819`
- `docker.io/rancher/klipper-helm:v0.13.3-build20260820`
- `docker.io/rancher/klipper-lb:v0.4.17`
- `docker.io/rancher/mirrored-pause:3.10.2`
- `docker.io/rancher/rke2-cloud-provider:v1.36.4-0.20260817193921-a2fc9574e060-build20260820`
- `docker.io/rancher/hardened-snapshot-controller:v8.6.0-build20260819`
- `docker.io/rancher/hardened-traefik:v3.7.11-build20260819`
- `docker.io/rancher/hardened-calico:v3.32.1-build20260827`
- `docker.io/rancher/hardened-flannel:v0.28.9-build20260819`

## Scan Results: `docker.io/rancher/rke2-runtime:v1.36.4-rke2r1`

```text

bin/crictl (gobinary)
=====================
Total: 1 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 1, CRITICAL: 0)

┌──────────────────┬────────────────┬──────────┬────────┬───────────────────┬───────────────┬───────────────────────────────────────────────────────────┐
│     Library      │ Vulnerability  │ Severity │ Status │ Installed Version │ Fixed Version │                           Title                           │
├──────────────────┼────────────────┼──────────┼────────┼───────────────────┼───────────────┼───────────────────────────────────────────────────────────┤
│ golang.org/x/mod │ CVE-2026-56865 │ HIGH     │ fixed  │ v0.35.0           │ 0.40.0        │ golang.org/x/mod/sumdb/tlog: golang.org/x/mod/sumdb/tlog: │
│                  │                │          │        │                   │               │ Supply chain compromise via transparency log tile         │
│                  │                │          │        │                   │               │ verification bypass                                       │
│                  │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-56865                │
└──────────────────┴────────────────┴──────────┴────────┴───────────────────┴───────────────┴───────────────────────────────────────────────────────────┘

bin/runc (gobinary)
===================
Total: 1 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 1, CRITICAL: 0)

┌────────────────────────┬────────────────┬──────────┬────────┬───────────────────┬───────────────┬────────────────────────────────────────────────────────────┐
│        Library         │ Vulnerability  │ Severity │ Status │ Installed Version │ Fixed Version │                           Title                            │
├────────────────────────┼────────────────┼──────────┼────────┼───────────────────┼───────────────┼────────────────────────────────────────────────────────────┤
│ github.com/cilium/ebpf │ CVE-2026-10722 │ HIGH     │ fixed  │ v0.17.3           │ 0.22.0        │ github.com/cilium/ebpf: Cilium ebpf: Denial of Service via │
│                        │                │          │        │                   │               │ integer overflow                                           │
│                        │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-10722                 │
└────────────────────────┴────────────────┴──────────┴────────┴───────────────────┴───────────────┴────────────────────────────────────────────────────────────┘
```

## Scan Results: `docker.io/rancher/hardened-kubernetes:v1.36.4-rke2r1-build20260821`

```text
```

## Scan Results: `docker.io/rancher/hardened-coredns:v1.14.7-build20260819`

```text
```

## Scan Results: `docker.io/rancher/hardened-cluster-autoscaler:v1.10.3-build20260819`

```text
```

## Scan Results: `docker.io/rancher/hardened-dns-node-cache:1.26.8-build20260819`

```text
```

## Scan Results: `docker.io/rancher/hardened-etcd:v3.6.14-k3s1-build20260819`

```text
```

## Scan Results: `docker.io/rancher/hardened-k8s-metrics-server:v0.9.0-build20260819`

```text
```

## Scan Results: `docker.io/rancher/hardened-addon-resizer:1.8.23-build20260819`

```text
```

## Scan Results: `docker.io/rancher/klipper-helm:v0.13.3-build20260820`

```text
```

## Scan Results: `docker.io/rancher/klipper-lb:v0.4.17`

```text
```

## Scan Results: `docker.io/rancher/mirrored-pause:3.10.2`

```text
```

## Scan Results: `docker.io/rancher/rke2-cloud-provider:v1.36.4-0.20260817193921-a2fc9574e060-build20260820`

```text
```

## Scan Results: `docker.io/rancher/hardened-snapshot-controller:v8.6.0-build20260819`

```text
```

## Scan Results: `docker.io/rancher/hardened-traefik:v3.7.11-build20260819`

```text
```

## Scan Results: `docker.io/rancher/hardened-calico:v3.32.1-build20260827`

```text
```

## Scan Results: `docker.io/rancher/hardened-flannel:v0.28.9-build20260819`

```text
```

## Summary

### CVEs by Severity

| Severity | Count |
| --- | ---: |
| CRITICAL | 0 |
| HIGH | 2 |
| **Total** | **2** |

### Images with CVEs (1)

| Image | CRITICAL | HIGH |
| --- | ---: | ---: |
| `docker.io/rancher/rke2-runtime:v1.36.4-rke2r1` | 0 | 2 |

### CVE-free Images (15)

- `docker.io/rancher/hardened-kubernetes:v1.36.4-rke2r1-build20260821`
- `docker.io/rancher/hardened-coredns:v1.14.7-build20260819`
- `docker.io/rancher/hardened-cluster-autoscaler:v1.10.3-build20260819`
- `docker.io/rancher/hardened-dns-node-cache:1.26.8-build20260819`
- `docker.io/rancher/hardened-etcd:v3.6.14-k3s1-build20260819`
- `docker.io/rancher/hardened-k8s-metrics-server:v0.9.0-build20260819`
- `docker.io/rancher/hardened-addon-resizer:1.8.23-build20260819`
- `docker.io/rancher/klipper-helm:v0.13.3-build20260820`
- `docker.io/rancher/klipper-lb:v0.4.17`
- `docker.io/rancher/mirrored-pause:3.10.2`
- `docker.io/rancher/rke2-cloud-provider:v1.36.4-0.20260817193921-a2fc9574e060-build20260820`
- `docker.io/rancher/hardened-snapshot-controller:v8.6.0-build20260819`
- `docker.io/rancher/hardened-traefik:v3.7.11-build20260819`
- `docker.io/rancher/hardened-calico:v3.32.1-build20260827`
- `docker.io/rancher/hardened-flannel:v0.28.9-build20260819`

