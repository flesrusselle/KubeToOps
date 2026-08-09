# 🚀 Getting Started with KubeToOps: Step-by-Step Guide

Welcome to **KubeToOps** (*Navigate Kubernetes. Operate with confidence.*).

This getting-started guide takes you step-by-step through setting up your environment, verifying your CLI tools, configuring shell completions, and executing your first diagnostic commands.

---

## 📋 Step-by-Step Walkthrough: What To Do & How To Do It

### Step 1: Verify Host Tooling
Run the built-in prerequisite checker to identify missing binaries:

```bash
# Run automated prerequisite check
make check-prerequisites
```

#### Recommended Tooling Matrix
| Binary | Recommended Action | macOS Command | Linux Command |
| :--- | :--- | :--- | :--- |
| `kubectl` | Primary K8s CLI | `brew install kubernetes-cli` | Official binary install |
| `kubectx` / `kubens` | Context & namespace switching | `brew install kubectx` | GitHub script install |
| `k9s` | Terminal UI dashboard | `brew install derailed/k9s/k9s` | Webinstall script |
| `stern` | Multi-pod log tailer | `brew install stern` | GitHub release download |

---

### Step 2: Configure Terminal Shell Completion & Aliases
Speed up your daily terminal workflow by enabling `kubectl` autocompletion and aliases:

#### For Zsh Users (`~/.zshrc`):
```zsh
# Enable kubectl autocompletion
source <(kubectl completion zsh)

# Core aliases
alias k='kubectl'
alias kgp='kubectl get pods'
alias kgs='kubectl get svc'
alias kgd='kubectl get deploy'
alias kge='kubectl get events --sort-by=.lastTimestamp'
alias klf='kubectl logs -f'

# Enable completion for alias 'k'
complete -o default -F __start_kubectl k
```

#### For Bash Users (`~/.bashrc`):
```bash
source <(kubectl completion bash)
alias k='kubectl'
complete -o default -F __start_kubectl k
```

Reload shell configuration:
```bash
source ~/.zshrc  # or source ~/.bashrc
```

---

### Step 3: Verify Cluster Context Before Running Commands
Before issuing state-changing commands, confirm which Kubernetes cluster context is currently active:

```bash
# Check current active context
kubectl config current-context

# Switch context if necessary
kubectx dev-cluster
```

---

### Step 4: Run Your First Diagnostic Inspection
Test your setup by retrieving pods and sorting recent cluster events:

```bash
# Get pods in current namespace with wide formatting (Pod IP + Node)
kubectl get pods -o wide

# Sort events chronologically to catch recent warnings
kubectl get events --sort-by=.lastTimestamp
```

---

### Step 5: Explore Diagnostic Playbooks
Bookmark our core troubleshooting guides:
- 🩺 **[CrashLoopBackOff Playbook](../troubleshooting/crashloopbackoff.md)**
- 🩺 **[ImagePullBackOff Playbook](../troubleshooting/imagepullbackoff.md)**
- 🩺 **[Pending Pod Playbook](../troubleshooting/pending.md)**
- 🩺 **[Service Unreachable Playbook](../troubleshooting/service-unreachable.md)**
- 🛡️ **[Don't Accidentally Break Production](../security/dont-accidentally-break-production.md)**
