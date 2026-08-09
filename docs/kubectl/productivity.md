# ⚡ kubectl Productivity Patterns

High-velocity Kubernetes engineers leverage built-in `kubectl` output modifiers and formatting flags to inspect cluster state without writing custom scripts.

---

## 1. Stream Pod Status Changes (`-w` / `--watch`)

### Command
```bash
kubectl get pods -n default -w
```

### Breakdown
- `-w` / `--watch`: Keeps stdout open after rendering initial list and streams updates in real time whenever pod status, restart counts, or readiness conditions change.

### Why & When to Use
Use when waiting for a Deployment rollout to complete, monitoring pod startup sequences, or observing CrashLoopBackOff restart cycles. Eliminates repeating `kubectl get pods` in shell loops.

### Safety Rating: 🟢 Safe

---

## 2. All-Namespaces Discovery (`-A` / `--all-namespaces`)

### Command
```bash
kubectl get pods -A
```

### Breakdown
- `-A` / `--all-namespaces`: Scopes the resource request across all isolated cluster namespaces.

### Why & When to Use
Use when locating misconfigured workloads or ingress routing across unknown team namespaces.

### Safety Rating: 🟢 Safe

---

## 3. Extended Resource Details (`-o wide`)

### Command
```bash
kubectl get pods -n default -o wide
```

### Breakdown
- `-o wide`: Appends additional columns including Pod IP address, assigned Node name, NOMINATED NODE, and READINESS GATES.

### Why & When to Use
Essential for network troubleshooting to confirm which physical worker node hosts a pod, or verifying Pod IP assignments.

### Safety Rating: 🟢 Safe

---

## 4. Chronological Event Sorting (`--sort-by`)

### Command
```bash
kubectl get events -n default --sort-by=.lastTimestamp
```

### Breakdown
- `--sort-by=.lastTimestamp`: Orders event objects chronologically using JSONPath field evaluation on event timestamp.

### Why & When to Use
Use when diagnosing cluster incidents to quickly read the most recent warnings, OOM evictions, or scheduling failures.

### Safety Rating: 🟢 Safe

---

## 5. Label Inspection & Filtering (`--show-labels` / `-l`)

### Command
```bash
# Show all labels attached to pods
kubectl get pods -n default --show-labels

# Filter pods by specific label selector
kubectl get pods -n default -l app=web-backend
```

### Breakdown
- `--show-labels`: Appends a `LABELS` column displaying key-value label pairs.
- `-l <selector>`: Filters output to resources matching label query.

### Safety Rating: 🟢 Safe
