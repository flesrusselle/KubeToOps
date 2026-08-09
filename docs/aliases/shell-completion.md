# 🐚 Shell Completion Guide

Configuring shell autocompletion for `kubectl` allows `Tab` completion for flags, resource types, pod names, and service names.

---

## 1. Zsh Setup (`~/.zshrc`)

```zsh
# Enable completion
source <(kubectl completion zsh)

# Alias completion setup
alias k=kubectl
complete -o default -F __start_kubectl k
```

---

## 2. Bash Setup (`~/.bashrc`)

```bash
# Install bash-completion package first (brew install bash-completion)
source <(kubectl completion bash)

alias k=kubectl
complete -o default -F __start_kubectl k
```

### Safety Rating: 🟢 Safe
