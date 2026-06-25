# Trivy Scan Report

<!-- scan-source-ref: release:v1.36.2+rke2r1 -->
<!-- scan-source-desc: release v1.36.2+rke2r1 -->
## Images Scanned

- `docker.io/rancher/rke2-runtime:v1.36.2-rke2r1`
- `docker.io/rancher/hardened-kubernetes:v1.36.2-rke2r1-build20260612`
- `docker.io/rancher/hardened-coredns:v1.14.4-build20260610`
- `docker.io/rancher/hardened-cluster-autoscaler:v1.10.3-build20260604`
- `docker.io/rancher/hardened-dns-node-cache:1.26.8-build20260608`
- `docker.io/rancher/hardened-etcd:v3.6.12-k3s1-build20260603`
- `docker.io/rancher/hardened-k8s-metrics-server:v0.8.1-build20260604`
- `docker.io/rancher/hardened-addon-resizer:1.8.23-build20260604`
- `docker.io/rancher/klipper-helm:v0.11.1-build20260615`
- `docker.io/rancher/klipper-lb:v0.4.17`
- `docker.io/rancher/mirrored-pause:3.6`
- `docker.io/rancher/rke2-cloud-provider:v1.36.1-0.20260508014929-7bbbf7c9b258-build20260515`
- `docker.io/rancher/hardened-snapshot-controller:v8.6.0-build20260608`
- `docker.io/rancher/hardened-traefik:v3.7.4-build20260608`
- `docker.io/rancher/hardened-calico:v3.32.0-build20260604`
- `docker.io/rancher/hardened-flannel:v0.28.5-build20260604`

## Scan Results: `docker.io/rancher/rke2-runtime:v1.36.2-rke2r1`

