# 🧭 KubeToOps — Navigate Kubernetes. Operate with confidence.

[![Validation](https://github.com/flesrusselle/KubeToOps/actions/workflows/validate.yml/badge.svg)](https://github.com/flesrusselle/KubeToOps/actions/workflows/validate.yml)
[![Command Catalog](https://github.com/flesrusselle/KubeToOps/actions/workflows/validate-commands.yml/badge.svg)](https://github.com/flesrusselle/KubeToOps/actions/workflows/validate-commands.yml)
[![Security Scan](https://github.com/flesrusselle/KubeToOps/actions/workflows/security.yml/badge.svg)](https://github.com/flesrusselle/KubeToOps/actions/workflows/security.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Cost: $0](https://img.shields.io/badge/Cost-%240_Hosting-brightgreen.svg)](docs/COST.md)

> A practical, high-velocity Kubernetes field guide and operational toolbox for DevOps engineers, SREs, platform engineers, and cloud developers.

**KubeToOps** is NOT a beginner Kubernetes tutorial. It is a practical engineering field guide for professionals who already understand basic Kubernetes concepts (`kubectl get pods`, pods vs services, basic YAML) and want to operate faster, safer, and with higher confidence.

---

## ⚡ 5-Minute Onboarding: What To Do & How To Do It

Select your current goal to jump straight into action:

```
                  ┌──────────────────────────────────────────┐
                  │          WHAT IS YOUR CURRENT GOAL?       │
                  └────────────────────┬─────────────────────┘
                                       │
         ┌─────────────────────────────┼─────────────────────────────┐
         ▼                             ▼                             ▼
┌──────────────────┐         ┌──────────────────┐         ┌──────────────────┐
│  ACTIVE INCIDENT │         │ SHELL SPEEDUP    │         │ PROD SAFEGUARDS  │
│  Fix broken pod  │         │ Aliases & K9s    │         │ Avoid outage     │
└────────┬─────────┘         └────────┬─────────┘         └────────┬─────────┘
         │                            │                            │
         ▼                            ▼                            ▼
┌──────────────────┐         ┌──────────────────┐         ┌──────────────────┐
│ Quick Reference  │         │ Set up Aliases   │         │ Context Guard    │
│ & Playbooks      │         │ & Install K9s    │         │ & Kube-PS1       │
└──────────────────┘         └──────────────────┘         └──────────────────┘
```

### 🚨 Scenario 1: "I am in the middle of an active incident!"
1. Open the **[Quick Reference Guide](docs/quick-reference.md)** ("I Need This Now").
2. Follow our diagnostic playbooks:
   - **CrashLoopBackOff**: [`docs/troubleshooting/crashloopbackoff.md`](docs/troubleshooting/crashloopbackoff.md)
   - **ImagePullBackOff**: [`docs/troubleshooting/imagepullbackoff.md`](docs/troubleshooting/imagepullbackoff.md)
   - **Pending Pod**: [`docs/troubleshooting/pending.md`](docs/troubleshooting/pending.md)
   - **OOMKilled**: [`docs/troubleshooting/oomkilled.md`](docs/troubleshooting/oomkilled.md)
   - **Service Unreachable**: [`docs/troubleshooting/service-unreachable.md`](docs/troubleshooting/service-unreachable.md)

### ⚡ Scenario 2: "I want to work 10x faster in terminal!"
1. Add our curated **[Shell Aliases](docs/aliases/README.md)** to your `~/.zshrc` or `~/.bashrc`.
2. Enable **[Shell Completion](docs/aliases/shell-completion.md)** for `kubectl`, `kubectx`, and `kubens`.
3. Install **[K9s Terminal UI](docs/tools/k9s.md)** (`brew install derailed/k9s/k9s`).

### 🛡️ Scenario 3: "I want to prevent accidental production outages!"
1. Read **[Don't Accidentally Break Production](docs/security/dont-accidentally-break-production.md)**.
2. Setup **[Context Safeguards & Prompt Indicators](docs/contexts/production-safeguards.md)** (`kube-ps1`).

---

## ⚡ Command of the Day

Stay sharp with our automated, deterministic daily Kubernetes command highlight!

👉 **[View Today's Featured Command](command-of-the-day/README.md)**

```bash
# Example: Stream pod status updates during rollouts
kubectl get pods -n default -w
```

---

## 🗺️ Complete Field Guide Navigation

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
