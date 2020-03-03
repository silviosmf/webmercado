import sys
import datetime
import random
from flask import Flask, json
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
    print(df)
    # return json.dumps(df[0])
    return (df.to_json())

@app.route('/indices')
def indices():
    df = IndicesColetor.carregarIndicePagina()
    print(df)
    return df.to_json()

app.run(host='localhost', port=5000)
