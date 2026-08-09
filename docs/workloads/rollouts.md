# 🔄 Workload Rollout Management

Managing Deployment updates safely without service interruptions.

---

## 1. Rolling Restart

Trigger a zero-downtime rolling restart of all pods in a Deployment:

```bash
kubectl rollout restart deployment/web-backend -n default
```
### Safety Rating: 🟡 Caution

---

## 2. Rollout Status Tracking

Monitor rolling update progress until all new replicas are healthy:

```bash
kubectl rollout status deployment/web-backend -n default
```
### Safety Rating: 🟢 Safe

---

## 3. Rollout Revision History & Rollback

```bash
# View rollout revision history
kubectl rollout history deployment/web-backend -n default

# Roll back to previous revision
kubectl rollout undo deployment/web-backend -n default

# Roll back to specific revision
kubectl rollout undo deployment/web-backend --to-revision=2 -n default
```
### Safety Rating: 🟡 Caution

---

## 4. Pausing & Resuming Rollouts

```bash
# Pause rollout to apply multiple spec changes
kubectl rollout pause deployment/web-backend -n default

# Resume rollout after edits complete
kubectl rollout resume deployment/web-backend -n default
```
### Safety Rating: 🟡 Caution
