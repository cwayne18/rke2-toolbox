# Trivy Scan Report

## Images Scanned

- `docker.io/rancher/rke2-runtime:v1.36.1-rke2r1`
- `docker.io/rancher/hardened-kubernetes:v1.36.1-rke2r1-build20260512`
- `docker.io/rancher/hardened-coredns:v1.14.3-build20260511`
- `docker.io/rancher/hardened-cluster-autoscaler:v1.10.3-build20260511`
- `docker.io/rancher/hardened-dns-node-cache:1.26.8-build20260511`
- `docker.io/rancher/hardened-etcd:v3.6.7-k3s1-build20260512`
- `docker.io/rancher/hardened-k8s-metrics-server:v0.8.1-build20260513`
- `docker.io/rancher/hardened-addon-resizer:1.8.23-build20260511`
- `docker.io/rancher/klipper-helm:v0.10.0-build20260513`
- `docker.io/rancher/klipper-lb:v0.4.17`
- `docker.io/rancher/mirrored-pause:3.6`
- `docker.io/rancher/rke2-cloud-provider:v1.36.0-rc2.0.20260427154526-d239025e2a23-build20260429`
- `docker.io/rancher/hardened-snapshot-controller:v8.5.0-build20260513`
- `docker.io/rancher/hardened-traefik:v3.6.16-build20260512`
- `docker.io/rancher/hardened-calico:v3.32.0-build20260511`
- `docker.io/rancher/hardened-flannel:v0.28.4-build20260511`

## Scan Results: `docker.io/rancher/rke2-runtime:v1.36.1-rke2r1`