```text

bin/containerd (gobinary)
=========================
Total: 3 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 3, CRITICAL: 0)

┌─────────────────────────────────────┬────────────────┬──────────┬────────┬───────────────────┬─────────────────────────────┬───────────────────────────────────────────────────────────┐
│               Library               │ Vulnerability  │ Severity │ Status │ Installed Version │        Fixed Version        │                           Title                           │
├─────────────────────────────────────┼────────────────┼──────────┼────────┼───────────────────┼─────────────────────────────┼───────────────────────────────────────────────────────────┤
│ github.com/containerd/containerd/v2 │ CVE-2026-53488 │ HIGH     │ fixed  │ v2.3.2-k3s2       │ 2.0.10, 2.1.9, 2.2.5, 2.3.2 │ CVE-2026-53488 affecting package containerd2 for versions │
│                                     │                │          │        │                   │                             │ less than 2.2.4-3                                         │
│                                     │                │          │        │                   │                             │ https://avd.aquasec.com/nvd/cve-2026-53488                │
│                                     ├────────────────┤          │        │                   ├─────────────────────────────┼───────────────────────────────────────────────────────────┤
│                                     │ CVE-2026-53489 │          │        │                   │ 2.1.9, 2.2.5, 2.3.2         │ CVE-2026-53489 affecting package containerd2 for versions │
│                                     │                │          │        │                   │                             │ less than 2.2.4-3                                         │
│                                     │                │          │        │                   │                             │ https://avd.aquasec.com/nvd/cve-2026-53489                │
│                                     ├────────────────┤          │        │                   │                             ├───────────────────────────────────────────────────────────┤
│                                     │ CVE-2026-53492 │          │        │                   │                             │ CVE-2026-53492 affecting package containerd2 for versions │
│                                     │                │          │        │                   │                             │ less than 2.2.4-3                                         │
│                                     │                │          │        │                   │                             │ https://avd.aquasec.com/nvd/cve-2026-53492                │
└─────────────────────────────────────┴────────────────┴──────────┴────────┴───────────────────┴─────────────────────────────┴───────────────────────────────────────────────────────────┘

bin/containerd-shim-runc-v2 (gobinary)
======================================
Total: 3 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 3, CRITICAL: 0)

┌─────────────────────────────────────┬────────────────┬──────────┬────────┬───────────────────┬─────────────────────────────┬───────────────────────────────────────────────────────────┐
│               Library               │ Vulnerability  │ Severity │ Status │ Installed Version │        Fixed Version        │                           Title                           │
├─────────────────────────────────────┼────────────────┼──────────┼────────┼───────────────────┼─────────────────────────────┼───────────────────────────────────────────────────────────┤
│ github.com/containerd/containerd/v2 │ CVE-2026-53488 │ HIGH     │ fixed  │ v2.3.2-k3s2       │ 2.0.10, 2.1.9, 2.2.5, 2.3.2 │ CVE-2026-53488 affecting package containerd2 for versions │
│                                     │                │          │        │                   │                             │ less than 2.2.4-3                                         │
│                                     │                │          │        │                   │                             │ https://avd.aquasec.com/nvd/cve-2026-53488                │
│                                     ├────────────────┤          │        │                   ├─────────────────────────────┼───────────────────────────────────────────────────────────┤
│                                     │ CVE-2026-53489 │          │        │                   │ 2.1.9, 2.2.5, 2.3.2         │ CVE-2026-53489 affecting package containerd2 for versions │
│                                     │                │          │        │                   │                             │ less than 2.2.4-3                                         │
│                                     │                │          │        │                   │                             │ https://avd.aquasec.com/nvd/cve-2026-53489                │
│                                     ├────────────────┤          │        │                   │                             ├───────────────────────────────────────────────────────────┤
│                                     │ CVE-2026-53492 │          │        │                   │                             │ CVE-2026-53492 affecting package containerd2 for versions │
│                                     │                │          │        │                   │                             │ less than 2.2.4-3                                         │
│                                     │                │          │        │                   │                             │ https://avd.aquasec.com/nvd/cve-2026-53492                │
└─────────────────────────────────────┴────────────────┴──────────┴────────┴───────────────────┴─────────────────────────────┴───────────────────────────────────────────────────────────┘

bin/crictl (gobinary)
=====================
Total: 1 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 1, CRITICAL: 0)

┌──────────────────┬────────────────┬──────────┬────────┬───────────────────┬───────────────┬───────────────────────────────────────────────────────┐
│     Library      │ Vulnerability  │ Severity │ Status │ Installed Version │ Fixed Version │                         Title                         │
├──────────────────┼────────────────┼──────────┼────────┼───────────────────┼───────────────┼───────────────────────────────────────────────────────┤
│ golang.org/x/net │ CVE-2026-33814 │ HIGH     │ fixed  │ v0.51.0           │ 0.53.0        │ net/http/internal/http2: golang: golang.org/x/net: Go │
│                  │                │          │        │                   │               │ HTTP/2: Denial of Service via malformed               │
│                  │                │          │        │                   │               │ SETTINGS_MAX_FRAME_SIZE frame...                      │
│                  │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-33814            │
└──────────────────┴────────────────┴──────────┴────────┴───────────────────┴───────────────┴───────────────────────────────────────────────────────┘

bin/ctr (gobinary)
==================
Total: 3 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 3, CRITICAL: 0)

┌─────────────────────────────────────┬────────────────┬──────────┬────────┬───────────────────┬─────────────────────────────┬───────────────────────────────────────────────────────────┐
│               Library               │ Vulnerability  │ Severity │ Status │ Installed Version │        Fixed Version        │                           Title                           │
├─────────────────────────────────────┼────────────────┼──────────┼────────┼───────────────────┼─────────────────────────────┼───────────────────────────────────────────────────────────┤
│ github.com/containerd/containerd/v2 │ CVE-2026-53488 │ HIGH     │ fixed  │ v2.3.2-k3s2       │ 2.0.10, 2.1.9, 2.2.5, 2.3.2 │ CVE-2026-53488 affecting package containerd2 for versions │
│                                     │                │          │        │                   │                             │ less than 2.2.4-3                                         │
│                                     │                │          │        │                   │                             │ https://avd.aquasec.com/nvd/cve-2026-53488                │
│                                     ├────────────────┤          │        │                   ├─────────────────────────────┼───────────────────────────────────────────────────────────┤
│                                     │ CVE-2026-53489 │          │        │                   │ 2.1.9, 2.2.5, 2.3.2         │ CVE-2026-53489 affecting package containerd2 for versions │
│                                     │                │          │        │                   │                             │ less than 2.2.4-3                                         │
│                                     │                │          │        │                   │                             │ https://avd.aquasec.com/nvd/cve-2026-53489                │
│                                     ├────────────────┤          │        │                   │                             ├───────────────────────────────────────────────────────────┤
│                                     │ CVE-2026-53492 │          │        │                   │                             │ CVE-2026-53492 affecting package containerd2 for versions │
│                                     │                │          │        │                   │                             │ less than 2.2.4-3                                         │
│                                     │                │          │        │                   │                             │ https://avd.aquasec.com/nvd/cve-2026-53492                │
└─────────────────────────────────────┴────────────────┴──────────┴────────┴───────────────────┴─────────────────────────────┴───────────────────────────────────────────────────────────┘

bin/kubectl (gobinary)
======================
Total: 2 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 2, CRITICAL: 0)

┌──────────────────┬────────────────┬──────────┬────────┬───────────────────┬───────────────┬──────────────────────────────────────────────────────────────┐
│     Library      │ Vulnerability  │ Severity │ Status │ Installed Version │ Fixed Version │                            Title                             │
├──────────────────┼────────────────┼──────────┼────────┼───────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ golang.org/x/net │ CVE-2026-33814 │ HIGH     │ fixed  │ v0.49.0           │ 0.53.0        │ net/http/internal/http2: golang: golang.org/x/net: Go        │
│                  │                │          │        │                   │               │ HTTP/2: Denial of Service via malformed                      │
│                  │                │          │        │                   │               │ SETTINGS_MAX_FRAME_SIZE frame...                             │
│                  │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-33814                   │
│                  ├────────────────┤          │        │                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                  │ CVE-2026-39821 │          │        │                   │ 0.55.0        │ golang.org/x/net/idna: golang: golang.org/x/net/idna:        │
│                  │                │          │        │                   │               │ Privilege escalation via incorrect Punycode label processing │
│                  │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-39821                   │
└──────────────────┴────────────────┴──────────┴────────┴───────────────────┴───────────────┴──────────────────────────────────────────────────────────────┘

bin/kubelet (gobinary)
======================
Total: 2 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 2, CRITICAL: 0)

┌──────────────────┬────────────────┬──────────┬────────┬───────────────────┬───────────────┬──────────────────────────────────────────────────────────────┐
│     Library      │ Vulnerability  │ Severity │ Status │ Installed Version │ Fixed Version │                            Title                             │
├──────────────────┼────────────────┼──────────┼────────┼───────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ golang.org/x/net │ CVE-2026-33814 │ HIGH     │ fixed  │ v0.49.0           │ 0.53.0        │ net/http/internal/http2: golang: golang.org/x/net: Go        │
│                  │                │          │        │                   │               │ HTTP/2: Denial of Service via malformed                      │
│                  │                │          │        │                   │               │ SETTINGS_MAX_FRAME_SIZE frame...                             │
│                  │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-33814                   │
│                  ├────────────────┤          │        │                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                  │ CVE-2026-39821 │          │        │                   │ 0.55.0        │ golang.org/x/net/idna: golang: golang.org/x/net/idna:        │
│                  │                │          │        │                   │               │ Privilege escalation via incorrect Punycode label processing │
│                  │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-39821                   │
└──────────────────┴────────────────┴──────────┴────────┴───────────────────┴───────────────┴──────────────────────────────────────────────────────────────┘
```

