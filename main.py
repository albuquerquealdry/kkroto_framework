from platform import python_build
import sys
import os
from istio import istioInstall
from k8s import managementCluster
from telemetry import prometheus
from install import install

def cluster(param1, param2):
    if param1 == "create":
        managementCluster.create(param2)
    elif param1 == "delete":
        managementCluster.delete()

def istio(param1):
    if param1 == "play":
        istioInstall.play()

def telemetry(param):
    if param == "run":
        prometheus.prometheus()

def installs():
    install.installClusterOperator()



comand = sys.argv[1]
if comand == "cluster":
    param1 = sys.argv[2]
    param2 = sys.argv[3]
    cluster(param1, param2)
elif comand == "istio":
    param1 = sys.argv[2]
    istio(param1)
elif comand == "telemetry":
    if (sys.argv[2]== "prometheus"):
        telemetry(sys.argv[3])
elif comand == "install":
    installs()
else:
    print("Metodo desconhecido") 