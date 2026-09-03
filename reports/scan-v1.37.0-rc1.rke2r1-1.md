# Trivy Scan Report

<!-- scan-source-ref: release:v1.37.0-rc1+rke2r1 -->
<!-- scan-source-desc: release v1.37.0-rc1+rke2r1 -->
<!-- suse-cvss-rescore: enabled -->
> Go binary CVE severities reflect SUSE's CVSS re-scoring where it differs from Trivy.

## Images Scanned

- `docker.io/rancher/rke2-runtime:v1.37.0-rc1-rke2r1`
- `docker.io/rancher/hardened-kubernetes:v1.37.0-rke2r1-build20260827`
- `docker.io/rancher/hardened-coredns:v1.14.7-build20260819`
- `docker.io/rancher/hardened-cluster-autoscaler:v1.10.3-build20260819`
- `docker.io/rancher/hardened-dns-node-cache:1.26.8-build20260819`
- `docker.io/rancher/hardened-etcd:v3.7.1-k3s1-build20260901`
- `docker.io/rancher/hardened-k8s-metrics-server:v0.9.0-build20260819`
- `docker.io/rancher/hardened-addon-resizer:1.8.23-build20260819`
- `docker.io/rancher/klipper-helm:v0.13.3-build20260820`
- `docker.io/rancher/klipper-lb:v0.4.17`
- `docker.io/rancher/mirrored-pause:3.10.2`
- `docker.io/rancher/rke2-cloud-provider:v1.35.1-0.20260817230842-2a1e2e8cf41b-build20260820`
- `docker.io/rancher/rke2-security-responder:v0.1.5`
- `docker.io/rancher/hardened-snapshot-controller:v8.6.0-build20260819`
- `docker.io/rancher/hardened-traefik:v3.7.11-build20260819`
- `docker.io/rancher/hardened-calico:v3.32.1-build20260827`
- `docker.io/rancher/hardened-flannel:v0.28.9-build20260819`

## Scan Results: `docker.io/rancher/rke2-runtime:v1.37.0-rc1-rke2r1`

