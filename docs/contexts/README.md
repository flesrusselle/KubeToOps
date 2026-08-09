# 🌐 Context Management & Multi-Cluster Safety

A Kubernetes **context** pairs a cluster, a user identity, and a default namespace in your `~/.kube/config` file.

---

## 📚 Section Navigation

| Guide | Purpose | Safety |
| :--- | :--- | :--- |
| **[kubectx Guide](kubectx.md)** | Fast context switching CLI tool | 🟢 Safe |
| **[Production Safeguards](production-safeguards.md)** | Multi-cluster safety guardrails & prompt colors | 🟢 Safe |
| **[Context Cheatsheet](cheatsheet.md)** | Quick `kubectl config` reference | 🟢 Safe |

---

## Core Mechanics

```bash
# View active context
kubectl config current-context

# List all available contexts in kubeconfig
kubectl config get-contexts

# Switch to target context
kubectl config use-context production-us-east-1
```
