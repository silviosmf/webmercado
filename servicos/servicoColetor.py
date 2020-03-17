import time
import sys
sys.path.insert(0,'Persistencia')
import Persistencia


def executar():
    while True:
        #Inicia consultas a cada 5 minuto 
        Persistencia.salvarMoedasMongo()
        Persistencia.salvarIndicesMongo()
        time.sleep(300)

# executar()

# dbMoedas = Persistencia.consultarMoedasMongo()
# for moeda in dbMoedas:
#     print(moeda)

# for m in moeda:
#     print(json.dumps(m))
# df = pd.DataFrame(moedas)
# print(df)

# indices = consultarIndicesMongo()
# df = pd.DataFrame(indices)
# print(df)

# salvarMoedasMongo()
# salvarIndicesMongo()