```text

bin/containerd (gobinary)
=========================
Total: 2 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 2, CRITICAL: 0)

┌──────────────────────────┬────────────────┬──────────┬──────────┬──────────────────────┬───────────────┬───────────────────────────────────────────────────────────┐
│         Library          │ Vulnerability  │ Severity │  Status  │  Installed Version   │ Fixed Version │                           Title                           │
├──────────────────────────┼────────────────┼──────────┼──────────┼──────────────────────┼───────────────┼───────────────────────────────────────────────────────────┤
│ github.com/docker/docker │ CVE-2026-41567 │ HIGH     │ affected │ v27.3.1+incompatible │               │ Docker: `PUT /containers/{id}/archive` executes container │
│                          │                │          │          │                      │               │ binary on the host                                        │
│                          │                │          │          │                      │               │ https://avd.aquasec.com/nvd/cve-2026-41567                │
│                          ├────────────────┤          │          │                      ├───────────────┼───────────────────────────────────────────────────────────┤
│                          │ CVE-2026-42306 │          │          │                      │               │ Docker: Race condition in docker cp allows bind mount     │
│                          │                │          │          │                      │               │ redirection to host...                                    │
│                          │                │          │          │                      │               │ https://avd.aquasec.com/nvd/cve-2026-42306                │
└──────────────────────────┴────────────────┴──────────┴──────────┴──────────────────────┴───────────────┴───────────────────────────────────────────────────────────┘

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

bin/kubectl (gobinary)
======================
Total: 4 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 4, CRITICAL: 0)

┌─────────┬────────────────┬──────────┬────────┬───────────────────┬─────────────────┬──────────────────────────────────────────────────────────────┐
│ Library │ Vulnerability  │ Severity │ Status │ Installed Version │  Fixed Version  │                            Title                             │
├─────────┼────────────────┼──────────┼────────┼───────────────────┼─────────────────┼──────────────────────────────────────────────────────────────┤
│ stdlib  │ CVE-2026-33814 │ HIGH     │ fixed  │ v1.26.2           │ 1.25.10, 1.26.3 │ When processing HTTP/2 SETTINGS frames, transport will enter │
│         │                │          │        │                   │                 │ an infini ...                                                │
│         │                │          │        │                   │                 │ https://avd.aquasec.com/nvd/cve-2026-33814                   │
│         ├────────────────┤          │        │                   │                 ├──────────────────────────────────────────────────────────────┤
│         │ CVE-2026-39820 │          │        │                   │                 │ Well-crafted inputs reaching ParseAddress, ParseAddressList, │
│         │                │          │        │                   │                 │ and Parse ...                                                │
│         │                │          │        │                   │                 │ https://avd.aquasec.com/nvd/cve-2026-39820                   │
│         ├────────────────┤          │        │                   │                 ├──────────────────────────────────────────────────────────────┤
│         │ CVE-2026-39836 │          │        │                   │                 │ Panic in Dial and LookupPort when handling NUL byte on       │
│         │                │          │        │                   │                 │ Windows in...                                                │
│         │                │          │        │                   │                 │ https://avd.aquasec.com/nvd/cve-2026-39836                   │
│         ├────────────────┤          │        │                   │                 ├──────────────────────────────────────────────────────────────┤
│         │ CVE-2026-42499 │          │        │                   │                 │ Pathological inputs could cause DoS through consumePhrase    │
│         │                │          │        │                   │                 │ when parsing ...                                             │
│         │                │          │        │                   │                 │ https://avd.aquasec.com/nvd/cve-2026-42499                   │
└─────────┴────────────────┴──────────┴────────┴───────────────────┴─────────────────┴──────────────────────────────────────────────────────────────┘

bin/kubelet (gobinary)
======================
Total: 4 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 4, CRITICAL: 0)

┌─────────┬────────────────┬──────────┬────────┬───────────────────┬─────────────────┬──────────────────────────────────────────────────────────────┐
│ Library │ Vulnerability  │ Severity │ Status │ Installed Version │  Fixed Version  │                            Title                             │
├─────────┼────────────────┼──────────┼────────┼───────────────────┼─────────────────┼──────────────────────────────────────────────────────────────┤
│ stdlib  │ CVE-2026-33814 │ HIGH     │ fixed  │ v1.26.2           │ 1.25.10, 1.26.3 │ When processing HTTP/2 SETTINGS frames, transport will enter │
│         │                │          │        │                   │                 │ an infini ...                                                │
│         │                │          │        │                   │                 │ https://avd.aquasec.com/nvd/cve-2026-33814                   │
│         ├────────────────┤          │        │                   │                 ├──────────────────────────────────────────────────────────────┤
│         │ CVE-2026-39820 │          │        │                   │                 │ Well-crafted inputs reaching ParseAddress, ParseAddressList, │
│         │                │          │        │                   │                 │ and Parse ...                                                │
│         │                │          │        │                   │                 │ https://avd.aquasec.com/nvd/cve-2026-39820                   │
│         ├────────────────┤          │        │                   │                 ├──────────────────────────────────────────────────────────────┤
│         │ CVE-2026-39836 │          │        │                   │                 │ Panic in Dial and LookupPort when handling NUL byte on       │
│         │                │          │        │                   │                 │ Windows in...                                                │
│         │                │          │        │                   │                 │ https://avd.aquasec.com/nvd/cve-2026-39836                   │
│         ├────────────────┤          │        │                   │                 ├──────────────────────────────────────────────────────────────┤
│         │ CVE-2026-42499 │          │        │                   │                 │ Pathological inputs could cause DoS through consumePhrase    │
│         │                │          │        │                   │                 │ when parsing ...                                             │
│         │                │          │        │                   │                 │ https://avd.aquasec.com/nvd/cve-2026-42499                   │
└─────────┴────────────────┴──────────┴────────┴───────────────────┴─────────────────┴──────────────────────────────────────────────────────────────┘
```

## Scan Results: `docker.io/rancher/hardened-kubernetes:v1.36.1-rke2r1-build20260512`

