from kind import kind_modules
from ultil import exceptions
import sys

class select():
    def kind_modulation(self, arg, subarg = ""):
        if(arg == "init"):
            kind_modules.kind_module.kind_init_config()
        if(arg == "create"):
            kind_modules.kind_module.kind_create_cluster(subarg)
        if(arg == "delete"):
            kind_modules.kind_module.kind_delete_cluster()

def methodQuestion(method, arg = "", subarg = ""):

    s = select()
    if(method == "kind"):
        s.kind_modulation(arg, subarg)
    else:
        print("Esse método é invalido")
    if(method == "help"):
        e = exceptions()
        e.exeception.generic_erro()

if len(sys.argv) == 4:
    try:   
        methodQuestion(sys.argv[1] , sys.argv[2] , sys.argv[3])
    except:
        print("[FATAL]: Erro, revise o seu método e seus argumentos")

if len(sys.argv) == 3:
    try:   
        methodQuestion(sys.argv[1] , sys.argv[2])
    except:
        print("[FATAL]: Erro, revise o seu método e seus argumentos")