## Scan Results: `docker.io/rancher/hardened-kubernetes:v1.36.2-rke2r1-build20260612`

```text

usr/local/bin/kube-apiserver (gobinary)
=======================================
Total: 2 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 2, CRITICAL: 0)

┌──────────────────┬────────────────┬──────────┬────────┬───────────────────┬───────────────┬──────────────────────────────────────────────────────────────┐
│     Library      │ Vulnerability  │ Severity │ Status │ Installed Version │ Fixed Version │                            Title                             │
├──────────────────┼────────────────┼──────────┼────────┼───────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ golang.org/x/net │ CVE-2026-33814 │ HIGH     │ fixed  │ v0.49.0           │ 0.53.0        │ net/http/internal/http2: golang: golang.org/x/net: Go        │
│                  │                │          │        │                   │               │ HTTP/2: Denial of Service via malformed                      │
│                  │                │          │        │                   │               │ SETTINGS_MAX_FRAME_SIZE frame...                             │
│                  │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-33814                   │
│                  ├────────────────┤          │        │                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                  │ CVE-2026-39821 │          │        │                   │ 0.55.0        │ golang.org/x/net/idna: golang: golang.org/x/net/idna:        │
│                  │                │          │        │                   │               │ Privilege escalation via incorrect Punycode label processing │
│                  │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-39821                   │
└──────────────────┴────────────────┴──────────┴────────┴───────────────────┴───────────────┴──────────────────────────────────────────────────────────────┘

usr/local/bin/kube-controller-manager (gobinary)
================================================
Total: 2 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 2, CRITICAL: 0)

┌──────────────────┬────────────────┬──────────┬────────┬───────────────────┬───────────────┬──────────────────────────────────────────────────────────────┐
│     Library      │ Vulnerability  │ Severity │ Status │ Installed Version │ Fixed Version │                            Title                             │
├──────────────────┼────────────────┼──────────┼────────┼───────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ golang.org/x/net │ CVE-2026-33814 │ HIGH     │ fixed  │ v0.49.0           │ 0.53.0        │ net/http/internal/http2: golang: golang.org/x/net: Go        │
│                  │                │          │        │                   │               │ HTTP/2: Denial of Service via malformed                      │
│                  │                │          │        │                   │               │ SETTINGS_MAX_FRAME_SIZE frame...                             │
│                  │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-33814                   │
│                  ├────────────────┤          │        │                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                  │ CVE-2026-39821 │          │        │                   │ 0.55.0        │ golang.org/x/net/idna: golang: golang.org/x/net/idna:        │
│                  │                │          │        │                   │               │ Privilege escalation via incorrect Punycode label processing │
│                  │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-39821                   │
└──────────────────┴────────────────┴──────────┴────────┴───────────────────┴───────────────┴──────────────────────────────────────────────────────────────┘

usr/local/bin/kube-proxy (gobinary)
===================================
Total: 2 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 2, CRITICAL: 0)

┌──────────────────┬────────────────┬──────────┬────────┬───────────────────┬───────────────┬──────────────────────────────────────────────────────────────┐
│     Library      │ Vulnerability  │ Severity │ Status │ Installed Version │ Fixed Version │                            Title                             │
├──────────────────┼────────────────┼──────────┼────────┼───────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ golang.org/x/net │ CVE-2026-33814 │ HIGH     │ fixed  │ v0.49.0           │ 0.53.0        │ net/http/internal/http2: golang: golang.org/x/net: Go        │
│                  │                │          │        │                   │               │ HTTP/2: Denial of Service via malformed                      │
│                  │                │          │        │                   │               │ SETTINGS_MAX_FRAME_SIZE frame...                             │
│                  │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-33814                   │
│                  ├────────────────┤          │        │                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                  │ CVE-2026-39821 │          │        │                   │ 0.55.0        │ golang.org/x/net/idna: golang: golang.org/x/net/idna:        │
│                  │                │          │        │                   │               │ Privilege escalation via incorrect Punycode label processing │
│                  │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-39821                   │
└──────────────────┴────────────────┴──────────┴────────┴───────────────────┴───────────────┴──────────────────────────────────────────────────────────────┘

usr/local/bin/kube-scheduler (gobinary)
=======================================
Total: 2 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 2, CRITICAL: 0)

┌──────────────────┬────────────────┬──────────┬────────┬───────────────────┬───────────────┬──────────────────────────────────────────────────────────────┐
│     Library      │ Vulnerability  │ Severity │ Status │ Installed Version │ Fixed Version │                            Title                             │
├──────────────────┼────────────────┼──────────┼────────┼───────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ golang.org/x/net │ CVE-2026-33814 │ HIGH     │ fixed  │ v0.49.0           │ 0.53.0        │ net/http/internal/http2: golang: golang.org/x/net: Go        │
│                  │                │          │        │                   │               │ HTTP/2: Denial of Service via malformed                      │
│                  │                │          │        │                   │               │ SETTINGS_MAX_FRAME_SIZE frame...                             │
│                  │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-33814                   │
│                  ├────────────────┤          │        │                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                  │ CVE-2026-39821 │          │        │                   │ 0.55.0        │ golang.org/x/net/idna: golang: golang.org/x/net/idna:        │
│                  │                │          │        │                   │               │ Privilege escalation via incorrect Punycode label processing │
│                  │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-39821                   │
└──────────────────┴────────────────┴──────────┴────────┴───────────────────┴───────────────┴──────────────────────────────────────────────────────────────┘

usr/local/bin/kubectl (gobinary)
================================
Total: 2 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 2, CRITICAL: 0)

┌──────────────────┬────────────────┬──────────┬────────┬───────────────────┬───────────────┬──────────────────────────────────────────────────────────────┐
│     Library      │ Vulnerability  │ Severity │ Status │ Installed Version │ Fixed Version │                            Title                             │
├──────────────────┼────────────────┼──────────┼────────┼───────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ golang.org/x/net │ CVE-2026-33814 │ HIGH     │ fixed  │ v0.49.0           │ 0.53.0        │ net/http/internal/http2: golang: golang.org/x/net: Go        │
│                  │                │          │        │                   │               │ HTTP/2: Denial of Service via malformed                      │
│                  │                │          │        │                   │               │ SETTINGS_MAX_FRAME_SIZE frame...                             │
│                  │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-33814                   │
│                  ├────────────────┤          │        │                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                  │ CVE-2026-39821 │          │        │                   │ 0.55.0        │ golang.org/x/net/idna: golang: golang.org/x/net/idna:        │
│                  │                │          │        │                   │               │ Privilege escalation via incorrect Punycode label processing │
│                  │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-39821                   │
└──────────────────┴────────────────┴──────────┴────────┴───────────────────┴───────────────┴──────────────────────────────────────────────────────────────┘

usr/local/bin/kubelet (gobinary)
================================
Total: 2 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 2, CRITICAL: 0)

┌──────────────────┬────────────────┬──────────┬────────┬───────────────────┬───────────────┬──────────────────────────────────────────────────────────────┐
│     Library      │ Vulnerability  │ Severity │ Status │ Installed Version │ Fixed Version │                            Title                             │
├──────────────────┼────────────────┼──────────┼────────┼───────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ golang.org/x/net │ CVE-2026-33814 │ HIGH     │ fixed  │ v0.49.0           │ 0.53.0        │ net/http/internal/http2: golang: golang.org/x/net: Go        │
│                  │                │          │        │                   │               │ HTTP/2: Denial of Service via malformed                      │
│                  │                │          │        │                   │               │ SETTINGS_MAX_FRAME_SIZE frame...                             │
│                  │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-33814                   │
│                  ├────────────────┤          │        │                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                  │ CVE-2026-39821 │          │        │                   │ 0.55.0        │ golang.org/x/net/idna: golang: golang.org/x/net/idna:        │
│                  │                │          │        │                   │               │ Privilege escalation via incorrect Punycode label processing │
│                  │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-39821                   │
└──────────────────┴────────────────┴──────────┴────────┴───────────────────┴───────────────┴──────────────────────────────────────────────────────────────┘
```

