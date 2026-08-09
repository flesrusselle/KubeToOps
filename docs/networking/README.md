# 🌐 Kubernetes Networking & Service Diagnostics

Understanding Service routing, EndpointSlices, CoreDNS, NetworkPolicies, and Ingress controllers.

---

## 1. Service Types

- **ClusterIP**: Internal cluster IP (default).
- **NodePort**: Exposes service on static port (30000-32767) across worker nodes.
- **LoadBalancer**: Provisions external cloud provider load balancer.

---

## 2. Endpoint & EndpointSlice Inspection

```bash
# Verify pods registered to Service endpoints
kubectl get endpoints <service-name> -n <namespace>

# View EndpointSlice detailed IP mapping
kubectl get endpointslice -l kubernetes.io/service-name=<service-name> -n <namespace>
```

---

## 3. CoreDNS Diagnostics

```bash
# Check CoreDNS pod status
kubectl get pods -n kube-system -l k8s-app=kube-dns

# Test DNS query inside cluster
kubectl run dns-test --rm -it --image=busybox -- nslookup my-service.default.svc.cluster.local
```
