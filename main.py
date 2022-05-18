from platform import python_build
import sys
import os

from click import command
from k8s import managementCluster

def cluster(param1, param2):
    if param1 == "create":
        managementCluster.create(param2)
    elif param1 == "delete":
        managementCluster.delete()

comand = sys.argv[1]
if comand == "cluster":
    param1 = sys.argv[2]
    param2 = sys.argv[3]
    cluster(param1, param2)
elif comand == "clustinho":
    param1 = sys.argv[2]
    param2 = sys.argv[3]
    cluster(param1, param2)
else:
    print("Metodo desconhecido")