## Scan Results: `docker.io/rancher/hardened-coredns:v1.14.4-build20260610`

```text
```

## Scan Results: `docker.io/rancher/hardened-cluster-autoscaler:v1.10.3-build20260604`

```text

cluster-proportional-autoscaler (gobinary)
==========================================
Total: 2 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 2, CRITICAL: 0)

┌──────────────────┬────────────────┬──────────┬────────┬───────────────────┬───────────────┬──────────────────────────────────────────────────────────────┐
│     Library      │ Vulnerability  │ Severity │ Status │ Installed Version │ Fixed Version │                            Title                             │
├──────────────────┼────────────────┼──────────┼────────┼───────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ golang.org/x/net │ CVE-2026-33814 │ HIGH     │ fixed  │ v0.36.0           │ 0.53.0        │ net/http/internal/http2: golang: golang.org/x/net: Go        │
│                  │                │          │        │                   │               │ HTTP/2: Denial of Service via malformed                      │
│                  │                │          │        │                   │               │ SETTINGS_MAX_FRAME_SIZE frame...                             │
│                  │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-33814                   │
│                  ├────────────────┤          │        │                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                  │ CVE-2026-39821 │          │        │                   │ 0.55.0        │ golang.org/x/net/idna: golang: golang.org/x/net/idna:        │
│                  │                │          │        │                   │               │ Privilege escalation via incorrect Punycode label processing │
│                  │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-39821                   │
└──────────────────┴────────────────┴──────────┴────────┴───────────────────┴───────────────┴──────────────────────────────────────────────────────────────┘
```

