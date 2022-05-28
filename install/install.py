import os


def installClusterOperator():
    os.system("curl -L https://get.docker.com/ | bash")
    os.system("usermod -aG docker $USER")
    os.system("curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.8.1/kind-linux-amd64")
    os.system("chmod +x ./kind && sudo mv ./kind /usr/local/bin/")