```text

bin/containerd (gobinary)
=========================
Total: 1 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 1, CRITICAL: 0)

┌────────────────────────┬────────────────┬──────────┬────────┬───────────────────┬───────────────┬─────────────────────────────────────────────────────────────┐
│        Library         │ Vulnerability  │ Severity │ Status │ Installed Version │ Fixed Version │                            Title                            │
├────────────────────────┼────────────────┼──────────┼────────┼───────────────────┼───────────────┼─────────────────────────────────────────────────────────────┤
│ google.golang.org/grpc │ CVE-2026-84304 │ HIGH     │ fixed  │ v1.82.1           │ 1.83.1        │ gRPC-Go is the Go language implementation of gRPC. Prior to │
│                        │                │          │        │                   │               │ 1.83.1, in...                                               │
│                        │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-84304                  │
└────────────────────────┴────────────────┴──────────┴────────┴───────────────────┴───────────────┴─────────────────────────────────────────────────────────────┘

bin/containerd-shim-runc-v2 (gobinary)
======================================
Total: 1 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 1, CRITICAL: 0)

┌────────────────────────┬────────────────┬──────────┬────────┬───────────────────┬───────────────┬─────────────────────────────────────────────────────────────┐
│        Library         │ Vulnerability  │ Severity │ Status │ Installed Version │ Fixed Version │                            Title                            │
├────────────────────────┼────────────────┼──────────┼────────┼───────────────────┼───────────────┼─────────────────────────────────────────────────────────────┤
│ google.golang.org/grpc │ CVE-2026-84304 │ HIGH     │ fixed  │ v1.82.1           │ 1.83.1        │ gRPC-Go is the Go language implementation of gRPC. Prior to │
│                        │                │          │        │                   │               │ 1.83.1, in...                                               │
│                        │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-84304                  │
└────────────────────────┴────────────────┴──────────┴────────┴───────────────────┴───────────────┴─────────────────────────────────────────────────────────────┘

bin/crictl (gobinary)
=====================
Total: 2 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 2, CRITICAL: 0)

┌────────────────────────┬────────────────┬──────────┬────────┬───────────────────┬───────────────┬─────────────────────────────────────────────────────────────┐
│        Library         │ Vulnerability  │ Severity │ Status │ Installed Version │ Fixed Version │                            Title                            │
├────────────────────────┼────────────────┼──────────┼────────┼───────────────────┼───────────────┼─────────────────────────────────────────────────────────────┤
│ golang.org/x/mod       │ CVE-2026-56865 │ HIGH     │ fixed  │ v0.38.0           │ 0.40.0        │ golang.org/x/mod/sumdb/tlog: golang.org/x/mod/sumdb/tlog:   │
│                        │                │          │        │                   │               │ Supply chain compromise via transparency log tile           │
│                        │                │          │        │                   │               │ verification bypass                                         │
│                        │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-56865                  │
├────────────────────────┼────────────────┤          │        ├───────────────────┼───────────────┼─────────────────────────────────────────────────────────────┤
│ google.golang.org/grpc │ CVE-2026-84304 │          │        │ v1.82.1           │ 1.83.1        │ gRPC-Go is the Go language implementation of gRPC. Prior to │
│                        │                │          │        │                   │               │ 1.83.1, in...                                               │
│                        │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-84304                  │
└────────────────────────┴────────────────┴──────────┴────────┴───────────────────┴───────────────┴─────────────────────────────────────────────────────────────┘

bin/ctr (gobinary)
==================
Total: 1 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 1, CRITICAL: 0)

┌────────────────────────┬────────────────┬──────────┬────────┬───────────────────┬───────────────┬─────────────────────────────────────────────────────────────┐
│        Library         │ Vulnerability  │ Severity │ Status │ Installed Version │ Fixed Version │                            Title                            │
├────────────────────────┼────────────────┼──────────┼────────┼───────────────────┼───────────────┼─────────────────────────────────────────────────────────────┤
│ google.golang.org/grpc │ CVE-2026-84304 │ HIGH     │ fixed  │ v1.82.1           │ 1.83.1        │ gRPC-Go is the Go language implementation of gRPC. Prior to │
│                        │                │          │        │                   │               │ 1.83.1, in...                                               │
│                        │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-84304                  │
└────────────────────────┴────────────────┴──────────┴────────┴───────────────────┴───────────────┴─────────────────────────────────────────────────────────────┘

bin/kubelet (gobinary)
======================
Total: 1 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 1, CRITICAL: 0)

┌────────────────────────┬────────────────┬──────────┬────────┬───────────────────┬───────────────┬─────────────────────────────────────────────────────────────┐
│        Library         │ Vulnerability  │ Severity │ Status │ Installed Version │ Fixed Version │                            Title                            │
├────────────────────────┼────────────────┼──────────┼────────┼───────────────────┼───────────────┼─────────────────────────────────────────────────────────────┤
│ google.golang.org/grpc │ CVE-2026-84304 │ HIGH     │ fixed  │ v1.82.1           │ 1.83.1        │ gRPC-Go is the Go language implementation of gRPC. Prior to │
│                        │                │          │        │                   │               │ 1.83.1, in...                                               │
│                        │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-84304                  │
└────────────────────────┴────────────────┴──────────┴────────┴───────────────────┴───────────────┴─────────────────────────────────────────────────────────────┘
```

## Scan Results: `docker.io/rancher/hardened-kubernetes:v1.37.0-rke2r1-build20260827`

