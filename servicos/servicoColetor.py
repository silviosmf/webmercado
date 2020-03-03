import sys
import time
import datetime
from pymongo import MongoClient
from flask import json
sys.path.insert(0,'MoedasColetor')
import MoedasColetor
sys.path.insert(0,'IndicesColetor')
import IndicesColetor

import pandas as pd

caminhodb = '10.217.30.40'
# caminhodb = '189.74.27.85'
# caminhodb = 'localhost'
portadb = 27017

def salvarMoedasMongo():
    client = MongoClient(caminhodb,portadb)
    db = client.GCF

    moedas = MoedasColetor.carregarMoedaPagina()
    db.tbl_moedas.insert_many(moedas)        
    print("---------------")
    print("Moedas Salvas com Sucesso")
    print("---------------")
    print(moedas)    

def consultarMoedasMongo():
    client = MongoClient(caminhodb,portadb)

    try:
        db = client["GCF"]
        tbl_moedas = db["tbl_moedas"]
        # consulta = {"titulo":noticia.titulo}
        # consulta = {'data':{'$gte':ISODate('2020-03-03')}}
        # retorno = tbl_moedas.find()    
        consulta = {"sigla":"EUR"}
        retorno = tbl_moedas.find(consulta)  
    except:
        False
    return retorno        


def salvarIndicesMongo():
    client = MongoClient(caminhodb,portadb)
    db = client.GCF

    indices = IndicesColetor.carregarIndicePagina()
    db.tbl_indices.insert_many(indices)        
    print("---------------")
    print("Indices Salvos com Sucesso")
    print("---------------")
    print(indices)    

def consultarIndicesMongo():
    client = MongoClient(caminhodb,portadb)

    try:
        db = client["GCF"]
        tbl_indices = db["tbl_indices"]
        # consulta = {"titulo":noticia.titulo}
        retorno = tbl_indices.find()    
    except:
        False
    return retorno        



def executar():
    while True:
        #Inicia consultas a cada 5 minuto 
        salvarMoedasMongo()
        salvarIndicesMongo()
        time.sleep(300)


# moedas = consultarMoedasMongo()
# df = pd.DataFrame(moedas)
# print(df)

# indices = consultarIndicesMongo()
# df = pd.DataFrame(indices)
# print(df)

# salvarMoedasMongo()
# salvarIndicesMongo()