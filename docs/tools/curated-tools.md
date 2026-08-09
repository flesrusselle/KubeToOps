# 🛠️ Curated External Tools

---

## 1. Stern (Multi-Pod Log Tailer)
- **Purpose**: Tail logs from multiple pods matching regex pattern.
- **Install**: `brew install stern`
- **Example**: `stern "web-api-.*" -n default`

---

## 2. Popeye (Cluster Sanitizer)
- **Purpose**: Scans live cluster and highlights unused resources, missing limits, and security vulnerabilities.
- **Install**: `brew install derailed/popeye/popeye`
- **Example**: `popeye --out standard`

---

## 3. Helm (Package Manager)
- **Purpose**: Manage Kubernetes application releases via Helm charts.
- **Install**: `brew install helm`
- **Example**: `helm list -A`