## Scan Results: `docker.io/rancher/hardened-dns-node-cache:1.26.8-build20260608`

```text

node-cache (gobinary)
=====================
Total: 2 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 2, CRITICAL: 0)

┌──────────────────┬────────────────┬──────────┬────────┬───────────────────┬───────────────┬──────────────────────────────────────────────────────────────┐
│     Library      │ Vulnerability  │ Severity │ Status │ Installed Version │ Fixed Version │                            Title                             │
├──────────────────┼────────────────┼──────────┼────────┼───────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ golang.org/x/net │ CVE-2026-33814 │ HIGH     │ fixed  │ v0.52.0           │ 0.53.0        │ net/http/internal/http2: golang: golang.org/x/net: Go        │
│                  │                │          │        │                   │               │ HTTP/2: Denial of Service via malformed                      │
│                  │                │          │        │                   │               │ SETTINGS_MAX_FRAME_SIZE frame...                             │
│                  │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-33814                   │
│                  ├────────────────┤          │        │                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                  │ CVE-2026-39821 │          │        │                   │ 0.55.0        │ golang.org/x/net/idna: golang: golang.org/x/net/idna:        │
│                  │                │          │        │                   │               │ Privilege escalation via incorrect Punycode label processing │
│                  │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-39821                   │
└──────────────────┴────────────────┴──────────┴────────┴───────────────────┴───────────────┴──────────────────────────────────────────────────────────────┘
```

## Scan Results: `docker.io/rancher/hardened-etcd:v3.6.12-k3s1-build20260603`

