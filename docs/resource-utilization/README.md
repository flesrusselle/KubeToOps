# 📊 Resource Utilization & Metrics

Monitoring CPU cores, memory limits, and node capacity using Metrics Server.

---

## 1. Prerequisites

Requires Metrics Server deployed in cluster (`kubectl get deployment metrics-server -n kube-system`).

---

## 2. Pod Metrics Inspection

```bash
# View top pod CPU and memory usage
kubectl top pods -n default

# Detailed breakdown per container
kubectl top pods -n default --containers
```

---

## 3. Node Resource Capacity

```bash
# View node resource utilization
kubectl top nodes
```

---

## 4. Requests vs Limits Mechanics

- **Requests**: Guaranteed resource allocation used by K8s scheduler for node placement.
- **Limits**: Maximum ceiling. Exceeding CPU limit causes throttling; exceeding Memory limit triggers **OOMKilled** termination.

### Safety Rating: 🟢 Safe
