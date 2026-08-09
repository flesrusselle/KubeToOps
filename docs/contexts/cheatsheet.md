# 📄 Context & Kubeconfig Cheatsheet

```bash
# Print current active context name
kubectl config current-context

# List all available contexts in kubeconfig
kubectl config get-contexts

# Set default namespace for current active context
kubectl config set-context --current --namespace=monitoring

# Switch active cluster context
kubectl config use-context staging-cluster

# Delete unused context reference from kubeconfig
kubectl config delete-context legacy-cluster
```