```text
```

## Scan Results: `docker.io/rancher/hardened-k8s-metrics-server:v0.8.1-build20260604`

```text

metrics-server (gobinary)
=========================
Total: 2 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 2, CRITICAL: 0)

┌──────────────────┬────────────────┬──────────┬────────┬───────────────────┬───────────────┬──────────────────────────────────────────────────────────────┐
│     Library      │ Vulnerability  │ Severity │ Status │ Installed Version │ Fixed Version │                            Title                             │
├──────────────────┼────────────────┼──────────┼────────┼───────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ golang.org/x/net │ CVE-2026-33814 │ HIGH     │ fixed  │ v0.52.0           │ 0.53.0        │ net/http/internal/http2: golang: golang.org/x/net: Go        │
│                  │                │          │        │                   │               │ HTTP/2: Denial of Service via malformed                      │
│                  │                │          │        │                   │               │ SETTINGS_MAX_FRAME_SIZE frame...                             │
│                  │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-33814                   │
│                  ├────────────────┤          │        │                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                  │ CVE-2026-39821 │          │        │                   │ 0.55.0        │ golang.org/x/net/idna: golang: golang.org/x/net/idna:        │
│                  │                │          │        │                   │               │ Privilege escalation via incorrect Punycode label processing │
│                  │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-39821                   │
└──────────────────┴────────────────┴──────────┴────────┴───────────────────┴───────────────┴──────────────────────────────────────────────────────────────┘
```

## Scan Results: `docker.io/rancher/hardened-addon-resizer:1.8.23-build20260604`

```text

pod_nanny (gobinary)
====================
Total: 2 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 2, CRITICAL: 0)

┌──────────────────┬────────────────┬──────────┬────────┬───────────────────┬───────────────┬──────────────────────────────────────────────────────────────┐
│     Library      │ Vulnerability  │ Severity │ Status │ Installed Version │ Fixed Version │                            Title                             │
├──────────────────┼────────────────┼──────────┼────────┼───────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ golang.org/x/net │ CVE-2026-33814 │ HIGH     │ fixed  │ v0.33.0           │ 0.53.0        │ net/http/internal/http2: golang: golang.org/x/net: Go        │
│                  │                │          │        │                   │               │ HTTP/2: Denial of Service via malformed                      │
│                  │                │          │        │                   │               │ SETTINGS_MAX_FRAME_SIZE frame...                             │
│                  │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-33814                   │
│                  ├────────────────┤          │        │                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                  │ CVE-2026-39821 │          │        │                   │ 0.55.0        │ golang.org/x/net/idna: golang: golang.org/x/net/idna:        │
│                  │                │          │        │                   │               │ Privilege escalation via incorrect Punycode label processing │
│                  │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-39821                   │
└──────────────────┴────────────────┴──────────┴────────┴───────────────────┴───────────────┴──────────────────────────────────────────────────────────────┘
```

## Scan Results: `docker.io/rancher/klipper-helm:v0.11.1-build20260615`