```text

usr/local/bin/kube-apiserver (gobinary)
=======================================
Total: 4 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 4, CRITICAL: 0)

┌─────────┬────────────────┬──────────┬────────┬───────────────────┬─────────────────┬──────────────────────────────────────────────────────────────┐
│ Library │ Vulnerability  │ Severity │ Status │ Installed Version │  Fixed Version  │                            Title                             │
├─────────┼────────────────┼──────────┼────────┼───────────────────┼─────────────────┼──────────────────────────────────────────────────────────────┤
│ stdlib  │ CVE-2026-33814 │ HIGH     │ fixed  │ v1.26.2           │ 1.25.10, 1.26.3 │ When processing HTTP/2 SETTINGS frames, transport will enter │
│         │                │          │        │                   │                 │ an infini ...                                                │
│         │                │          │        │                   │                 │ https://avd.aquasec.com/nvd/cve-2026-33814                   │
│         ├────────────────┤          │        │                   │                 ├──────────────────────────────────────────────────────────────┤
│         │ CVE-2026-39820 │          │        │                   │                 │ Well-crafted inputs reaching ParseAddress, ParseAddressList, │
│         │                │          │        │                   │                 │ and Parse ...                                                │
│         │                │          │        │                   │                 │ https://avd.aquasec.com/nvd/cve-2026-39820                   │
│         ├────────────────┤          │        │                   │                 ├──────────────────────────────────────────────────────────────┤
│         │ CVE-2026-39836 │          │        │                   │                 │ Panic in Dial and LookupPort when handling NUL byte on       │
│         │                │          │        │                   │                 │ Windows in...                                                │
│         │                │          │        │                   │                 │ https://avd.aquasec.com/nvd/cve-2026-39836                   │
│         ├────────────────┤          │        │                   │                 ├──────────────────────────────────────────────────────────────┤
│         │ CVE-2026-42499 │          │        │                   │                 │ Pathological inputs could cause DoS through consumePhrase    │
│         │                │          │        │                   │                 │ when parsing ...                                             │
│         │                │          │        │                   │                 │ https://avd.aquasec.com/nvd/cve-2026-42499                   │
└─────────┴────────────────┴──────────┴────────┴───────────────────┴─────────────────┴──────────────────────────────────────────────────────────────┘

usr/local/bin/kube-controller-manager (gobinary)
================================================
Total: 4 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 4, CRITICAL: 0)

┌─────────┬────────────────┬──────────┬────────┬───────────────────┬─────────────────┬──────────────────────────────────────────────────────────────┐
│ Library │ Vulnerability  │ Severity │ Status │ Installed Version │  Fixed Version  │                            Title                             │
├─────────┼────────────────┼──────────┼────────┼───────────────────┼─────────────────┼──────────────────────────────────────────────────────────────┤
│ stdlib  │ CVE-2026-33814 │ HIGH     │ fixed  │ v1.26.2           │ 1.25.10, 1.26.3 │ When processing HTTP/2 SETTINGS frames, transport will enter │
│         │                │          │        │                   │                 │ an infini ...                                                │
│         │                │          │        │                   │                 │ https://avd.aquasec.com/nvd/cve-2026-33814                   │
│         ├────────────────┤          │        │                   │                 ├──────────────────────────────────────────────────────────────┤
│         │ CVE-2026-39820 │          │        │                   │                 │ Well-crafted inputs reaching ParseAddress, ParseAddressList, │
│         │                │          │        │                   │                 │ and Parse ...                                                │
│         │                │          │        │                   │                 │ https://avd.aquasec.com/nvd/cve-2026-39820                   │
│         ├────────────────┤          │        │                   │                 ├──────────────────────────────────────────────────────────────┤
│         │ CVE-2026-39836 │          │        │                   │                 │ Panic in Dial and LookupPort when handling NUL byte on       │
│         │                │          │        │                   │                 │ Windows in...                                                │
│         │                │          │        │                   │                 │ https://avd.aquasec.com/nvd/cve-2026-39836                   │
│         ├────────────────┤          │        │                   │                 ├──────────────────────────────────────────────────────────────┤
│         │ CVE-2026-42499 │          │        │                   │                 │ Pathological inputs could cause DoS through consumePhrase    │
│         │                │          │        │                   │                 │ when parsing ...                                             │
│         │                │          │        │                   │                 │ https://avd.aquasec.com/nvd/cve-2026-42499                   │
└─────────┴────────────────┴──────────┴────────┴───────────────────┴─────────────────┴──────────────────────────────────────────────────────────────┘

usr/local/bin/kube-proxy (gobinary)
===================================
Total: 4 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 4, CRITICAL: 0)

┌─────────┬────────────────┬──────────┬────────┬───────────────────┬─────────────────┬──────────────────────────────────────────────────────────────┐
│ Library │ Vulnerability  │ Severity │ Status │ Installed Version │  Fixed Version  │                            Title                             │
├─────────┼────────────────┼──────────┼────────┼───────────────────┼─────────────────┼──────────────────────────────────────────────────────────────┤
│ stdlib  │ CVE-2026-33814 │ HIGH     │ fixed  │ v1.26.2           │ 1.25.10, 1.26.3 │ When processing HTTP/2 SETTINGS frames, transport will enter │
│         │                │          │        │                   │                 │ an infini ...                                                │
│         │                │          │        │                   │                 │ https://avd.aquasec.com/nvd/cve-2026-33814                   │
│         ├────────────────┤          │        │                   │                 ├──────────────────────────────────────────────────────────────┤
│         │ CVE-2026-39820 │          │        │                   │                 │ Well-crafted inputs reaching ParseAddress, ParseAddressList, │
│         │                │          │        │                   │                 │ and Parse ...                                                │
│         │                │          │        │                   │                 │ https://avd.aquasec.com/nvd/cve-2026-39820                   │
│         ├────────────────┤          │        │                   │                 ├──────────────────────────────────────────────────────────────┤
│         │ CVE-2026-39836 │          │        │                   │                 │ Panic in Dial and LookupPort when handling NUL byte on       │
│         │                │          │        │                   │                 │ Windows in...                                                │
│         │                │          │        │                   │                 │ https://avd.aquasec.com/nvd/cve-2026-39836                   │
│         ├────────────────┤          │        │                   │                 ├──────────────────────────────────────────────────────────────┤
│         │ CVE-2026-42499 │          │        │                   │                 │ Pathological inputs could cause DoS through consumePhrase    │
│         │                │          │        │                   │                 │ when parsing ...                                             │
│         │                │          │        │                   │                 │ https://avd.aquasec.com/nvd/cve-2026-42499                   │
└─────────┴────────────────┴──────────┴────────┴───────────────────┴─────────────────┴──────────────────────────────────────────────────────────────┘

usr/local/bin/kube-scheduler (gobinary)
=======================================
Total: 4 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 4, CRITICAL: 0)

┌─────────┬────────────────┬──────────┬────────┬───────────────────┬─────────────────┬──────────────────────────────────────────────────────────────┐
│ Library │ Vulnerability  │ Severity │ Status │ Installed Version │  Fixed Version  │                            Title                             │
├─────────┼────────────────┼──────────┼────────┼───────────────────┼─────────────────┼──────────────────────────────────────────────────────────────┤
│ stdlib  │ CVE-2026-33814 │ HIGH     │ fixed  │ v1.26.2           │ 1.25.10, 1.26.3 │ When processing HTTP/2 SETTINGS frames, transport will enter │
│         │                │          │        │                   │                 │ an infini ...                                                │
│         │                │          │        │                   │                 │ https://avd.aquasec.com/nvd/cve-2026-33814                   │
│         ├────────────────┤          │        │                   │                 ├──────────────────────────────────────────────────────────────┤
│         │ CVE-2026-39820 │          │        │                   │                 │ Well-crafted inputs reaching ParseAddress, ParseAddressList, │
│         │                │          │        │                   │                 │ and Parse ...                                                │
│         │                │          │        │                   │                 │ https://avd.aquasec.com/nvd/cve-2026-39820                   │
│         ├────────────────┤          │        │                   │                 ├──────────────────────────────────────────────────────────────┤
│         │ CVE-2026-39836 │          │        │                   │                 │ Panic in Dial and LookupPort when handling NUL byte on       │
│         │                │          │        │                   │                 │ Windows in...                                                │
│         │                │          │        │                   │                 │ https://avd.aquasec.com/nvd/cve-2026-39836                   │
│         ├────────────────┤          │        │                   │                 ├──────────────────────────────────────────────────────────────┤
│         │ CVE-2026-42499 │          │        │                   │                 │ Pathological inputs could cause DoS through consumePhrase    │
│         │                │          │        │                   │                 │ when parsing ...                                             │
│         │                │          │        │                   │                 │ https://avd.aquasec.com/nvd/cve-2026-42499                   │
└─────────┴────────────────┴──────────┴────────┴───────────────────┴─────────────────┴──────────────────────────────────────────────────────────────┘

usr/local/bin/kubectl (gobinary)
================================
Total: 4 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 4, CRITICAL: 0)

┌─────────┬────────────────┬──────────┬────────┬───────────────────┬─────────────────┬──────────────────────────────────────────────────────────────┐
│ Library │ Vulnerability  │ Severity │ Status │ Installed Version │  Fixed Version  │                            Title                             │
├─────────┼────────────────┼──────────┼────────┼───────────────────┼─────────────────┼──────────────────────────────────────────────────────────────┤
│ stdlib  │ CVE-2026-33814 │ HIGH     │ fixed  │ v1.26.2           │ 1.25.10, 1.26.3 │ When processing HTTP/2 SETTINGS frames, transport will enter │
│         │                │          │        │                   │                 │ an infini ...                                                │
│         │                │          │        │                   │                 │ https://avd.aquasec.com/nvd/cve-2026-33814                   │
│         ├────────────────┤          │        │                   │                 ├──────────────────────────────────────────────────────────────┤
│         │ CVE-2026-39820 │          │        │                   │                 │ Well-crafted inputs reaching ParseAddress, ParseAddressList, │
│         │                │          │        │                   │                 │ and Parse ...                                                │
│         │                │          │        │                   │                 │ https://avd.aquasec.com/nvd/cve-2026-39820                   │
│         ├────────────────┤          │        │                   │                 ├──────────────────────────────────────────────────────────────┤
│         │ CVE-2026-39836 │          │        │                   │                 │ Panic in Dial and LookupPort when handling NUL byte on       │
│         │                │          │        │                   │                 │ Windows in...                                                │
│         │                │          │        │                   │                 │ https://avd.aquasec.com/nvd/cve-2026-39836                   │
│         ├────────────────┤          │        │                   │                 ├──────────────────────────────────────────────────────────────┤
│         │ CVE-2026-42499 │          │        │                   │                 │ Pathological inputs could cause DoS through consumePhrase    │
│         │                │          │        │                   │                 │ when parsing ...                                             │
│         │                │          │        │                   │                 │ https://avd.aquasec.com/nvd/cve-2026-42499                   │
└─────────┴────────────────┴──────────┴────────┴───────────────────┴─────────────────┴──────────────────────────────────────────────────────────────┘

usr/local/bin/kubelet (gobinary)
================================
Total: 4 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 4, CRITICAL: 0)

┌─────────┬────────────────┬──────────┬────────┬───────────────────┬─────────────────┬──────────────────────────────────────────────────────────────┐
│ Library │ Vulnerability  │ Severity │ Status │ Installed Version │  Fixed Version  │                            Title                             │
├─────────┼────────────────┼──────────┼────────┼───────────────────┼─────────────────┼──────────────────────────────────────────────────────────────┤
│ stdlib  │ CVE-2026-33814 │ HIGH     │ fixed  │ v1.26.2           │ 1.25.10, 1.26.3 │ When processing HTTP/2 SETTINGS frames, transport will enter │
│         │                │          │        │                   │                 │ an infini ...                                                │
│         │                │          │        │                   │                 │ https://avd.aquasec.com/nvd/cve-2026-33814                   │
│         ├────────────────┤          │        │                   │                 ├──────────────────────────────────────────────────────────────┤
│         │ CVE-2026-39820 │          │        │                   │                 │ Well-crafted inputs reaching ParseAddress, ParseAddressList, │
│         │                │          │        │                   │                 │ and Parse ...                                                │
│         │                │          │        │                   │                 │ https://avd.aquasec.com/nvd/cve-2026-39820                   │
│         ├────────────────┤          │        │                   │                 ├──────────────────────────────────────────────────────────────┤
│         │ CVE-2026-39836 │          │        │                   │                 │ Panic in Dial and LookupPort when handling NUL byte on       │
│         │                │          │        │                   │                 │ Windows in...                                                │
│         │                │          │        │                   │                 │ https://avd.aquasec.com/nvd/cve-2026-39836                   │
│         ├────────────────┤          │        │                   │                 ├──────────────────────────────────────────────────────────────┤
│         │ CVE-2026-42499 │          │        │                   │                 │ Pathological inputs could cause DoS through consumePhrase    │
│         │                │          │        │                   │                 │ when parsing ...                                             │
│         │                │          │        │                   │                 │ https://avd.aquasec.com/nvd/cve-2026-42499                   │
└─────────┴────────────────┴──────────┴────────┴───────────────────┴─────────────────┴──────────────────────────────────────────────────────────────┘
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
```

