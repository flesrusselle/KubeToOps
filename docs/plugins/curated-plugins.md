# 🔌 Curated kubectl Plugins

Evaluated plugins for security, active maintenance, and high operational value.

---

## 1. `kubectl-neat`

### What is it?
Strips boilerplate status, managedFields, creationTimestamps, and default values from exported resource YAML.

```bash
# Installation
kubectl krew install neat

# Usage
kubectl get deployment my-app -o yaml | kubectl neat
```
### Safety Rating: 🟢 Safe

---

## 2. `kubectl-who-can`

### What is it?
Inspects RBAC permissions to answer *"Who can perform verb X on resource Y in namespace Z?"*.

```bash
# Installation
kubectl krew install who-can

# Usage
kubectl who-can delete pods -n production
```
### Safety Rating: 🟢 Safe

---

## 3. `kubectl-images`

### What is it?
Lists all container images currently running across cluster pods or deployments.

```bash
# Installation
kubectl krew install images

# Usage
kubectl images -n default
```
### Safety Rating: 🟢 Safe
