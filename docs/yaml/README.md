# 📜 YAML Manifest Formatting & Editing

Kubernetes declarative management relies on clean, valid YAML specifications.

---

## 1. Dry-Run Generation

```bash
# Imperatively generate clean Deployment manifest
kubectl create deployment my-app --image=nginx:latest --dry-run=client -o yaml > deployment.yaml
```

---

## 2. Stripping Managed Fields (`kubectl-neat`)

Exported resource manifests contain noisy server-side metadata (`managedFields`, `resourceVersion`, `uid`).

```bash
# Export pristine YAML manifest
kubectl get deployment my-app -n default -o yaml | kubectl neat > clean-deployment.yaml
```

---

## 3. Manifest Diffing (`kubectl diff`)

Compare live cluster state against a local manifest file before executing `kubectl apply`:

```bash
kubectl diff -f deployment.yaml
```

### Safety Rating: 🟢 Safe