## Scan Results: `docker.io/rancher/klipper-lb:v0.4.17`

```text
```

## Scan Results: `docker.io/rancher/mirrored-pause:3.6`

```text
```

## Scan Results: `docker.io/rancher/rke2-cloud-provider:v1.36.0-rc2.0.20260427154526-d239025e2a23-build20260429`

```text

usr/local/bin/rke2-cloud-provider (gobinary)
============================================
Total: 5 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 5, CRITICAL: 0)

┌─────────┬────────────────┬──────────┬────────┬───────────────────┬─────────────────┬──────────────────────────────────────────────────────────────┐
│ Library │ Vulnerability  │ Severity │ Status │ Installed Version │  Fixed Version  │                            Title                             │
├─────────┼────────────────┼──────────┼────────┼───────────────────┼─────────────────┼──────────────────────────────────────────────────────────────┤
│ stdlib  │ CVE-2026-33811 │ HIGH     │ fixed  │ v1.26.2           │ 1.25.10, 1.26.3 │ When using LookupCNAME with the cgo DNS resolver, a very     │
│         │                │          │        │                   │                 │ long CNAME...                                                │
│         │                │          │        │                   │                 │ https://avd.aquasec.com/nvd/cve-2026-33811                   │
│         ├────────────────┤          │        │                   │                 ├──────────────────────────────────────────────────────────────┤
│         │ CVE-2026-33814 │          │        │                   │                 │ When processing HTTP/2 SETTINGS frames, transport will enter │
│         │                │          │        │                   │                 │ an infini ...                                                │
│         │                │          │        │                   │                 │ https://avd.aquasec.com/nvd/cve-2026-33814                   │
│         ├────────────────┤          │        │                   │                 ├──────────────────────────────────────────────────────────────┤
│         │ CVE-2026-39820 │          │        │                   │                 │ Well-crafted inputs reaching ParseAddress, ParseAddressList, │
│         │                │          │        │                   │                 │ and Parse ...                                                │
│         │                │          │        │                   │                 │ https://avd.aquasec.com/nvd/cve-2026-39820                   │
│         ├────────────────┤          │        │                   │                 ├──────────────────────────────────────────────────────────────┤
│         │ CVE-2026-39836 │          │        │                   │                 │ Panic in Dial and LookupPort when handling NUL byte on       │
│         │                │          │        │                   │                 │ Windows in...                                                │
│         │                │          │        │                   │                 │ https://avd.aquasec.com/nvd/cve-2026-39836                   │
│         ├────────────────┤          │        │                   │                 ├──────────────────────────────────────────────────────────────┤
│         │ CVE-2026-42499 │          │        │                   │                 │ Pathological inputs could cause DoS through consumePhrase    │
│         │                │          │        │                   │                 │ when parsing ...                                             │
│         │                │          │        │                   │                 │ https://avd.aquasec.com/nvd/cve-2026-42499                   │
└─────────┴────────────────┴──────────┴────────┴───────────────────┴─────────────────┴──────────────────────────────────────────────────────────────┘
```

