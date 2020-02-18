import sys
import asyncio
import websockets
import datetime
import random
from flask import json

sys.path.insert(0,'./MoedasColetor')
import MoedasColetor


async def moedas(websockets, path):
    while True:
        lMoedas = MoedasColetor.carregarMoedaPagina();
        moedas = []
        for moeda in lMoedas:
            moedas.append(
                {
                    'sigla':moeda['sigla'],
                    'data':moeda['data'],    
                    'aberto':moeda['aberto'],
                    'cotacao':moeda['cotacao'],
                    'percentual':moeda['percentual']}        
                )        
            print(moedas)
        jMoedas = json.dumps(moedas)
        print(jMoedas)
        await websockets.send(jMoedas)
        await asyncio.sleep(5)

start_server = websockets.serve(moedas, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