```text

usr/local/bin/kube-apiserver (gobinary)
=======================================
Total: 1 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 1, CRITICAL: 0)

┌────────────────────────┬────────────────┬──────────┬────────┬───────────────────┬───────────────┬─────────────────────────────────────────────────────────────┐
│        Library         │ Vulnerability  │ Severity │ Status │ Installed Version │ Fixed Version │                            Title                            │
├────────────────────────┼────────────────┼──────────┼────────┼───────────────────┼───────────────┼─────────────────────────────────────────────────────────────┤
│ google.golang.org/grpc │ CVE-2026-84304 │ HIGH     │ fixed  │ v1.82.1           │ 1.83.1        │ gRPC-Go is the Go language implementation of gRPC. Prior to │
│                        │                │          │        │                   │               │ 1.83.1, in...                                               │
│                        │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-84304                  │
└────────────────────────┴────────────────┴──────────┴────────┴───────────────────┴───────────────┴─────────────────────────────────────────────────────────────┘

usr/local/bin/kube-controller-manager (gobinary)
================================================
Total: 1 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 1, CRITICAL: 0)

┌────────────────────────┬────────────────┬──────────┬────────┬───────────────────┬───────────────┬─────────────────────────────────────────────────────────────┐
│        Library         │ Vulnerability  │ Severity │ Status │ Installed Version │ Fixed Version │                            Title                            │
├────────────────────────┼────────────────┼──────────┼────────┼───────────────────┼───────────────┼─────────────────────────────────────────────────────────────┤
│ google.golang.org/grpc │ CVE-2026-84304 │ HIGH     │ fixed  │ v1.82.1           │ 1.83.1        │ gRPC-Go is the Go language implementation of gRPC. Prior to │
│                        │                │          │        │                   │               │ 1.83.1, in...                                               │
│                        │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-84304                  │
└────────────────────────┴────────────────┴──────────┴────────┴───────────────────┴───────────────┴─────────────────────────────────────────────────────────────┘

usr/local/bin/kube-proxy (gobinary)
===================================
Total: 1 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 1, CRITICAL: 0)

┌────────────────────────┬────────────────┬──────────┬────────┬───────────────────┬───────────────┬─────────────────────────────────────────────────────────────┐
│        Library         │ Vulnerability  │ Severity │ Status │ Installed Version │ Fixed Version │                            Title                            │
├────────────────────────┼────────────────┼──────────┼────────┼───────────────────┼───────────────┼─────────────────────────────────────────────────────────────┤
│ google.golang.org/grpc │ CVE-2026-84304 │ HIGH     │ fixed  │ v1.82.1           │ 1.83.1        │ gRPC-Go is the Go language implementation of gRPC. Prior to │
│                        │                │          │        │                   │               │ 1.83.1, in...                                               │
│                        │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-84304                  │
└────────────────────────┴────────────────┴──────────┴────────┴───────────────────┴───────────────┴─────────────────────────────────────────────────────────────┘

usr/local/bin/kube-scheduler (gobinary)
=======================================
Total: 1 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 1, CRITICAL: 0)

┌────────────────────────┬────────────────┬──────────┬────────┬───────────────────┬───────────────┬─────────────────────────────────────────────────────────────┐
│        Library         │ Vulnerability  │ Severity │ Status │ Installed Version │ Fixed Version │                            Title                            │
├────────────────────────┼────────────────┼──────────┼────────┼───────────────────┼───────────────┼─────────────────────────────────────────────────────────────┤
│ google.golang.org/grpc │ CVE-2026-84304 │ HIGH     │ fixed  │ v1.82.1           │ 1.83.1        │ gRPC-Go is the Go language implementation of gRPC. Prior to │
│                        │                │          │        │                   │               │ 1.83.1, in...                                               │
│                        │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-84304                  │
└────────────────────────┴────────────────┴──────────┴────────┴───────────────────┴───────────────┴─────────────────────────────────────────────────────────────┘

usr/local/bin/kubelet (gobinary)
================================
Total: 1 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 1, CRITICAL: 0)

┌────────────────────────┬────────────────┬──────────┬────────┬───────────────────┬───────────────┬─────────────────────────────────────────────────────────────┐
│        Library         │ Vulnerability  │ Severity │ Status │ Installed Version │ Fixed Version │                            Title                            │
├────────────────────────┼────────────────┼──────────┼────────┼───────────────────┼───────────────┼─────────────────────────────────────────────────────────────┤
│ google.golang.org/grpc │ CVE-2026-84304 │ HIGH     │ fixed  │ v1.82.1           │ 1.83.1        │ gRPC-Go is the Go language implementation of gRPC. Prior to │
│                        │                │          │        │                   │               │ 1.83.1, in...                                               │
│                        │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-84304                  │
└────────────────────────┴────────────────┴──────────┴────────┴───────────────────┴───────────────┴─────────────────────────────────────────────────────────────┘
```

## Scan Results: `docker.io/rancher/hardened-coredns:v1.14.7-build20260819`