## Scan Results: `docker.io/rancher/hardened-snapshot-controller:v8.5.0-build20260513`

```text
```

## Scan Results: `docker.io/rancher/hardened-traefik:v3.6.16-build20260512`

```text
```

## Scan Results: `docker.io/rancher/hardened-calico:v3.32.0-build20260511`

```text
```

## Scan Results: `docker.io/rancher/hardened-flannel:v0.28.4-build20260511`

```text
```

## Summary

### CVEs by Severity

| Severity | Count |
| --- | ---: |
| CRITICAL | 0 |
| HIGH | 41 |
| **Total** | **41** |

### Scan Coverage

| Metric | Count |
| --- | ---: |
| Images scanned | 16 |
| Binaries scanned | 55 |
| **Total scanned targets** | **71** |

### Images with CVEs (3)

| Image | CRITICAL | HIGH |
| --- | ---: | ---: |
| `docker.io/rancher/rke2-runtime:v1.36.1-rke2r1` | 0 | 12 |
| `docker.io/rancher/hardened-kubernetes:v1.36.1-rke2r1-build20260512` | 0 | 24 |
| `docker.io/rancher/rke2-cloud-provider:v1.36.0-rc2.0.20260427154526-d239025e2a23-build20260429` | 0 | 5 |

### CVE-free Images (13)

- `docker.io/rancher/hardened-coredns:v1.14.3-build20260511`
- `docker.io/rancher/hardened-cluster-autoscaler:v1.10.3-build20260511`
- `docker.io/rancher/hardened-dns-node-cache:1.26.8-build20260511`
- `docker.io/rancher/hardened-etcd:v3.6.7-k3s1-build20260512`
- `docker.io/rancher/hardened-k8s-metrics-server:v0.8.1-build20260513`
- `docker.io/rancher/hardened-addon-resizer:1.8.23-build20260511`
- `docker.io/rancher/klipper-helm:v0.10.0-build20260513`
- `docker.io/rancher/klipper-lb:v0.4.17`
- `docker.io/rancher/mirrored-pause:3.6`
- `docker.io/rancher/hardened-snapshot-controller:v8.5.0-build20260513`
- `docker.io/rancher/hardened-traefik:v3.6.16-build20260512`
- `docker.io/rancher/hardened-calico:v3.32.0-build20260511`
- `docker.io/rancher/hardened-flannel:v0.28.4-build20260511`

