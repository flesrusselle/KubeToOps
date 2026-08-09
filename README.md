# 🧭 KubeToOps — Navigate Kubernetes. Operate with confidence.

[![Validation](https://github.com/KubeToOps/KubeToOps/actions/workflows/validate.yml/badge.svg)](https://github.com/KubeToOps/KubeToOps/actions/workflows/validate.yml)
[![Command Catalog](https://github.com/KubeToOps/KubeToOps/actions/workflows/validate-commands.yml/badge.svg)](https://github.com/KubeToOps/KubeToOps/actions/workflows/validate-commands.yml)
[![Security Scan](https://github.com/KubeToOps/KubeToOps/actions/workflows/security.yml/badge.svg)](https://github.com/KubeToOps/KubeToOps/actions/workflows/security.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Cost: $0](https://img.shields.io/badge/Cost-%240_Hosting-brightgreen.svg)](docs/COST.md)

> A practical, high-velocity Kubernetes field guide for DevOps engineers, SREs, platform engineers, and cloud developers.

**KubeToOps** is NOT a beginner Kubernetes tutorial. It is a practical engineering toolbox for professionals who already understand basic Kubernetes concepts (`kubectl get pods`, pods vs services, basic YAML) and want to:

- ⚡ **Work faster** using vetted productivity flags and aliases
- 🔍 **Troubleshoot effectively** with structured diagnostic decision trees
- 🛠️ **Discover powerful tools** like K9s, kubectx/kubens, Krew, Stern, and Popeye
- 🛡️ **Operate safely** with production safeguards and context guardrails
- 📜 **Master YAML workflow** using dry-run generation and schema introspection (`kubectl explain`)

---

## ⚡ Command of the Day

Stay sharp with our automated, deterministic Kubernetes command highlight!

👉 **[View Today's Featured Command](command-of-the-day/README.md)**

```bash
# Example: Stream pod status updates during rollouts
kubectl get pods -n default -w
```

---

## ⚡ "I Need This Now" — Fast Reference

In the middle of an incident or deployment? Skip the guide and hit our fast-lookup index:

👉 **[docs/quick-reference.md](docs/quick-reference.md)**

| Urgent Scenario | Recommended Action / Guide | Safety |
| :--- | :--- | :--- |
| **Pod keeps restarting** | [CrashLoopBackOff Playbook](docs/troubleshooting/crashloopbackoff.md) | 🟢 Safe |
| **Pod stuck pulling image** | [ImagePullBackOff Playbook](docs/troubleshooting/imagepullbackoff.md) | 🟢 Safe |
| **Pod stuck in Pending state** | [Pending Pod Playbook](docs/troubleshooting/pending.md) | 🟢 Safe |
| **Container killed by OOM** | [OOMKilled Playbook](docs/troubleshooting/oomkilled.md) | 🟢 Safe |
| **Service returns connection refused**| [Service Unreachable Playbook](docs/troubleshooting/service-unreachable.md) | 🟢 Safe |
| **Switch cluster context safely** | [Context Safeguards Guide](docs/contexts/production-safeguards.md) | 🟢 Safe |
| **Restart deployment without downtime** | [Rollout Management Guide](docs/workloads/rollouts.md) | 🟡 Caution |

---

## 🗺️ Field Guide Navigation

| Category | Description | Primary Reference |
| :--- | :--- | :--- |
| 🚀 **Getting Started** | Prerequisites, CLI setup, and host validation | [`docs/getting-started/README.md`](docs/getting-started/README.md) |
| 🧰 **kubectl Mastery** | Flags (-A, -o wide, -w), `explain`, dry-run YAML, cheatsheet | [`docs/kubectl/README.md`](docs/kubectl/README.md) |
| 🌐 **Context & Namespaces**| Context safety, `kubectx`, `kubens`, kubeconfig safety | [`docs/contexts/README.md`](docs/contexts/README.md) |
| ⚡ **Aliases & Completion** | Shell completion (Zsh/Bash/Fish) and safe command aliases | [`docs/aliases/README.md`](docs/aliases/README.md) |
| 🔌 **Krew & Plugins** | Curated kubectl plugin ecosystem (`neat`, `who-can`, etc.) | [`docs/plugins/README.md`](docs/plugins/README.md) |
| 🖥️ **K9s & External Tools**| In-depth K9s terminal UI guide, Stern, Helm, Popeye, Kube-linter | [`docs/tools/README.md`](docs/tools/README.md) |
| 🩺 **Troubleshooting** | Step-by-step diagnostic workflows for K8s failure modes | [`docs/troubleshooting/README.md`](docs/troubleshooting/README.md) |
| 🛡️ **Security & Safeguards**| Don't accidentally break production, RBAC, least privilege | [`docs/security/README.md`](docs/security/README.md) |
| 💰 **Zero-Cost Hosting** | $0 cost architecture specification & GitHub Actions design | [`docs/COST.md`](docs/COST.md) |

---

## 🛡️ Core Explanation & Safety Standard

Every command, tool, and playbook in KubeToOps adheres to our strict engineering rubric:

1. **What it does** — Direct technical summary.
2. **Why it is useful** — Real-world operational context.
3. **When to use it** — Specific scenario triggering usage.
4. **How to use it** — Copy-paste command with flag-by-flag breakdown.
5. **What could go wrong** — Edge cases, performance pitfalls, data hazards.
6. **How to verify** — Output validation step.
7. **Official Documentation** — Direct link to official Kubernetes / tool docs.
8. **Safety Rating**:
   - 🟢 **Safe**: Read-only, dry-run, schema lookup.
   - 🟡 **Caution**: Rolling restart, scaling, context switch.
   - 🔴 **Destructive**: Deletion, node drain, resource eviction.

---

## 🛠️ Prerequisites & Local Validation

Before running diagnostic commands or contributing to KubeToOps, verify your host tools:

```bash
# Check prerequisites (git, python3, kubectl, gh, etc.)
make check-prerequisites

# Validate repository integrity & command schema
make validate
```

---

## 🤝 Contributing

We welcome high-quality operational contributions! Please review our [Contributing Guidelines](CONTRIBUTING.md) and [Code of Conduct](CODE_OF_CONDUCT.md).

---

## 📜 License

KubeToOps is open-source software licensed under the [MIT License](LICENSE).
