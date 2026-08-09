# 📄 Essential kubectl Command Cheatsheet

Quick reference for essential `kubectl` operational commands.

---

## Resource Inspection
```bash
# Get pods with IP and Node details
kubectl get pods -o wide -n <namespace>

# Stream pod updates
kubectl get pods -w -n <namespace>

# Describe resource events and status
kubectl describe pod <pod-name> -n <namespace>

# Sort events chronologically
kubectl get events --sort-by=.lastTimestamp -n <namespace>
```

---

## Workload Management
```bash
# Gracefully restart deployment pods
kubectl rollout restart deployment/<deployment-name> -n <namespace>

# Scale deployment replicas
kubectl scale deployment/<deployment-name> --replicas=5 -n <namespace>

# View rollout status
kubectl rollout status deployment/<deployment-name> -n <namespace>

# Roll back to previous revision
kubectl rollout undo deployment/<deployment-name> -n <namespace>
```

---

## Logs & Debugging
```bash
# Follow live container logs
kubectl logs -f <pod-name> -c <container-name> -n <namespace>

# Get logs from previous crashed container
kubectl logs <pod-name> --previous -n <namespace>

# Interactive container shell
kubectl exec -it <pod-name> -c <container-name> -n <namespace> -- /bin/sh

# Port-forward service to localhost
kubectl port-forward svc/<service-name> 8080:80 -n <namespace>
```