```text

home/klipper-helm/.local/share/helm/plugins/helm-mapkubeapis/bin/mapkubeapis (gobinary)
=======================================================================================
Total: 2 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 2, CRITICAL: 0)

┌──────────────────┬────────────────┬──────────┬────────┬───────────────────┬───────────────┬──────────────────────────────────────────────────────────────┐
│     Library      │ Vulnerability  │ Severity │ Status │ Installed Version │ Fixed Version │                            Title                             │
├──────────────────┼────────────────┼──────────┼────────┼───────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ golang.org/x/net │ CVE-2026-33814 │ HIGH     │ fixed  │ v0.49.0           │ 0.53.0        │ net/http/internal/http2: golang: golang.org/x/net: Go        │
│                  │                │          │        │                   │               │ HTTP/2: Denial of Service via malformed                      │
│                  │                │          │        │                   │               │ SETTINGS_MAX_FRAME_SIZE frame...                             │
│                  │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-33814                   │
│                  ├────────────────┤          │        │                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                  │ CVE-2026-39821 │          │        │                   │ 0.55.0        │ golang.org/x/net/idna: golang: golang.org/x/net/idna:        │
│                  │                │          │        │                   │               │ Privilege escalation via incorrect Punycode label processing │
│                  │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-39821                   │
└──────────────────┴────────────────┴──────────┴────────┴───────────────────┴───────────────┴──────────────────────────────────────────────────────────────┘

home/klipper-helm/.local/share/helm/plugins/helm-set-status/helm-set-status (gobinary)
======================================================================================
Total: 2 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 2, CRITICAL: 0)

┌──────────────────┬────────────────┬──────────┬────────┬───────────────────┬───────────────┬──────────────────────────────────────────────────────────────┐
│     Library      │ Vulnerability  │ Severity │ Status │ Installed Version │ Fixed Version │                            Title                             │
├──────────────────┼────────────────┼──────────┼────────┼───────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ golang.org/x/net │ CVE-2026-33814 │ HIGH     │ fixed  │ v0.49.0           │ 0.53.0        │ net/http/internal/http2: golang: golang.org/x/net: Go        │
│                  │                │          │        │                   │               │ HTTP/2: Denial of Service via malformed                      │
│                  │                │          │        │                   │               │ SETTINGS_MAX_FRAME_SIZE frame...                             │
│                  │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-33814                   │
│                  ├────────────────┤          │        │                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                  │ CVE-2026-39821 │          │        │                   │ 0.55.0        │ golang.org/x/net/idna: golang: golang.org/x/net/idna:        │
│                  │                │          │        │                   │               │ Privilege escalation via incorrect Punycode label processing │
│                  │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-39821                   │
└──────────────────┴────────────────┴──────────┴────────┴───────────────────┴───────────────┴──────────────────────────────────────────────────────────────┘

usr/bin/helm (gobinary)
=======================
Total: 2 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 2, CRITICAL: 0)

┌──────────────────┬────────────────┬──────────┬────────┬───────────────────┬───────────────┬──────────────────────────────────────────────────────────────┐
│     Library      │ Vulnerability  │ Severity │ Status │ Installed Version │ Fixed Version │                            Title                             │
├──────────────────┼────────────────┼──────────┼────────┼───────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ golang.org/x/net │ CVE-2026-33814 │ HIGH     │ fixed  │ v0.49.0           │ 0.53.0        │ net/http/internal/http2: golang: golang.org/x/net: Go        │
│                  │                │          │        │                   │               │ HTTP/2: Denial of Service via malformed                      │
│                  │                │          │        │                   │               │ SETTINGS_MAX_FRAME_SIZE frame...                             │
│                  │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-33814                   │
│                  ├────────────────┤          │        │                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                  │ CVE-2026-39821 │          │        │                   │ 0.55.0        │ golang.org/x/net/idna: golang: golang.org/x/net/idna:        │
│                  │                │          │        │                   │               │ Privilege escalation via incorrect Punycode label processing │
│                  │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-39821                   │
└──────────────────┴────────────────┴──────────┴────────┴───────────────────┴───────────────┴──────────────────────────────────────────────────────────────┘
```

## Scan Results: `docker.io/rancher/klipper-lb:v0.4.17`

```text
```

## Scan Results: `docker.io/rancher/mirrored-pause:3.6`

```text
```

## Scan Results: `docker.io/rancher/rke2-cloud-provider:v1.36.1-0.20260508014929-7bbbf7c9b258-build20260515`

```text

usr/local/bin/rke2-cloud-provider (gobinary)
============================================
Total: 2 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 2, CRITICAL: 0)

┌──────────────────┬────────────────┬──────────┬────────┬───────────────────┬─────────────────┬──────────────────────────────────────────────────────────────┐
│     Library      │ Vulnerability  │ Severity │ Status │ Installed Version │  Fixed Version  │                            Title                             │
├──────────────────┼────────────────┼──────────┼────────┼───────────────────┼─────────────────┼──────────────────────────────────────────────────────────────┤
│ golang.org/x/net │ CVE-2026-39821 │ HIGH     │ fixed  │ v0.53.0           │ 0.55.0          │ golang.org/x/net/idna: golang: golang.org/x/net/idna:        │
│                  │                │          │        │                   │                 │ Privilege escalation via incorrect Punycode label processing │
│                  │                │          │        │                   │                 │ https://avd.aquasec.com/nvd/cve-2026-39821                   │
├──────────────────┼────────────────┤          │        ├───────────────────┼─────────────────┼──────────────────────────────────────────────────────────────┤
│ stdlib           │ CVE-2026-27145 │          │        │ v1.26.3           │ 1.25.11, 1.26.4 │ *x509.Certificate).VerifyHostname previously called          │
│                  │                │          │        │                   │                 │ matchHostnames in ...                                        │
│                  │                │          │        │                   │                 │ https://avd.aquasec.com/nvd/cve-2026-27145                   │
└──────────────────┴────────────────┴──────────┴────────┴───────────────────┴─────────────────┴──────────────────────────────────────────────────────────────┘
```

## Scan Results: `docker.io/rancher/hardened-snapshot-controller:v8.6.0-build20260608`

