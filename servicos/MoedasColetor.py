import time
from urllib.request import urlopen
from parsel import Selector
from pymongo import MongoClient
from datetime import datetime
# from Classes import Moeda, PacoteMoedas



#-----------------------
#Cria e insere valores nas tabelas de Moedas
# NÃO ESTÁ SALVANDO AS COTAÇÕES
#-----------------------

# def salvarPacotemoedaMongoDB(pacote):
#     if(pacote == None):
#         print("lista de câmbios vazia")
#         return

#     client = MongoClient(Variaveis.caminhodb,27017)
#     db = client["GCF"]    

#     moedas = []
#     for moeda in pacote._listamoeda:
#         moedas.append({"sigla":moeda._sigla, "cotacao":moeda._cotacao, "porcentagem":moeda._porcentagem})

#     pacoteInsercao = {"dia":pacote._dia,"hora":pacote._hora, "listamoeda":moedas}

#     db.tbl_pacotemoeda.insert_one(pacoteInsercao)

#-----------------------
# Fim - Cria e insere valores em uma tabela no MongoDB
#-----------------------

#-----------------------------------
# Carregar Dados do EURO
#-----------------------------------
def carregarMoedaPagina():    
    moedas = [] 
    data = datetime.now()
    try:
        html= urlopen("https://br.widgets.investing.com/live-currency-cross-rates?theme=darkTheme&pairs=2103,3,4,7,2090,2091,2103,2112,2124,2126,39,2177,962711,41,18,17,2111,160,2110", timeout=600000).read()    
    except :
        print("Falha na conexão...")
        return None
    
    retorno = str(html.decode("utf-8"))    

    #Obtém as informações do Html da página
    sel = Selector(text=retorno)      

    # # Real
    # cotacao = sel.css('.pid-2103-bid::text').get()
    # percentual = sel.css('.pid-2103-pcp::text').get()
    # hora = sel.css('.pid-2103-time::text').get()
    # retorno = hora.find(':')
    # aberto = True
    # if(retorno == -1):
    #     aberto = False
    # moeda = {
    #     'sigla':"BRL", 
    #     'data':data,
    #     'aberto':aberto,
    #     'cotacao':cotacao, 
    #     'percentual':percentual}
    # moedas.append(moeda)

    # Euro
    cotacao = sel.css('.pid-2124-bid::text').get()
    percentual = sel.css('.pid-2124-pcp::text').get()
    hora = sel.css('.pid-2124-time::text').get()
    retorno = hora.find(':')
    aberto = True
    if(retorno == -1):
        aberto = False
    moeda = {
        'sigla':"EUR", 
        'data':data,
        'aberto':aberto,
        'cotacao':cotacao, 
        'percentual':percentual}
    moedas.append(moeda)

     
    # # Libra Esterlina
    # cotacao = sel.css('.pid-2126-bid::text').get()
    # percentual = sel.css('.pid-2126-pcp::text').get()
    # hora = sel.css('.pid-2126-time::text').get()
    # retorno = hora.find(':')
    # aberto = True
    # if(retorno == -1):
    #     aberto = False
    # moeda = {
    #     'sigla':"GBP", 
    #     'data':data,
    #     'aberto':aberto,
    #     'cotacao':cotacao, 
    #     'percentual':percentual}
    # moedas.append(moeda)


    # # Iene Japones
    # cotacao = sel.css('.pid-3-bid::text').get()
    # percentual = sel.css('.pid-3-pcp::text').get()
    # hora = sel.css('.pid-3-time::text').get()
    # retorno = hora.find(':')
    # aberto = True
    # if(retorno == -1):
    #     aberto = False
    # moeda = {
    #     'sigla':"JPY", 
    #     'data':data,
    #     'aberto':aberto,
    #     'cotacao':cotacao, 
    #     'percentual':percentual}
    # moedas.append(moeda)
             

    # # Franco Suíço
    # cotacao = sel.css('.pid-4-bid::text').get()
    # percentual = sel.css('.pid-4-pcp::text').get()
    # hora = sel.css('.pid-4-time::text').get()
    # retorno = hora.find(':')
    # aberto = True
    # if(retorno == -1):
    #     aberto = False
    # moeda = {
    #     'sigla':"CHF", 
    #     'data':data,
    #     'aberto':aberto,
    #     'cotacao':cotacao, 
    #     'percentual':percentual}
    # moedas.append(moeda)

    # # Dólar Canadense
    # cotacao = sel.css('.pid-7-bid::text').get()
    # percentual = sel.css('.pid-7-pcp::text').get()
    # hora = sel.css('.pid-7-time::text').get()
    # retorno = hora.find(':')
    # aberto = True
    # if(retorno == -1):
    #     aberto = False
    # moeda = {
    #     'sigla':"CAD", 
    #     'data':data,
    #     'aberto':aberto,
    #     'cotacao':cotacao, 
    #     'percentual':percentual}
    # moedas.append(moeda)

    # # Peso argentino
    # cotacao = sel.css('.pid-2090-bid::text').get()
    # percentual = sel.css('.pid-2090-pcp::text').get()
    # hora = sel.css('.pid-2090-time::text').get()
    # retorno = hora.find(':')
    # aberto = True
    # if(retorno == -1):
    #     aberto = False
    # moeda = {
    #     'sigla':"ARS", 
    #     'data':data,
    #     'aberto':aberto,
    #     'cotacao':cotacao, 
    #     'percentual':percentual}
    # moedas.append(moeda)

    # # Dólar australiano
    # cotacao = sel.css('.pid-2091-bid::text').get()
    # percentual = sel.css('.pid-2091-pcp::text').get()
    # hora = sel.css('.pid-2091-time::text').get()
    # retorno = hora.find(':')
    # aberto = True
    # if(retorno == -1):
    #     aberto = False
    # moeda = {
    #     'sigla':"AUD", 
    #     'data':data,
    #     'aberto':aberto,
    #     'cotacao':cotacao, 
    #     'percentual':percentual}
    # moedas.append(moeda)

    # # Peso Colombiano
    # cotacao = sel.css('.pid-2112-bid::text').get()
    # percentual = sel.css('.pid-2112-pcp::text').get()
    # hora = sel.css('.pid-2112-time::text').get()
    # retorno = hora.find(':')
    # aberto = True
    # if(retorno == -1):
    #     aberto = False
    # moeda = {
    #     'sigla':"COP", 
    #     'data':data,
    #     'aberto':aberto,
    #     'cotacao':cotacao, 
    #     'percentual':percentual}
    # moedas.append(moeda)

    # # Peso Mexicano
    # cotacao = sel.css('.pid-39-bid::text').get()
    # percentual = sel.css('.pid-39-pcp::text').get()
    # hora = sel.css('.pid-39-time::text').get()
    # retorno = hora.find(':')
    # aberto = True
    # if(retorno == -1):
    #     aberto = False
    # moeda = {
    #     'sigla':"MXN", 
    #     'data':data,
    #     'aberto':aberto,
    #     'cotacao':cotacao, 
    #     'percentual':percentual}
    # moedas.append(moeda)

    # # Sol do Perú
    # cotacao = sel.css('.pid-2177-bid::text').get()
    # percentual = sel.css('.pid-2177-pcp::text').get()
    # hora = sel.css('.pid-2177-time::text').get()
    # retorno = hora.find(':')
    # aberto = True
    # if(retorno == -1):
    #     aberto = False
    # moeda = {
    #     'sigla':"PEN", 
    #     'data':data,
    #     'aberto':aberto,
    #     'cotacao':cotacao, 
    #     'percentual':percentual}
    # moedas.append(moeda)


    # # Rublo Russo
    # cotacao = sel.css('.pid-962711-bid::text').get()
    # percentual = sel.css('.pid-962711-pcp::text').get()
    # hora = sel.css('.pid-962711-time::text').get()
    # retorno = hora.find(':')
    # aberto = True
    # if(retorno == -1):
    #     aberto = False
    # moeda = {
    #     'sigla':"RUB", 
    #     'data':data,
    #     'aberto':aberto,
    #     'cotacao':cotacao, 
    #     'percentual':percentual}
    # moedas.append(moeda)

    # # Coroa Sueca
    # cotacao = sel.css('.pid-41-bid::text').get()
    # percentual = sel.css('.pid-41-pcp::text').get()
    # hora = sel.css('.pid-41-time::text').get()
    # retorno = hora.find(':')
    # aberto = True
    # if(retorno == -1):
    #     aberto = False
    # moeda = {
    #     'sigla':"SEK", 
    #     'data':data,
    #     'aberto':aberto,
    #     'cotacao':cotacao, 
    #     'percentual':percentual}
    # moedas.append(moeda)

    # # Lira Turca
    # cotacao = sel.css('.pid-18-bid::text').get()
    # percentual = sel.css('.pid-18-pcp::text').get()
    # hora = sel.css('.pid-18-time::text').get()
    # retorno = hora.find(':')
    # aberto = True
    # if(retorno == -1):
    #     aberto = False
    # moeda = {
    #     'sigla':"TRY", 
    #     'data':data,
    #     'aberto':aberto,
    #     'cotacao':cotacao, 
    #     'percentual':percentual}
    # moedas.append(moeda)

    # # Rand Sul-Africano
    # cotacao = sel.css('.pid-17-bid::text').get()
    # percentual = sel.css('.pid-17-pcp::text').get()
    # hora = sel.css('.pid-17-time::text').get()
    # retorno = hora.find(':')
    # aberto = True
    # if(retorno == -1):
    #     aberto = False
    # moeda = {
    #     'sigla':"ZAR", 
    #     'data':data,
    #     'aberto':aberto,
    #     'cotacao':cotacao, 
    #     'percentual':percentual}
    # moedas.append(moeda)

    # # Yuan Chinês
    # cotacao = sel.css('.pid-2111-bid::text').get()
    # percentual = sel.css('.pid-2111-pcp::text').get()
    # hora = sel.css('.pid-2111-time::text').get()
    # retorno = hora.find(':')
    # aberto = True
    # if(retorno == -1):
    #     aberto = False
    # moeda = {
    #     'sigla':"CNY", 
    #     'data':data,
    #     'aberto':aberto,
    #     'cotacao':cotacao, 
    #     'percentual':percentual}
    # moedas.append(moeda)

    # # Rúpia Indiana
    # cotacao = sel.css('.pid-160-bid::text').get()
    # percentual = sel.css('.pid-160-pcp::text').get()
    # hora = sel.css('.pid-160-time::text').get()
    # retorno = hora.find(':')
    # aberto = True
    # if(retorno == -1):
    #     aberto = False
    # moeda = {
    #     'sigla':"INR", 
    #     'data':data,
    #     'aberto':aberto,
    #     'cotacao':cotacao, 
    #     'percentual':percentual}
    # moedas.append(moeda)

    # # Peso Chileno
    # cotacao = sel.css('.pid-2110-bid::text').get()
    # percentual = sel.css('.pid-2110-pcp::text').get()
    # hora = sel.css('.pid-2110-time::text').get()
    # retorno = hora.find(':')
    # aberto = True
    # if(retorno == -1):
    #     aberto = False
    # moeda = {
    #     'sigla':"CLP", 
    #     'data':data,
    #     'aberto':aberto,
    #     'cotacao':cotacao, 
    #     'percentual':percentual}
    # moedas.append(moeda)

    return moedas

#-----------------------------------
# Fim - Carregar Dados do EURO
#-----------------------------------       

# def carregarPacotemoeda():
#     while True:
#         dataAtual = datetime.now()
#         diaSemana = str(dataAtual.strftime("%w"))
#         dia = str(dataAtual.strftime("%d-%m-%Y")) 
#         hora = dataAtual.strftime("%H:%M")
#         minuto = dataAtual.strftime("%M")
#         if(diaSemana == 6):
#             continue
#         if(int(minuto)%5 == 0):
#             moedas = carregarmoedaPagina(dia, hora, diaSemana)
#             pacote = PacoteMoedas(dia,hora,moedas)
#             salvarPacotemoedaMongoDB(pacote)
#         time.sleep(60)

def carregarPacotemoedaTmp():
    while True:
        moedas = carregarMoedaPagina()
        # pacote = PacoteMoedas(dia,hora,moedas)
        print(moedas)
        print('------------------')
        time.sleep(1)

carregarPacotemoedaTmp()
#carregarPacotemoeda()