```text

coredns (gobinary)
==================
Total: 1 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 1, CRITICAL: 0)

┌────────────────────────┬────────────────┬──────────┬────────┬───────────────────┬───────────────┬─────────────────────────────────────────────────────────────┐
│        Library         │ Vulnerability  │ Severity │ Status │ Installed Version │ Fixed Version │                            Title                            │
├────────────────────────┼────────────────┼──────────┼────────┼───────────────────┼───────────────┼─────────────────────────────────────────────────────────────┤
│ google.golang.org/grpc │ CVE-2026-84304 │ HIGH     │ fixed  │ v1.83.0           │ 1.83.1        │ gRPC-Go is the Go language implementation of gRPC. Prior to │
│                        │                │          │        │                   │               │ 1.83.1, in...                                               │
│                        │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-84304                  │
└────────────────────────┴────────────────┴──────────┴────────┴───────────────────┴───────────────┴─────────────────────────────────────────────────────────────┘
```

## Scan Results: `docker.io/rancher/hardened-cluster-autoscaler:v1.10.3-build20260819`

```text
```

## Scan Results: `docker.io/rancher/hardened-dns-node-cache:1.26.8-build20260819`

```text

node-cache (gobinary)
=====================
Total: 1 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 1, CRITICAL: 0)

┌────────────────────────┬────────────────┬──────────┬────────┬───────────────────┬───────────────┬─────────────────────────────────────────────────────────────┐
│        Library         │ Vulnerability  │ Severity │ Status │ Installed Version │ Fixed Version │                            Title                            │
├────────────────────────┼────────────────┼──────────┼────────┼───────────────────┼───────────────┼─────────────────────────────────────────────────────────────┤
│ google.golang.org/grpc │ CVE-2026-84304 │ HIGH     │ fixed  │ v1.82.1           │ 1.83.1        │ gRPC-Go is the Go language implementation of gRPC. Prior to │
│                        │                │          │        │                   │               │ 1.83.1, in...                                               │
│                        │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-84304                  │
└────────────────────────┴────────────────┴──────────┴────────┴───────────────────┴───────────────┴─────────────────────────────────────────────────────────────┘
```

## Scan Results: `docker.io/rancher/hardened-etcd:v3.7.1-k3s1-build20260901`

```text

usr/local/bin/etcd (gobinary)
=============================
Total: 1 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 1, CRITICAL: 0)

┌────────────────────────┬────────────────┬──────────┬────────┬───────────────────┬───────────────┬─────────────────────────────────────────────────────────────┐
│        Library         │ Vulnerability  │ Severity │ Status │ Installed Version │ Fixed Version │                            Title                            │
├────────────────────────┼────────────────┼──────────┼────────┼───────────────────┼───────────────┼─────────────────────────────────────────────────────────────┤
│ google.golang.org/grpc │ CVE-2026-84304 │ HIGH     │ fixed  │ v1.82.1           │ 1.83.1        │ gRPC-Go is the Go language implementation of gRPC. Prior to │
│                        │                │          │        │                   │               │ 1.83.1, in...                                               │
│                        │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-84304                  │
└────────────────────────┴────────────────┴──────────┴────────┴───────────────────┴───────────────┴─────────────────────────────────────────────────────────────┘

usr/local/bin/etcdctl (gobinary)
================================
Total: 1 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 1, CRITICAL: 0)

┌────────────────────────┬────────────────┬──────────┬────────┬───────────────────┬───────────────┬─────────────────────────────────────────────────────────────┐
│        Library         │ Vulnerability  │ Severity │ Status │ Installed Version │ Fixed Version │                            Title                            │
├────────────────────────┼────────────────┼──────────┼────────┼───────────────────┼───────────────┼─────────────────────────────────────────────────────────────┤
│ google.golang.org/grpc │ CVE-2026-84304 │ HIGH     │ fixed  │ v1.82.1           │ 1.83.1        │ gRPC-Go is the Go language implementation of gRPC. Prior to │
│                        │                │          │        │                   │               │ 1.83.1, in...                                               │
│                        │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-84304                  │
└────────────────────────┴────────────────┴──────────┴────────┴───────────────────┴───────────────┴─────────────────────────────────────────────────────────────┘
```

## Scan Results: `docker.io/rancher/hardened-k8s-metrics-server:v0.9.0-build20260819`

