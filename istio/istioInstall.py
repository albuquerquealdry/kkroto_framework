import os


os.chdir('../kkroto_framework')
def play():
    os.system("cd tmp && curl -L https://istio.io/downloadIstio | sh -")
    os.system("cd tmp && cd istio-1.13.4 && export istioctl=$PWD/bin:$PATH")
def delete():
    os.system("eho teste")
    # os.system("kind delete cluster")
    # os.system("clear && cat ./typos/nervoso.txt")
