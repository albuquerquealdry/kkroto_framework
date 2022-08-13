import os



def create(typeCluster):
    os.path.join('./')
    os.system("ls")
    os.system("clear")
    os.system(f"kind create cluster --config ./$PWD/tmp/{typeCluster}.yaml")
    os.system("echo O miserável é um gênio, teste seu k8s com _kubectl get nodes_")

def delete():
    os.system("kind delete cluster")
    os.system("clear && cat ./typos/nervoso.txt")
