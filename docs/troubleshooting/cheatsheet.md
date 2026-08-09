# 📄 Troubleshooting Commands Cheatsheet

```bash
# Check pod status and restart count
kubectl get pods -n <namespace>

# Describe pod events & last state exit code
kubectl describe pod <pod-name> -n <namespace>

# Logs from previous crashed container instance
kubectl logs <pod-name> --previous -n <namespace>

# Chronological event log
kubectl get events --sort-by=.lastTimestamp -n <namespace>

# Check service endpoints mapping
kubectl get endpoints <service-name> -n <namespace>

# Top resource utilization
kubectl top pods -n <namespace>
```