```text

metrics-server (gobinary)
=========================
Total: 2 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 1, CRITICAL: 1)

┌────────────────────────┬────────────────┬──────────┬────────┬───────────────────┬───────────────┬─────────────────────────────────────────────────────────────┐
│        Library         │ Vulnerability  │ Severity │ Status │ Installed Version │ Fixed Version │                            Title                            │
├────────────────────────┼────────────────┼──────────┼────────┼───────────────────┼───────────────┼─────────────────────────────────────────────────────────────┤
│ golang.org/x/crypto    │ CVE-2026-56854 │ CRITICAL │ fixed  │ v0.52.0           │ 0.55.0        │ golang.org/x/crypto/ssh: golang.org/x/crypto/ssh:           │
│                        │                │          │        │                   │               │ Authentication bypass due to unenforced source-address      │
│                        │                │          │        │                   │               │ restrictions                                                │
│                        │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-56854                  │
├────────────────────────┼────────────────┼──────────┤        ├───────────────────┼───────────────┼─────────────────────────────────────────────────────────────┤
│ google.golang.org/grpc │ CVE-2026-84304 │ HIGH     │        │ v1.82.1           │ 1.83.1        │ gRPC-Go is the Go language implementation of gRPC. Prior to │
│                        │                │          │        │                   │               │ 1.83.1, in...                                               │
│                        │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-84304                  │
└────────────────────────┴────────────────┴──────────┴────────┴───────────────────┴───────────────┴─────────────────────────────────────────────────────────────┘
```

## Scan Results: `docker.io/rancher/hardened-addon-resizer:1.8.23-build20260819`

```text
```

## Scan Results: `docker.io/rancher/klipper-helm:v0.13.3-build20260820`

```text

docker.io/rancher/klipper-helm:v0.13.3-build20260820 (alpine 3.24.1)
====================================================================
Total: 2 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 2, CRITICAL: 0)

┌─────────┬────────────────┬──────────┬────────┬───────────────────┬───────────────┬───────────────────────────────────────────────────────────┐
│ Library │ Vulnerability  │ Severity │ Status │ Installed Version │ Fixed Version │                           Title                           │
├─────────┼────────────────┼──────────┼────────┼───────────────────┼───────────────┼───────────────────────────────────────────────────────────┤
│ jq      │ CVE-2026-32316 │ HIGH     │ fixed  │ 1.8.1-r0          │ 1.8.2-r0      │ jq: jq: Denial of Service or potential arbitrary code     │
│         │                │          │        │                   │               │ execution due to...                                       │
│         │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-32316                │
│         ├────────────────┤          │        │                   │               ├───────────────────────────────────────────────────────────┤
│         │ CVE-2026-40164 │          │        │                   │               │ jq: jq: Denial of Service via crafted JSON object causing │
│         │                │          │        │                   │               │ hash collisions...                                        │
│         │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-40164                │
└─────────┴────────────────┴──────────┴────────┴───────────────────┴───────────────┴───────────────────────────────────────────────────────────┘

home/klipper-helm/.local/share/helm/plugins/helm-set-status/helm-set-status (gobinary)
======================================================================================
Total: 1 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 0, CRITICAL: 1)

┌─────────────────────┬────────────────┬──────────┬────────┬───────────────────┬───────────────┬────────────────────────────────────────────────────────┐
│       Library       │ Vulnerability  │ Severity │ Status │ Installed Version │ Fixed Version │                         Title                          │
├─────────────────────┼────────────────┼──────────┼────────┼───────────────────┼───────────────┼────────────────────────────────────────────────────────┤
│ golang.org/x/crypto │ CVE-2026-56854 │ CRITICAL │ fixed  │ v0.51.0           │ 0.55.0        │ golang.org/x/crypto/ssh: golang.org/x/crypto/ssh:      │
│                     │                │          │        │                   │               │ Authentication bypass due to unenforced source-address │
│                     │                │          │        │                   │               │ restrictions                                           │
│                     │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-56854             │
└─────────────────────┴────────────────┴──────────┴────────┴───────────────────┴───────────────┴────────────────────────────────────────────────────────┘

usr/bin/helm (gobinary)
=======================
Total: 1 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 0, CRITICAL: 1)

┌─────────────────────┬────────────────┬──────────┬────────┬───────────────────┬───────────────┬────────────────────────────────────────────────────────┐
│       Library       │ Vulnerability  │ Severity │ Status │ Installed Version │ Fixed Version │                         Title                          │
├─────────────────────┼────────────────┼──────────┼────────┼───────────────────┼───────────────┼────────────────────────────────────────────────────────┤
│ golang.org/x/crypto │ CVE-2026-56854 │ CRITICAL │ fixed  │ v0.51.0           │ 0.55.0        │ golang.org/x/crypto/ssh: golang.org/x/crypto/ssh:      │
│                     │                │          │        │                   │               │ Authentication bypass due to unenforced source-address │
│                     │                │          │        │                   │               │ restrictions                                           │
│                     │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-56854             │
└─────────────────────┴────────────────┴──────────┴────────┴───────────────────┴───────────────┴────────────────────────────────────────────────────────┘
```

