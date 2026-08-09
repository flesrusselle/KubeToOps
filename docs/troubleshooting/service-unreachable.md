# 🩺 Troubleshooting Service Unreachable & Connectivity Failures

## Symptom
Service IP or DNS name returns connection refused, timeout, or 503.

---

## Diagnostic Flow

```
Service ↓ Selector ↓ Endpoints / EndpointSlices ↓ Pod labels ↓ Container port ↓ TargetPort ↓ NetworkPolicy ↓ DNS
```

### Step 1: Inspect Service Endpoints
```bash
kubectl get endpoints <service-name> -n <namespace>
```
*If `ENDPOINTS` displays `<none>`, the Service selector does not match any running Pod labels.*

### Step 2: Compare Selector vs Pod Labels
```bash
# Check Service selector
kubectl get svc <service-name> -n <namespace> -o jsonpath='{.spec.selector}'

# Check Pod labels
kubectl get pods -n <namespace> --show-labels
```

### Step 3: Verify Container Port & TargetPort Match
Ensure Service `targetPort` matches the container's `containerPort` listening port inside the application.

### Step 4: Test Internal DNS Resolution
```bash
kubectl run net-test --rm -it --image=busybox -- nslookup <service-name>.<namespace>.svc.cluster.local
```

### Safety Rating: 🟢 Safe
