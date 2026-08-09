# 📜 Dry-Run & Manifest Generation

Generating valid Kubernetes YAML manifests manually is error-prone. `kubectl` imperatively generates declarative YAML boilerplates using client-side dry-run flags.

---

## 1. Client Dry-Run (`--dry-run=client`)

### Command
```bash
kubectl create deployment my-app --image=nginx:1.25.4 --dry-run=client -o yaml > deployment.yaml
```

### Breakdown
- `--dry-run=client`: Formats and validates the resource object locally in client memory without sending an HTTP request to the cluster API server.
- `-o yaml`: Output formatted YAML to stdout.

---

## 2. Server Dry-Run (`--dry-run=server`)

### Command
```bash
kubectl apply -f deployment.yaml --dry-run=server
```

### Breakdown
- `--dry-run=server`: Sends the request to the Kubernetes API server to execute admission webhooks, mutating controllers, and schema validation without persisting state changes to etcd.

### Why & When to Use
Use server dry-run to test complex admission policies (OPA Gatekeeper, Kyverno) or admission webhooks before committing changes.

---

## 3. Generating Common Manifests Imperatively

```bash
# Service manifest (ClusterIP)
kubectl expose deployment my-app --port=80 --target-port=8080 --dry-run=client -o yaml > service.yaml

# ConfigMap from literal values
kubectl create configmap app-config --from-literal=ENV=production --dry-run=client -o yaml > configmap.yaml

# Secret (Opaque)
kubectl create secret generic app-secret --from-literal=DB_PASS=s3cr3t --dry-run=client -o yaml > secret.yaml
```

### Safety Rating: 🟢 Safe
