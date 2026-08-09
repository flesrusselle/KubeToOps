# 🩺 Troubleshooting CrashLoopBackOff

## Symptom
Pod status displays `CrashLoopBackOff` or `Error`. The restart count increments steadily.

---

## Diagnostic Workflow

```
Status ↓ Describe ↓ Logs ↓ Previous logs ↓ Events ↓ Configuration ↓ Probes ↓ Verification
```

### Step 1: First Command — Check Pod Details & Events
```bash
kubectl describe pod <pod-name> -n <namespace>
```
*Look at the `Last State` line under `Containers`. Note exit codes (e.g. `Exit Code 1`, `Exit Code 137`).*

### Step 2: Fetch Previous Container Logs
```bash
kubectl logs <pod-name> --previous -n <namespace>
```
*`--previous` extracts stderr/stdout logs from the instance immediately before it crashed.*

### Step 3: How to Interpret Results

| Exit Code | Meaning | Immediate Remediation |
| :--- | :--- | :--- |
| **Exit Code 1 / 2** | Application runtime exception / missing environment variable | Check application config & environment vars |
| **Exit Code 137** | Process killed by OOM (Out Of Memory) killer | Increase container `resources.limits.memory` |
| **Exit Code 139** | Segmentation fault | Check native C/C++ library dependencies |
| **Exit Code 143** | SIGTERM graceful termination timeout | Adjust `terminationGracePeriodSeconds` or liveness probe |

### Step 4: Likely Fixes
1. Fix missing ConfigMap or Secret references in `env` / `envFrom`.
2. Relax failing `livenessProbe` initialDelaySeconds or threshold.
3. Fix memory limit allocation.

### Step 5: Verification
```bash
kubectl get pod <pod-name> -n <namespace> -w
```
Confirm `STATUS` transitions to `Running` and `READY` shows `1/1` without incrementing restart count.

### Safety Rating: 🟢 Safe
