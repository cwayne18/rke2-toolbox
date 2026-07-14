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
Total: 3 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 3, CRITICAL: 0)

┌──────────────────┬────────────────┬──────────┬────────┬───────────────────┬──────────────────────────────┬──────────────────────────────────────────────────────────────┐
│     Library      │ Vulnerability  │ Severity │ Status │ Installed Version │        Fixed Version         │                            Title                             │
├──────────────────┼────────────────┼──────────┼────────┼───────────────────┼──────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ golang.org/x/net │ CVE-2026-33814 │ HIGH     │ fixed  │ v0.49.0           │ 0.53.0                       │ net/http/internal/http2: golang: golang.org/x/net: Go        │
│                  │                │          │        │                   │                              │ HTTP/2: Denial of Service via malformed                      │
│                  │                │          │        │                   │                              │ SETTINGS_MAX_FRAME_SIZE frame...                             │
│                  │                │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-33814                   │
│                  ├────────────────┤          │        │                   ├──────────────────────────────┼──────────────────────────────────────────────────────────────┤
│                  │ CVE-2026-39821 │          │        │                   │ 0.55.0                       │ golang.org/x/net/idna: golang: golang.org/x/net/idna:        │
│                  │                │          │        │                   │                              │ Privilege escalation via incorrect Punycode label processing │
│                  │                │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-39821                   │
├──────────────────┼────────────────┤          │        ├───────────────────┼──────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ stdlib           │ CVE-2026-39822 │          │        │ v1.25.11          │ 1.25.12, 1.26.5, 1.27.0-rc.2 │ os: golang: Go os.Root: Symlink following vulnerability      │
│                  │                │          │        │                   │                              │ allows directory traversal                                   │
│                  │                │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-39822                   │
└──────────────────┴────────────────┴──────────┴────────┴───────────────────┴──────────────────────────────┴──────────────────────────────────────────────────────────────┘

usr/bin/helm (gobinary)
=======================
Total: 3 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 3, CRITICAL: 0)

┌──────────────────┬────────────────┬──────────┬────────┬───────────────────┬──────────────────────────────┬──────────────────────────────────────────────────────────────┐
│     Library      │ Vulnerability  │ Severity │ Status │ Installed Version │        Fixed Version         │                            Title                             │
├──────────────────┼────────────────┼──────────┼────────┼───────────────────┼──────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ golang.org/x/net │ CVE-2026-33814 │ HIGH     │ fixed  │ v0.49.0           │ 0.53.0                       │ net/http/internal/http2: golang: golang.org/x/net: Go        │
│                  │                │          │        │                   │                              │ HTTP/2: Denial of Service via malformed                      │
│                  │                │          │        │                   │                              │ SETTINGS_MAX_FRAME_SIZE frame...                             │
│                  │                │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-33814                   │
│                  ├────────────────┤          │        │                   ├──────────────────────────────┼──────────────────────────────────────────────────────────────┤
│                  │ CVE-2026-39821 │          │        │                   │ 0.55.0                       │ golang.org/x/net/idna: golang: golang.org/x/net/idna:        │
│                  │                │          │        │                   │                              │ Privilege escalation via incorrect Punycode label processing │
│                  │                │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-39821                   │
├──────────────────┼────────────────┤          │        ├───────────────────┼──────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ stdlib           │ CVE-2026-39822 │          │        │ v1.25.11          │ 1.25.12, 1.26.5, 1.27.0-rc.2 │ os: golang: Go os.Root: Symlink following vulnerability      │
│                  │                │          │        │                   │                              │ allows directory traversal                                   │
│                  │                │          │        │                   │                              │ https://avd.aquasec.com/nvd/cve-2026-39822                   │
└──────────────────┴────────────────┴──────────┴────────┴───────────────────┴──────────────────────────────┴──────────────────────────────────────────────────────────────┘
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
Total: 1 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 1, CRITICAL: 0)

