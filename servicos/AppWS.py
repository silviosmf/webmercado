import sys
import datetime
import random
from flask import Flask, json,jsonify
from flask_cors import CORS
from flask import request
import pandas as pd
sys.path.insert(0,'./servicoColetor')
import servicoColetor
sys.path.insert(0,'./IndicesColetor')
import IndicesColetor

app = Flask(__name__)

CORS(app)

@app.route('/moedas')
def moedas():
    retorno = servicoColetor.consultarMoedasMongo()
    df = pd.DataFrame(retorno)
    # for ret in retorno:
    #     print(ret)
    # for d in df:
    #     print(d)
    print(df.to_json(orient='records'))
    # j = json.loads(df.to_json())
    return jsonify("{'nome':'silvio'}")

@app.route('/indices')
def indices():
    df = IndicesColetor.carregarIndicePagina()
    print(df)    
    return (df)

app.run(host='localhost', port=5000)