## Scan Results: `docker.io/rancher/klipper-lb:v0.4.17`

```text
```

## Scan Results: `docker.io/rancher/mirrored-pause:3.10.2`

```text
```

## Scan Results: `docker.io/rancher/rke2-cloud-provider:v1.35.1-0.20260817230842-2a1e2e8cf41b-build20260820`

```text

usr/local/bin/rke2-cloud-provider (gobinary)
============================================
Total: 2 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 1, CRITICAL: 1)

┌────────────────────────┬────────────────┬──────────┬────────┬───────────────────┬───────────────┬─────────────────────────────────────────────────────────────┐
│        Library         │ Vulnerability  │ Severity │ Status │ Installed Version │ Fixed Version │                            Title                            │
├────────────────────────┼────────────────┼──────────┼────────┼───────────────────┼───────────────┼─────────────────────────────────────────────────────────────┤
│ golang.org/x/crypto    │ CVE-2026-56854 │ CRITICAL │ fixed  │ v0.54.0           │ 0.55.0        │ golang.org/x/crypto/ssh: golang.org/x/crypto/ssh:           │
│                        │                │          │        │                   │               │ Authentication bypass due to unenforced source-address      │
│                        │                │          │        │                   │               │ restrictions                                                │
│                        │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-56854                  │
├────────────────────────┼────────────────┼──────────┤        ├───────────────────┼───────────────┼─────────────────────────────────────────────────────────────┤
│ google.golang.org/grpc │ CVE-2026-84304 │ HIGH     │        │ v1.82.1           │ 1.83.1        │ gRPC-Go is the Go language implementation of gRPC. Prior to │
│                        │                │          │        │                   │               │ 1.83.1, in...                                               │
│                        │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-84304                  │
└────────────────────────┴────────────────┴──────────┴────────┴───────────────────┴───────────────┴─────────────────────────────────────────────────────────────┘
```

## Scan Results: `docker.io/rancher/rke2-security-responder:v0.1.5`

```text
```

## Scan Results: `docker.io/rancher/hardened-snapshot-controller:v8.6.0-build20260819`

```text

snapshot-controller (gobinary)
==============================
Total: 1 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 1, CRITICAL: 0)

┌────────────────────────┬────────────────┬──────────┬────────┬───────────────────┬───────────────┬─────────────────────────────────────────────────────────────┐
│        Library         │ Vulnerability  │ Severity │ Status │ Installed Version │ Fixed Version │                            Title                            │
├────────────────────────┼────────────────┼──────────┼────────┼───────────────────┼───────────────┼─────────────────────────────────────────────────────────────┤
│ google.golang.org/grpc │ CVE-2026-84304 │ HIGH     │ fixed  │ v1.82.1           │ 1.83.1        │ gRPC-Go is the Go language implementation of gRPC. Prior to │
│                        │                │          │        │                   │               │ 1.83.1, in...                                               │
│                        │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-84304                  │
└────────────────────────┴────────────────┴──────────┴────────┴───────────────────┴───────────────┴─────────────────────────────────────────────────────────────┘
```

## Scan Results: `docker.io/rancher/hardened-traefik:v3.7.11-build20260819`

```text

traefik (gobinary)
==================
Total: 1 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 1, CRITICAL: 0)

┌────────────────────────┬────────────────┬──────────┬────────┬───────────────────┬───────────────┬─────────────────────────────────────────────────────────────┐
│        Library         │ Vulnerability  │ Severity │ Status │ Installed Version │ Fixed Version │                            Title                            │
├────────────────────────┼────────────────┼──────────┼────────┼───────────────────┼───────────────┼─────────────────────────────────────────────────────────────┤
│ google.golang.org/grpc │ CVE-2026-84304 │ HIGH     │ fixed  │ v1.82.1           │ 1.83.1        │ gRPC-Go is the Go language implementation of gRPC. Prior to │
│                        │                │          │        │                   │               │ 1.83.1, in...                                               │
│                        │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-84304                  │
└────────────────────────┴────────────────┴──────────┴────────┴───────────────────┴───────────────┴─────────────────────────────────────────────────────────────┘
```

