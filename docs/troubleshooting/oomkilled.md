# 🩺 Troubleshooting OOMKilled Containers

## Symptom
Container restarts with `OOMKilled` status or exit code `137`.

---

## Diagnostic Workflow

### Step 1: Confirm OOM Event
```bash
kubectl describe pod <pod-name> -n <namespace> | grep -E "OOMKilled|Exit Code"
```

### Step 2: Check Actual Memory Consumption
```bash
kubectl top pod <pod-name> -n <namespace> --containers
```

### Step 3: Fixes
1. **Increase Memory Limits**: Update `resources.limits.memory` in Deployment spec.
2. **Profile Application Memory Leaks**: Heap dump or profile application memory usage.

### Step 4: Verification
```bash
kubectl top pod <pod-name> -n <namespace>
```

### Safety Rating: 🟢 Safe
