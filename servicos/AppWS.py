import sys
import datetime
import random
from flask import Flask, json,jsonify
from flask_cors import CORS
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
    for ret in retorno:
        print(ret)
        listaMoedas.append(ret)
    return jsonify('listaMoedas[0]')

@app.route('/indices')
def indices():
    df = IndicesColetor.carregarIndicePagina()
    print(df)    
    return (df)

app.run(host='localhost', port=5000)
