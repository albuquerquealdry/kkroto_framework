import os

def create(typeCluster):
    os.system("clear")
    os.system(f"kind create cluster --config ./tmp/{typeCluster}.yaml")
    os.system("echo O miserável é um gênio, teste seu k8s com _kubectl get nodes_")

def delete():
    os.system("kind delete cluster")
    os.system("cat ./typos/nervoso.txt")
