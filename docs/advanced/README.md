# 🔬 Advanced Kubernetes Operations

Custom Resource Definitions (CRDs), JSONPath filtering, and API discovery.

---

## 1. Custom Resource Discovery

```bash
# List all registered CRDs in cluster
kubectl get crd

# Get instances of a Custom Resource
kubectl get <crd-name> -A
```

---

## 2. Advanced JSONPath Expressions

```bash
# Extract only pod IP and pod name
kubectl get pods -o jsonpath='{range .items[*]}{.metadata.name}{"\t"}{.status.podIP}{"\n"}{end}'
```

### Safety Rating: 🟢 Safe
