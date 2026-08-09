# 🐞 Advanced Container Debugging

Techniques for deep container inspection, interactive debugging, and port forwarding.

---

## 1. Ephemeral Debug Containers (`kubectl debug`)

When a distroless or minimal container lacks basic diagnostic utilities (`curl`, `sh`, `netstat`), attach an ephemeral debug container into the pod's process namespace:

```bash
kubectl debug -it <pod-name> -n <namespace> --image=nicolaka/netshoot --target=<container-name>
```

---

## 2. Interactive Shell Execution

```bash
kubectl exec -it <pod-name> -c <container-name> -n <namespace> -- /bin/sh
```

---

## 3. Local Port Forwarding

```bash
kubectl port-forward svc/my-service 8080:80 -n <namespace>
```
