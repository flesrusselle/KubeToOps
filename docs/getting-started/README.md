# 🚀 Getting Started with KubeToOps

Welcome to **KubeToOps** (*Navigate Kubernetes. Operate with confidence.*).

This getting-started guide ensures your local workstation is equipped with the recommended tools, shell configurations, and environment checks before using our operational playbooks.

---

## 1. Prerequisite Checklist

Before diving into KubeToOps workflows, check which host CLI tools are currently installed:

```bash
# Run the automated prerequisite checker script
make check-prerequisites
```

### Essential Tools Hierarchy

| Tool | Purpose | Priority | Installation (macOS) | Installation (Linux) |
| :--- | :--- | :--- | :--- | :--- |
| `kubectl` | Kubernetes primary CLI | **Required** | `brew install kubernetes-cli` | Official binary download |
| `git` | Version control & repo sync | **Required** | Installed by default / `brew install git` | `sudo apt install git` |
| `python3` | Automation & catalog verification | **Required** | `brew install python` | `sudo apt install python3` |
| `kubectx` / `kubens` | Safe context/namespace switching | **Highly Recommended** | `brew install kubectx` | GitHub binary install |
| `k9s` | Terminal UI for K8s navigation | **Highly Recommended** | `brew install derailed/k9s/k9s` | Webinstall script |
| `krew` | kubectl plugin package manager | **Recommended** | Official install script | Official install script |
| `shellcheck` | Shell script linter | **Optional (CI/Dev)** | `brew install shellcheck` | `sudo apt install shellcheck` |
| `yamllint` | YAML format validator | **Optional (CI/Dev)** | `brew install yamllint` | `pip install yamllint` |

---

## 2. Shell Completion Setup

Enable shell completion so `kubectl`, `kubectx`, and `kubens` auto-complete resource names and flags.

### Zsh (`~/.zshrc`)
```zsh
# Enable kubectl autocompletion
source <(kubectl completion zsh)

# Setup alias for k and enable completion
alias k=kubectl
complete -o default -F __start_kubectl k
```

### Bash (`~/.bashrc`)
```bash
# Enable kubectl autocompletion
source <(kubectl completion bash)

# Setup alias for k and enable completion
alias k=kubectl
complete -o default -F __start_kubectl k
```

👉 Detailed shell completion reference: [`docs/aliases/shell-completion.md`](../aliases/shell-completion.md)

---

## 3. Verifying Your Local Environment

Run the repository validation tool to confirm that all catalog commands and Python scripts pass validation:

```bash
# Run local unit tests and schema checks
make test
```

Expected output:
```
============================== test session starts ==============================
collected 4 items

tests/test_command_catalog.py .                                         [ 25%]
tests/test_cotd_selection.py .                                          [ 50%]
tests/test_pr_summary.py .                                              [ 75%]
tests/test_release_preview.py .                                         [100%]

============================== 4 passed in 0.15s ===============================
```

---

## 4. Next Steps

- Explore the **[Quick Reference](file:///Users/flestorres/Desktop/apply/KubeToOps/docs/quick-reference.md)** for immediate incident response commands.
- Review **[kubectl Productivity](file:///Users/flestorres/Desktop/apply/KubeToOps/docs/kubectl/productivity.md)** for speed shortcuts.
- Check **[Production Safeguards](file:///Users/flestorres/Desktop/apply/KubeToOps/docs/security/dont-accidentally-break-production.md)** to prevent dangerous production mistakes.