```text

snapshot-controller (gobinary)
==============================
Total: 1 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 1, CRITICAL: 0)

┌──────────────────┬────────────────┬──────────┬────────┬───────────────────┬───────────────┬──────────────────────────────────────────────────────────────┐
│     Library      │ Vulnerability  │ Severity │ Status │ Installed Version │ Fixed Version │                            Title                             │
├──────────────────┼────────────────┼──────────┼────────┼───────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ golang.org/x/net │ CVE-2026-39821 │ HIGH     │ fixed  │ v0.54.0           │ 0.55.0        │ golang.org/x/net/idna: golang: golang.org/x/net/idna:        │
│                  │                │          │        │                   │               │ Privilege escalation via incorrect Punycode label processing │
│                  │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-39821                   │
└──────────────────┴────────────────┴──────────┴────────┴───────────────────┴───────────────┴──────────────────────────────────────────────────────────────┘
```

## Scan Results: `docker.io/rancher/hardened-traefik:v3.7.4-build20260608`

```text
```

## Scan Results: `docker.io/rancher/hardened-calico:v3.32.0-build20260604`

```text
```

## Scan Results: `docker.io/rancher/hardened-flannel:v0.28.5-build20260604`

```text

opt/bin/flanneld (gobinary)
===========================
Total: 2 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 2, CRITICAL: 0)

┌──────────────────┬────────────────┬──────────┬────────┬───────────────────┬───────────────┬──────────────────────────────────────────────────────────────┐
│     Library      │ Vulnerability  │ Severity │ Status │ Installed Version │ Fixed Version │                            Title                             │
├──────────────────┼────────────────┼──────────┼────────┼───────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ golang.org/x/net │ CVE-2026-33814 │ HIGH     │ fixed  │ v0.52.0           │ 0.53.0        │ net/http/internal/http2: golang: golang.org/x/net: Go        │
│                  │                │          │        │                   │               │ HTTP/2: Denial of Service via malformed                      │
│                  │                │          │        │                   │               │ SETTINGS_MAX_FRAME_SIZE frame...                             │
│                  │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-33814                   │
│                  ├────────────────┤          │        │                   ├───────────────┼──────────────────────────────────────────────────────────────┤
│                  │ CVE-2026-39821 │          │        │                   │ 0.55.0        │ golang.org/x/net/idna: golang: golang.org/x/net/idna:        │
│                  │                │          │        │                   │               │ Privilege escalation via incorrect Punycode label processing │
│                  │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-39821                   │
└──────────────────┴────────────────┴──────────┴────────┴───────────────────┴───────────────┴──────────────────────────────────────────────────────────────┘
```

## Summary

### CVEs by Severity

| Severity | Count |
| --- | ---: |
| CRITICAL | 0 |
| HIGH | 45 |
| **Total** | **45** |

### Images with CVEs (10)

| Image | CRITICAL | HIGH |
| --- | ---: | ---: |
| `docker.io/rancher/rke2-runtime:v1.36.2-rke2r1` | 0 | 14 |
| `docker.io/rancher/hardened-kubernetes:v1.36.2-rke2r1-build20260612` | 0 | 12 |
| `docker.io/rancher/hardened-cluster-autoscaler:v1.10.3-build20260604` | 0 | 2 |
| `docker.io/rancher/hardened-dns-node-cache:1.26.8-build20260608` | 0 | 2 |
| `docker.io/rancher/hardened-k8s-metrics-server:v0.8.1-build20260604` | 0 | 2 |
| `docker.io/rancher/hardened-addon-resizer:1.8.23-build20260604` | 0 | 2 |
| `docker.io/rancher/klipper-helm:v0.11.1-build20260615` | 0 | 6 |
| `docker.io/rancher/rke2-cloud-provider:v1.36.1-0.20260508014929-7bbbf7c9b258-build20260515` | 0 | 2 |
| `docker.io/rancher/hardened-snapshot-controller:v8.6.0-build20260608` | 0 | 1 |
| `docker.io/rancher/hardened-flannel:v0.28.5-build20260604` | 0 | 2 |

### CVE-free Images (6)

- `docker.io/rancher/hardened-coredns:v1.14.4-build20260610`
- `docker.io/rancher/hardened-etcd:v3.6.12-k3s1-build20260603`
- `docker.io/rancher/klipper-lb:v0.4.17`
- `docker.io/rancher/mirrored-pause:3.6`
- `docker.io/rancher/hardened-traefik:v3.7.4-build20260608`
- `docker.io/rancher/hardened-calico:v3.32.0-build20260604`

