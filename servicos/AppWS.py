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

@app.route('/', methods=['GET'])
def main():
	return jsonify({'message':'TUDO CERTO'})
    
# @app.route('/moedas');
@app.route('/moedas/<string:sigla_par>', methods=['GET', 'POST'])
def moedas(sigla_par):
    retorno = servicoColetor.consultarMoedasSigla(sigla_par.upper())
    df = pd.DataFrame(retorno)
    listaMoedas = df.drop(columns=['_id'])

    print(listaMoedas)

    # content = request.json
    # print (content['sigla_par'])

    return listaMoedas.to_json(orient='records')

@app.route('/indices')
def indices():
    df = IndicesColetor.carregarIndicePagina()
    print(df)    
    return (df)

app.run(host='localhost', port=5000)