## Scan Results: `docker.io/rancher/hardened-calico:v3.32.1-build20260827`

```text

calicoctl (gobinary)
====================
Total: 1 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 1, CRITICAL: 0)

┌────────────────────────┬────────────────┬──────────┬────────┬───────────────────┬───────────────┬─────────────────────────────────────────────────────────────┐
│        Library         │ Vulnerability  │ Severity │ Status │ Installed Version │ Fixed Version │                            Title                            │
├────────────────────────┼────────────────┼──────────┼────────┼───────────────────┼───────────────┼─────────────────────────────────────────────────────────────┤
│ google.golang.org/grpc │ CVE-2026-84304 │ HIGH     │ fixed  │ v1.82.1           │ 1.83.1        │ gRPC-Go is the Go language implementation of gRPC. Prior to │
│                        │                │          │        │                   │               │ 1.83.1, in...                                               │
│                        │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-84304                  │
└────────────────────────┴────────────────┴──────────┴────────┴───────────────────┴───────────────┴─────────────────────────────────────────────────────────────┘

opt/cni/bin/calico (gobinary)
=============================
Total: 1 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 1, CRITICAL: 0)

┌────────────────────────┬────────────────┬──────────┬────────┬───────────────────┬───────────────┬─────────────────────────────────────────────────────────────┐
│        Library         │ Vulnerability  │ Severity │ Status │ Installed Version │ Fixed Version │                            Title                            │
├────────────────────────┼────────────────┼──────────┼────────┼───────────────────┼───────────────┼─────────────────────────────────────────────────────────────┤
│ google.golang.org/grpc │ CVE-2026-84304 │ HIGH     │ fixed  │ v1.82.1           │ 1.83.1        │ gRPC-Go is the Go language implementation of gRPC. Prior to │
│                        │                │          │        │                   │               │ 1.83.1, in...                                               │
│                        │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-84304                  │
└────────────────────────┴────────────────┴──────────┴────────┴───────────────────┴───────────────┴─────────────────────────────────────────────────────────────┘

opt/cni/bin/calico-ipam (gobinary)
==================================
Total: 1 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 1, CRITICAL: 0)

┌────────────────────────┬────────────────┬──────────┬────────┬───────────────────┬───────────────┬─────────────────────────────────────────────────────────────┐
│        Library         │ Vulnerability  │ Severity │ Status │ Installed Version │ Fixed Version │                            Title                            │
├────────────────────────┼────────────────┼──────────┼────────┼───────────────────┼───────────────┼─────────────────────────────────────────────────────────────┤
│ google.golang.org/grpc │ CVE-2026-84304 │ HIGH     │ fixed  │ v1.82.1           │ 1.83.1        │ gRPC-Go is the Go language implementation of gRPC. Prior to │
│                        │                │          │        │                   │               │ 1.83.1, in...                                               │
│                        │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-84304                  │
└────────────────────────┴────────────────┴──────────┴────────┴───────────────────┴───────────────┴─────────────────────────────────────────────────────────────┘

usr/bin/calico-node (gobinary)
==============================
Total: 1 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 1, CRITICAL: 0)

┌────────────────────────┬────────────────┬──────────┬────────┬───────────────────┬───────────────┬─────────────────────────────────────────────────────────────┐
│        Library         │ Vulnerability  │ Severity │ Status │ Installed Version │ Fixed Version │                            Title                            │
├────────────────────────┼────────────────┼──────────┼────────┼───────────────────┼───────────────┼─────────────────────────────────────────────────────────────┤
│ google.golang.org/grpc │ CVE-2026-84304 │ HIGH     │ fixed  │ v1.82.1           │ 1.83.1        │ gRPC-Go is the Go language implementation of gRPC. Prior to │
│                        │                │          │        │                   │               │ 1.83.1, in...                                               │
│                        │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-84304                  │
└────────────────────────┴────────────────┴──────────┴────────┴───────────────────┴───────────────┴─────────────────────────────────────────────────────────────┘

usr/bin/kube-controllers (gobinary)
===================================
Total: 1 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 1, CRITICAL: 0)

┌────────────────────────┬────────────────┬──────────┬────────┬───────────────────┬───────────────┬─────────────────────────────────────────────────────────────┐
│        Library         │ Vulnerability  │ Severity │ Status │ Installed Version │ Fixed Version │                            Title                            │
├────────────────────────┼────────────────┼──────────┼────────┼───────────────────┼───────────────┼─────────────────────────────────────────────────────────────┤
│ google.golang.org/grpc │ CVE-2026-84304 │ HIGH     │ fixed  │ v1.82.1           │ 1.83.1        │ gRPC-Go is the Go language implementation of gRPC. Prior to │
│                        │                │          │        │                   │               │ 1.83.1, in...                                               │
│                        │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-84304                  │
└────────────────────────┴────────────────┴──────────┴────────┴───────────────────┴───────────────┴─────────────────────────────────────────────────────────────┘
```