┌──────────────────┬────────────────┬──────────┬────────┬───────────────────┬───────────────┬──────────────────────────────────────────────────────────────┐
│     Library      │ Vulnerability  │ Severity │ Status │ Installed Version │ Fixed Version │                            Title                             │
├──────────────────┼────────────────┼──────────┼────────┼───────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ golang.org/x/net │ CVE-2026-39821 │ HIGH     │ fixed  │ v0.53.0           │ 0.55.0        │ golang.org/x/net/idna: golang: golang.org/x/net/idna:        │
│                  │                │          │        │                   │               │ Privilege escalation via incorrect Punycode label processing │
│                  │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-39821                   │
└──────────────────┴────────────────┴──────────┴────────┴───────────────────┴───────────────┴──────────────────────────────────────────────────────────────┘
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

docker.io/rancher/hardened-calico:v3.32.0-build20260604 (sles 15.7)
===================================================================
Total: 3 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 3, CRITICAL: 0)

┌────────────────────────────┬─────────────────────┬──────────┬────────┬───────────────────────┬───────────────────────┬─────────────────────────────────────┐
│          Library           │    Vulnerability    │ Severity │ Status │   Installed Version   │     Fixed Version     │                Title                │
├────────────────────────────┼─────────────────────┼──────────┼────────┼───────────────────────┼───────────────────────┼─────────────────────────────────────┤
│ krb5                       │ SUSE-SU-2026:2848-1 │ HIGH     │ fixed  │ 1.20.1-150600.11.14.1 │ 1.20.1-150600.11.19.1 │ Security update for krb5, krb5-mini │
├────────────────────────────┼─────────────────────┤          │        ├───────────────────────┼───────────────────────┼─────────────────────────────────────┤
│ libopenssl-3-fips-provider │ SUSE-SU-2026:2648-1 │          │        │ 3.2.3-150700.5.31.1   │ 3.2.3-150700.5.36.1   │ Security update for openssl-3       │
├────────────────────────────┤                     │          │        │                       │                       │                                     │
│ libopenssl3                │                     │          │        │                       │                       │                                     │
└────────────────────────────┴─────────────────────┴──────────┴────────┴───────────────────────┴───────────────────────┴─────────────────────────────────────┘
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
| HIGH | 39 |
| **Total** | **39** |

### Images with CVEs (11)

| Image | CRITICAL | HIGH |
| --- | ---: | ---: |
| `docker.io/rancher/rke2-runtime:v1.36.2-rke2r1` | 0 | 4 |
| `docker.io/rancher/hardened-kubernetes:v1.36.2-rke2r1-build20260612` | 0 | 12 |
| `docker.io/rancher/hardened-cluster-autoscaler:v1.10.3-build20260604` | 0 | 2 |
| `docker.io/rancher/hardened-dns-node-cache:1.26.8-build20260608` | 0 | 2 |
| `docker.io/rancher/hardened-k8s-metrics-server:v0.8.1-build20260604` | 0 | 2 |
| `docker.io/rancher/hardened-addon-resizer:1.8.23-build20260604` | 0 | 2 |
| `docker.io/rancher/klipper-helm:v0.11.1-build20260615` | 0 | 8 |
| `docker.io/rancher/rke2-cloud-provider:v1.36.1-0.20260508014929-7bbbf7c9b258-build20260515` | 0 | 1 |
| `docker.io/rancher/hardened-snapshot-controller:v8.6.0-build20260608` | 0 | 1 |
| `docker.io/rancher/hardened-calico:v3.32.0-build20260604` | 0 | 3 |
| `docker.io/rancher/hardened-flannel:v0.28.5-build20260604` | 0 | 2 |

### CVE-free Images (5)

- `docker.io/rancher/hardened-coredns:v1.14.4-build20260610`
- `docker.io/rancher/hardened-etcd:v3.6.12-k3s1-build20260603`
- `docker.io/rancher/klipper-lb:v0.4.17`
- `docker.io/rancher/mirrored-pause:3.6`
- `docker.io/rancher/hardened-traefik:v3.7.4-build20260608`

