# 🩺 Kubernetes Troubleshooting Playbooks

Structured operational decision trees for diagnosing and remediating common Kubernetes pod and service failure modes.

---

## 📚 Playbook Directory

| Failure Mode | Common Root Cause | Playbook Link |
| :--- | :--- | :--- |
| **CrashLoopBackOff** | Application crash, missing config, failed probes | [`crashloopbackoff.md`](crashloopbackoff.md) |
| **ImagePullBackOff** | Bad image tag, registry auth error, network blocked | [`imagepullbackoff.md`](imagepullbackoff.md) |
| **Pending Pod** | Insufficient node resources, taint mismatch, PVC unmapped | [`pending.md`](pending.md) |
| **OOMKilled** | Container memory limit exceeded, application memory leak | [`oomkilled.md`](oomkilled.md) |
| **Service Unreachable** | Bad pod selector, container port mismatch, NetworkPolicy | [`service-unreachable.md`](service-unreachable.md) |

---

## Standard Diagnostic Flow

`Status ↓ Describe ↓ Logs ↓ Previous logs ↓ Events ↓ Configuration ↓ Probes ↓ Verification`
