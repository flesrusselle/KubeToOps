# ⚡ Quick Reference: "I Need This Now"

When operating Kubernetes in production, speed and correctness matter. This page provides instant, copy-pasteable commands for urgent operational tasks, linked directly to full playbooks.

---

## 🚀 Fast Command Index

### 1. Need Pod Logs?
```bash
# Follow logs in real time for a specific container
kubectl logs -f <pod-name> -c <container-name> -n <namespace>
```
👉 Detailed guide: [`docs/debugging/README.md`](debugging/README.md) | Safety: 🟢 Safe

---

### 2. Need Logs from a Previous Crashed Container?
```bash
# Retrieve logs from the instance immediately preceding a crash
kubectl logs <pod-name> --previous -n <namespace>
```
👉 Detailed guide: [`docs/troubleshooting/crashloopbackoff.md`](troubleshooting/crashloopbackoff.md) | Safety: 🟢 Safe

---

### 3. Need Recent Cluster Events Sorted by Timestamp?
```bash
# List events ordered by last timestamp to see recent failures
kubectl get events --sort-by=.lastTimestamp -n <namespace>
```
👉 Detailed guide: [`docs/kubectl/productivity.md`](kubectl/productivity.md) | Safety: 🟢 Safe

---

### 4. Need an Interactive Shell Inside a Running Container?
```bash
# Open an interactive bash/sh session inside a target container
kubectl exec -it <pod-name> -c <container-name> -n <namespace> -- /bin/sh
```
👉 Detailed guide: [`docs/debugging/README.md`](debugging/README.md) | Safety: 🟡 Caution

---

### 5. Need to Restart a Deployment Without Downtime?
```bash
# Trigger a graceful rolling restart of all pods in a deployment
kubectl rollout restart deployment/<deployment-name> -n <namespace>
```
👉 Detailed guide: [`docs/workloads/rollouts.md`](workloads/rollouts.md) | Safety: 🟡 Caution

---

### 6. Need to Roll Back a Failed Deployment?
```bash
# Roll back a deployment to its previous revision
kubectl rollout undo deployment/<deployment-name> -n <namespace>
```
👉 Detailed guide: [`docs/workloads/rollouts.md`](workloads/rollouts.md) | Safety: 🟡 Caution

---

### 7. Need to Switch Cluster Context Safely?
```bash
# List all contexts and switch active context
kubectx
kubectx <target-context-name>
```
👉 Detailed guide: [`docs/contexts/kubectx.md`](contexts/kubectx.md) | Safety: 🟢 Safe

---

### 8. Need to Change Target Namespace in Current Context?
```bash
# Change default namespace for subsequent kubectl commands
kubens <target-namespace>
```
👉 Detailed guide: [`docs/namespaces/kubens.md`](namespaces/kubens.md) | Safety: 🟢 Safe

---

### 9. Need to See Resource Usage (CPU / Memory)?
```bash
# View live CPU and memory utilization of pods
kubectl top pods -n <namespace> --containers

# View node utilization
kubectl top nodes
```
👉 Detailed guide: [`docs/resource-utilization/README.md`](resource-utilization/README.md) | Safety: 🟢 Safe

---

### 10. Need to Inspect Manifest YAML Without Noisy Status Fields?
```bash
# Export clean resource manifest stripped of managedFields and status
kubectl get deployment <name> -n <namespace> -o yaml | kubectl-neat
```
👉 Detailed guide: [`docs/plugins/curated-plugins.md`](plugins/curated-plugins.md) | Safety: 🟢 Safe

---

### 11. Need to Generate Clean Deployment YAML Without Applying?
```bash
# Dry-run deployment generation
kubectl create deployment my-app --image=nginx:latest --dry-run=client -o yaml > deployment.yaml
```
👉 Detailed guide: [`docs/kubectl/dry-run-yaml.md`](kubectl/dry-run-yaml.md) | Safety: 🟢 Safe

---

### 12. Need to See Which Worker Node a Pod Runs On?
```bash
# Output pods with assigned node name and Pod IP
kubectl get pods -o wide -n <namespace>
```
👉 Detailed guide: [`docs/kubectl/productivity.md`](kubectl/productivity.md) | Safety: 🟢 Safe

---

### 13. Need to Test Local Port Connectivity to a Service or Pod?
```bash
# Forward local port 8080 to service port 80
kubectl port-forward svc/<service-name> 8080:80 -n <namespace>
```
👉 Detailed guide: [`docs/networking/README.md`](networking/README.md) | Safety: 🟢 Safe

---

### 14. Need to Discover Nested Resource Schema Fields?
```bash
# Explore deployment specification schema
kubectl explain deployment.spec.template.spec.containers
```
👉 Detailed guide: [`docs/kubectl/explain.md`](kubectl/explain.md) | Safety: 🟢 Safe
