from kind import kind_modules
from ultil import menssage_module
from telemetry import telemetry_module
import sys, questionary, os

def acctionManagement():
    os.system("clear")
    acction = questionary.select(
            "Selecione oque deseja:",
            choices=[
                'Init Cluster',
                'Create Cluster',
                'Delete Cluster',
                'Exit'
            ]).ask()
    
    if(acction == "Init Cluster"):
        kind_modules.kind_module.kind_init_config()
    
    if(acction == 'Create Cluster'):
        clusterType = questionary.select(
            "Selecione o tipo do seu cluster",
            choices=[
                'sayajim',
                'Basic',
                'Exit'
            ]).ask()
        kind_modules.kind_module.kind_create_cluster(clusterType)
    
    if(acction == 'Delete Cluster'):
        kind_modules.kind_module.kind_delete_cluster()
    if (acction == 'Exit'):
        exit()

def methodKubernetes():
    os.system("clear")
    subMethod = questionary.select(
            "Kubernetes Menu:",
            choices=[
                'Cluster Management',
                'Select Context Kubernetes',
                'Exit'
            ]).ask()
    if(subMethod == 'Cluster Management'):
        acctionManagement()

def help():
    menssage_module.menssage_module.help()

def selectCommand():
    os.system("clear")
    method = questionary.select(
            "Selecione oque deseja:",
            choices=[
                'Kubernetes ⭐',
                'Telemetry',
                'Help 💬'
            ]).ask()
    if (method == "Kubernetes ⭐"):
        methodKubernetes()
    
    if (method == 'Help 💬'):
        help()

selectCommand()