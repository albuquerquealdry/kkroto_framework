class menssage_module():
    def help():
        print(""" 
                        [KKROTO HELP]

Revise seus métodos e Argumentos se quiser ser um guerreiro sayajim:                    
--------------------------Métodos-----------------------------------  
# kind:
descrição : Inicia o seu cluster kubernetes local usando os métodos do kind
    
    --Args:
    ---------------------------------------------------------
    init -> Inicia as configurações do kind na sua instância.
            
        uso : kkroto kind init
            
    --------------------------------------------------------
    create -> Cria o cluster na sua instância
            
        uso : kkroto kind create sayjim
            --------------------------------------------------------
    
    delete -> Cria o cluster na sua instância
            
        uso : kkroto kind delete

# telemetry:
descrição : Inicia telemetria no cluster
    -- Args;
    ---------------------------------------------------------
    init -> Cria o namespace de telemetria no cluster.
 
  """)