## Scan Results: `docker.io/rancher/hardened-flannel:v0.28.9-build20260819`

```text

opt/bin/flanneld (gobinary)
===========================
Total: 1 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 1, CRITICAL: 0)

┌────────────────────────┬────────────────┬──────────┬────────┬───────────────────┬───────────────┬─────────────────────────────────────────────────────────────┐
│        Library         │ Vulnerability  │ Severity │ Status │ Installed Version │ Fixed Version │                            Title                            │
├────────────────────────┼────────────────┼──────────┼────────┼───────────────────┼───────────────┼─────────────────────────────────────────────────────────────┤
│ google.golang.org/grpc │ CVE-2026-84304 │ HIGH     │ fixed  │ v1.82.1           │ 1.83.1        │ gRPC-Go is the Go language implementation of gRPC. Prior to │
│                        │                │          │        │                   │               │ 1.83.1, in...                                               │
│                        │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-84304                  │
└────────────────────────┴────────────────┴──────────┴────────┴───────────────────┴───────────────┴─────────────────────────────────────────────────────────────┘
```

## Summary

### CVEs by Severity

| Severity | Count |
| --- | ---: |
| CRITICAL | 4 |
| HIGH | 27 |
| **Total** | **31** |

### Images with CVEs (12)

| Image | CRITICAL | HIGH |
| --- | ---: | ---: |
| `docker.io/rancher/rke2-runtime:v1.37.0-rc1-rke2r1` | 0 | 6 |
| `docker.io/rancher/hardened-kubernetes:v1.37.0-rke2r1-build20260827` | 0 | 5 |
| `docker.io/rancher/hardened-coredns:v1.14.7-build20260819` | 0 | 1 |
| `docker.io/rancher/hardened-dns-node-cache:1.26.8-build20260819` | 0 | 1 |
| `docker.io/rancher/hardened-etcd:v3.7.1-k3s1-build20260901` | 0 | 2 |
| `docker.io/rancher/hardened-k8s-metrics-server:v0.9.0-build20260819` | 1 | 1 |
| `docker.io/rancher/klipper-helm:v0.13.3-build20260820` | 2 | 2 |
| `docker.io/rancher/rke2-cloud-provider:v1.35.1-0.20260817230842-2a1e2e8cf41b-build20260820` | 1 | 1 |
| `docker.io/rancher/hardened-snapshot-controller:v8.6.0-build20260819` | 0 | 1 |
| `docker.io/rancher/hardened-traefik:v3.7.11-build20260819` | 0 | 1 |
| `docker.io/rancher/hardened-calico:v3.32.1-build20260827` | 0 | 5 |
| `docker.io/rancher/hardened-flannel:v0.28.9-build20260819` | 0 | 1 |

### CVE-free Images (5)

- `docker.io/rancher/hardened-cluster-autoscaler:v1.10.3-build20260819`
- `docker.io/rancher/hardened-addon-resizer:1.8.23-build20260819`
- `docker.io/rancher/klipper-lb:v0.4.17`
- `docker.io/rancher/mirrored-pause:3.10.2`
- `docker.io/rancher/rke2-security-responder:v0.1.5`

