# 🛡️ Production Safeguards & Context Awareness

Executing a destructive command (e.g. `kubectl delete pod`, `kubectl apply -f`) against a production cluster by mistake is a major operational risk.

---

## 1. Context-Aware Shell Prompts (Kube-PS1)

Integrate active Kubernetes cluster context and namespace into your Zsh/Bash prompt.

```zsh
# ~/.zshrc setup for kube-ps1
source "/usr/local/opt/kube-ps1/share/kube-ps1.sh"
PROMPT='$(kube_ps1) '$PROMPT
```

Displays: `(prod-cluster:default) $`

---

## 2. Separate Kubeconfig Files

Avoid storing staging, dev, and production credentials in a single monolithic `~/.kube/config` file.

```bash
# Export distinct environment kubeconfig files
export KUBECONFIG=~/.kube/config-dev:~/.kube/config-prod
```

---

## 3. Destructive Command Aliases & Safe Habits

Never run deletion commands without validating current context:

```bash
# Verify active cluster context before state modification
kubectl config current-context
```

### Safety Rating: 🟢 Safe
