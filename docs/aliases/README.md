# ⚡ Shell Aliases & Autocompletion

Boost your terminal velocity with vetted `kubectl` command aliases and shell completion configs.

---

## Recommended Alias Set

```bash
# Core alias
alias k='kubectl'

# Get resources
alias kgp='kubectl get pods'
alias kgs='kubectl get services'
alias kgd='kubectl get deployments'
alias kge='kubectl get events --sort-by=.lastTimestamp'

# Describe resources
alias kdp='kubectl describe pod'
alias kdd='kubectl describe deployment'

# Logs & Exec
alias kl='kubectl logs'
alias klf='kubectl logs -f'
alias kex='kubectl exec -it'
```

👉 **[Shell Completion Setup](shell-completion.md)** | **[Alias Cheatsheet](cheatsheet.md)**
