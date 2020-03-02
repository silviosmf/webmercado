import sys
from urllib.request import urlopen
from parsel import Selector
from datetime import datetime
import pandas as pd
from urllib.error import URLError

#-----------------------
#Consulta a tabela News ao Banco
#-----------------------
# def consultarNews(noticia):
#     client = MongoClient(Variaveis.caminhodb,27017)

#     try:
#         db = client["GCF"]
#         tbl_news = db["tbl_news"]
#         consulta = {"titulo":noticia.titulo}
#         retorno = tbl_news.find_one(consulta)    
#     except:
#         False
#     return retorno    

#-----------------------
#Consulta ao Banco
#-----------------------
# def consultarNoticia(noticia):
#     client = MongoClient(Variaveis.caminhodb,27017)

#     try:
#         db = client["GCF"]
#         tbl_noticias = db["tbl_noticias"]
#         consulta = {"titulo":noticia.titulo}
#         retorno = tbl_noticias.find_one(consulta)    
#     except:
#         False
#     return retorno    
#-----------------------
#Fim - Consulta ao Banco
#-----------------------


#-----------------------
#Cria e insere valores em uma tabela news no MongoDB
#-----------------------

# def salvarNewsMongoDB(noticias):
#     if(len(noticias) == 0):
#         print("Não possui nenhuma notícia")
#         return

#     client = MongoClient(Variaveis.caminhodb,27017)
#     db = client.GCF

#     conteudo = []

#     # data = "30/01/2020 00:00:00"
#     # data = datetime.strftime(noticia.data, "%d/%m/%Y %H:%M:%S")
#     d = datetime.now()
#     data = str(d.day)+"/"+str(d.month)+"/"+str(d.year)+" "+str(d.hour)+":"+str(d.minute)+":"+str(d.second)
#     dataAtual = datetime.strptime(data, "%d/%m/%Y %H:%M:%S")

#     for noticia in noticias:    
#         consulta = consultarNews(noticia)
#         if consulta:            
#             print ("O Título: "+noticia.titulo+" JÁ ESTÁ NA BASE DE DADOS")        
#         else:            
#             conteudo.append({"fonte":""+noticia.fonte+"","titulo":""+noticia.titulo+"", "link":""+noticia.link+"", 
#             "resumo":""+noticia.resumo+"", "categoria":""+noticia.categoria+"", "data":dataAtual})    

#     if conteudo:
#         db.tbl_news.insert_many(conteudo)        
#         print("NOVAS NOTÍCIAS INSERIDAS")
#         print(conteudo)    

#-----------------------
#Cria e insere valores em uma tabela no MongoDB
#-----------------------

# def salvarNoticiasMongoDB(noticias):
#     if(len(noticias) == 0):
#         print("Não possui nenhuma notícia")
#         return

#     client = MongoClient(Variaveis.caminhodb,27017)
#     db = client.GCF

#     conteudo = []

#     for noticia in noticias:    
#         consulta = consultarNoticia(noticia)
#         if consulta:            
#             print ("O Título: "+noticia.titulo+" JÁ ESTÁ NA BASE DE DADOS")        
#         else:
#             conteudo.append({"fonte":""+noticia.fonte+"","titulo":""+noticia.titulo+"", "link":""+noticia.link+"", "resumo":""+noticia.resumo+"", "categoria":""+noticia.categoria+"", "data":""+str(noticia.data.strftime("%d-%m-%Y %H:%M:%S"))+""})    

#     if conteudo:
#         db.tbl_noticias.insert_many(conteudo)        
#         print("NOVAS NOTÍCIAS INSERIDAS")
#         print(conteudo)    

#-----------------------
# Fim - Cria e insere valores em uma tabela no MongoDB
#-----------------------

