# 🩺 Troubleshooting ImagePullBackOff & ErrImagePull

## Symptom
Pod status displays `ImagePullBackOff` or `ErrImagePull`.

---

## Diagnostic Workflow

### Step 1: Describe Pod Events
```bash
kubectl describe pod <pod-name> -n <namespace>
```
*Scroll to the `Events:` block at the bottom.*

### Step 2: How to Interpret Results

| Error Message | Meaning | Fix |
| :--- | :--- | :--- |
| `manifest for ... not found` | Image tag does not exist in registry | Correct image tag in pod spec |
| `unauthorized: authentication required` | Missing or invalid registry credentials | Add valid `imagePullSecrets` to pod/serviceaccount |
| `connection refused / timeout` | Worker node cannot reach container registry | Fix node outbound networking / proxy settings |
| `no matching manifest for architecture` | Architecture mismatch (e.g. arm64 vs amd64) | Rebuild multi-arch container image |

### Step 3: Verification
```bash
kubectl get pod <pod-name> -n <namespace> -w
```

### Safety Rating: 🟢 Safe
