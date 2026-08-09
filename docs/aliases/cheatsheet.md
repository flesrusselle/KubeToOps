# 📄 Shell Alias Cheatsheet

```bash
# Add these lines to ~/.zshrc or ~/.bashrc
alias k='kubectl'
alias kg='kubectl get'
alias kgp='kubectl get pods'
alias kgpw='kubectl get pods -w'
alias kgpa='kubectl get pods -A'
alias kgs='kubectl get svc'
alias kgd='kubectl get deploy'
alias kge='kubectl get events --sort-by=.lastTimestamp'
alias kd='kubectl describe'
alias kdp='kubectl describe pod'
alias kdd='kubectl describe deploy'
alias kl='kubectl logs'
alias klf='kubectl logs -f'
alias klp='kubectl logs --previous'
alias kex='kubectl exec -it'
alias kpf='kubectl port-forward'
```
