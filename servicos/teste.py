from pymongo import MongoClient
import pandas as pd

caminhodb = '189.74.27.85'
portadb = 27017

def salvar(obj):
    client = MongoClient(caminhodb,portadb)
    db = client.GCF

    db.tbl_obj.insert_one(obj)        
    print("---------------")
    print("Objeto salvo")
    print("---------------")
    print(obj)    

def consultar():
    client = MongoClient(caminhodb,portadb)

    try:
        db = client["GCF"]
        tbl_obj = db["tbl_obj"]
        retorno = tbl_obj.find()  
    except:
        False
    return retorno        

def limparBanco():
    client = MongoClient(caminhodb,portadb)
    try:
        db = client["GCF"]
        tbl_obj = db["tbl_obj"]
        tbl_obj.drop()  
    except:
        False

# limparBanco()

# obj = {'nome':'Silvio', 'sobrenome':'Silva Miranda Filho'}
# salvar(obj)
# obj = {'nome':'Bernardo', 'sobrenome':'de Agapito Miranda'}
# salvar(obj)
# obj = {'nome':'Beatriz', 'sobrenome':'de Agapito Miranda'}
# salvar(obj)
# obj = {'nome':'Alline', 'sobrenome':'Ferreira Agapito Miranda'}
# salvar(obj)

retorno = consultar()

df = pd.DataFrame(retorno)
# df.drop(['sobrenome'], axis=1)
novadf = df.drop(columns=['_id'])
objetos = novadf.to_json()
print(objetos)
# for ob in obj:
#     print(ob['nome'])