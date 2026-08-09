# 🏷️ Namespace Scoping & Management

Namespaces provide virtual isolation within a single physical Kubernetes cluster.

---

## Native Namespace Switching

```bash
# View active namespace set in current context
kubectl config view --minify --output 'jsonpath={..namespace}'

# Change default namespace for active context
kubectl config set-context --current --namespace=kube-system
```

👉 See **[kubens Guide](kubens.md)** for fast switching.