#-----------------------------------
# Carregar Dados do Valor Econômico
#-----------------------------------
def carregarValor():
    noticias = []
    try:
        html= urlopen("https://valor.globo.com/ultimas-noticias", timeout=600000).read()    
    except URLError as e:
        print(e)   
        print("Falha na conexão com Valor Econômico")
        return noticias
    
    retorno = str(html.decode("utf-8"))

    #Obtém as informações do Html da página
    sel = Selector(text=retorno)
    titulos = sel.css('.feed-post-body-title').xpath('.//a/text()').getall()
    links = sel.css('.feed-post-body-title').xpath('.//a/@href').getall()
    categorias = sel.css('.feed-post-metadata-section::text').getall()     
    data = datetime.now()

    #Monta a lista de notícias
    conteudo = []    
    for indice in range(len(titulos)): 
        # print(titulos[indice])      
        conteudo.append({"fonte":"Valor Econômico",
            "titulo":""+titulos[indice]+"", 
            "link":""+links[indice]+"", "resumo":" ", 
            "categoria":""+categorias[indice]+"", 
            "data":""+str(data.strftime("%d-%m-%Y %H:%M:%S"))+""})    
    return conteudo
#-----------------------------------
# Fim - Carregar Dados do Valor Econômico
#-----------------------------------           

#-----------------------------------
# Carregar Dados da Reuters
#-----------------------------------
def carregarReuters():
    noticias = []
    try:
        html= urlopen("https://br.reuters.com/news", timeout=600000).read()    
    except URLError as e:
        print(e)   
        print("Falha na conexão com Reuters")
        return noticias
    retorno = str(html.decode("utf-8"))

    sel = Selector(text=retorno)
    titulos = sel.css('.NONE').css('.topStory').xpath('.//h5/a/text()').getall()   
    links = sel.css('.NONE').css('.topStory').xpath('.//h5/a/@href').getall()    
    resumosColeta = sel.css('.NONE').css('.topStory').xpath('.//p/text()').getall()   
    categorias = sel.css('.NONE').css('.moduleHeader').xpath('.//a/text()').getall()   
    data = datetime.now()

    #Limpar resumos
    resumos = []
    for resumo in resumosColeta:        
        if(resumo != '\xa0\n\t\t\t'):
            resumos.append(resumo)
    
    #Monta a lista de notícias
    conteudo = []    
    for indice in range(len(titulos)): 
        # print(titulos[indice])      
        conteudo.append({"fonte":"Reuters",
            "titulo":""+titulos[indice]+"", 
            "link":""+links[indice]+"", 
            "resumo":""+resumos[indice]+"", 
            "categoria":""+categorias[indice]+"", 
            "data":""+str(data.strftime("%d-%m-%Y %H:%M:%S"))+""})    
    return conteudo
#-----------------------------------
# Fim - Carregar Dados da Reuters
#-----------------------------------    


#-----------------------------------
# Carregar Dados do Money Times
#-----------------------------------

def carregarG1():
    noticias = []
    try:
        html= urlopen("http://g1.globo.com/economia/ultimas-noticias.html", timeout=600000).read()    
    except URLError as e:
        print(e)   
        print("Falha na conexão com G1")
        return []        
    retorno = str(html.decode("utf-8"))

    #Obtém as informações do Html da página
    sel = Selector(text=retorno)
    titulos = sel.css('.feed-post-body').css('.feed-post-body-title').css('.feed-post-link').xpath('.//text()').getall()
    links = sel.css('.feed-post-body').css('.feed-post-body-title').css('.feed-post-link').xpath('.//@href').getall()
    resumos = sel.css('.feed-post-body').css('.feed-post-body-resumo').xpath('.//text()').getall()
    categorias = sel.css('.feed-post-body').css('.feed-post-metadata').css('.feed-post-metadata-section').xpath('.//text()').getall()
    datas = sel.css('.feed-post-body').css('.feed-post-metadata').css('.feed-post-datetime').xpath('.//text()').getall()

    #Monta a lista de notícias
    conteudo = []    
    for indice in range(len(titulos)):      
        conteudo.append({"fonte":"G1",
            "titulo":""+titulos[indice]+"", 
            "link":""+links[indice]+"", 
            "resumo":""+resumos[indice]+"", 
            "categoria":""+categorias[indice]+"", 
            "data":""+datas[indice]+""})    
    return conteudo

#-----------------------------------
# Fim - Carregar Dados do Money Times
#-----------------------------------

def carregarNoticias():
    noticias = []
    noticias.extend(carregarReuters())
    noticias.extend(carregarValor())
    noticias.extend(carregarG1())
    print('------------')
    print(noticias)
    return noticias     

carregarNoticias()
