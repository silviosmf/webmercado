import sys
import datetime
import random
from flask import Flask, json,jsonify
from flask_cors import CORS
import pandas as pd
from flask import request
sys.path.insert(0,'./servicoColetor')
import servicoColetor
sys.path.insert(0,'./IndicesColetor')
import IndicesColetor

app = Flask(__name__)

CORS(app)

@app.route('/moedas')
def moedas():
    retorno = servicoColetor.consultarMoedasMongo()
    listaMoedas = []
      
    for m in retorno:
        print(m)
    #     listaMoedas.append(str(d.sigla))
    # j = str(listaMoedas[0])
    return jsonify('listaMoedas')

@app.route('/indices')
def indices():
    df = IndicesColetor.carregarIndicePagina()
    print(df)    
    return (df)

app.run(host='localhost', port=5000)
