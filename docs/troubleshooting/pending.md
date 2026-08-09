# 🩺 Troubleshooting Pending Pods

## Symptom
Pod status remains stuck in `Pending` state indefinitely.

---

## Diagnostic Workflow

### Step 1: Describe Pod Events
```bash
kubectl describe pod <pod-name> -n <namespace>
```
*Look for scheduler events stating `0/N nodes are available`.*

### Step 2: How to Interpret Scheduler Events

1. **`Insufficient cpu / memory`**: Cluster nodes do not have available allocatable CPU or RAM matching pod `requests`.
   - *Fix*: Add worker nodes via autoscaler, or lower pod resource `requests`.
2. **`node(s) had untolerated taint`**: Worker nodes contain taints that the pod spec does not tolerate.
   - *Fix*: Add matching `tolerations` to pod spec.
3. **`node(s) didn't match Pod's node affinity/selector`**: Node selector key-values do not match any active node.
   - *Fix*: Align `nodeSelector` labels with worker node labels.
4. **`persistentvolumeclaim "..." not found / bound`**: Storage PVC is not bound.
   - *Fix*: Verify StorageClass and PVC provisioning.

### Step 3: Verification
```bash
kubectl get pod <pod-name> -n <namespace> -o wide
```

### Safety Rating: 🟢 Safe
