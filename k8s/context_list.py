import os, questionary
import json

os.chdir('kkroto_framework/k8s')

listChoice = []
class context_list():
    def select_context():
        os.system(" ls ./kubeconfig | grep yaml | sed  's/.yaml//g'> tmplist.txt")
        with open("tmplist.txt", "r") as list:
            for item in list:
                listChoice.append(item.rstrip())

        kubeconfig = questionary.select(
                    "Select Cluster",
                    choices=listChoice).ask()
        os.system("ls")
        os.system(f"export KUBECONFIG=$PWD/{kubeconfig}.yaml")