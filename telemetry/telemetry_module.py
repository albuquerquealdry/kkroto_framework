import os

class telemetry_module():
    def init_telemetry(self):
        print("chegou")
        os.system(" kubectl create ns telemetry")
    
    def prometheus(self):
        os.system("kubectl apply -f ./manifests/prometheus -n telemetry")
    
    def grafana(self):
        os.system("kubectl apply -f ./manifests/grafana -n telemetry")
