import os

def prometheus():
    os.system("cd tmp && kubectl apply -f deployment-prometheus.yaml && kubectl apply -f svc.yaml && kubectl apply -f configMapPrometheus.yaml && kubectl apply -f clusterRolePrometheus.yaml")
    os.system("Prometheus Adicionado a sua cluster")