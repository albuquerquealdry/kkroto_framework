import os
import sys
sys.path
class kind_module():
    def kind_init_config():
        os.system("""/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)""")
        os.system("brew install  kind")
    
    def kind_create_cluster(arg):
        os.system("cd ..")
        os.system(f"kind create cluster --config ~/kkroto_framework/tmp/{arg}.yaml")

    def kind_delete_cluster():
        os.system("kind delete cluster")
