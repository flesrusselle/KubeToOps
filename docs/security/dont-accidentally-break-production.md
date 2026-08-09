# 🛑 Don't Accidentally Break Production

Operational rules and habits to prevent accidental cluster downtime or data loss.

---

## 1. Golden Rules of Production Operation

1. **Rule #1: Check Context Before Executing**: Always verify active context via `kubectl config current-context` or `kubectx`.
2. **Rule #2: Always Use `--dry-run=client` First**: Validate manifest changes locally before sending to cluster.
3. **Rule #3: Never Delete Without Scoping**: Avoid wildcard deletion (`kubectl delete pods --all`).
4. **Rule #4: Separate Credentials**: Maintain distinct `KUBECONFIG` environment files for dev, staging, and production environments.
5. **Rule #5: Use Prompt Indicators**: Integrate `kube-ps1` into your shell prompt so production contexts display in bold red.

---

## 2. Dangerous Commands Matrix

| Command | Danger Level | Mitigation |
| :--- | :--- | :--- |
| `kubectl delete namespace <ns>` | 🔴 **High** | Deletes ALL resources, PVCs, and state inside namespace. |
| `kubectl delete pods --all` | 🔴 **High** | Causes widespread application outage. |
| `kubectl drain <node>` | 🟡 **Medium** | Evicts all pods from worker node; check PodDisruptionBudgets first. |
| `kubectl apply -f .` | 🟡 **Medium** | Recursively applies all YAML files in directory; verify directory contents. |
