import time
from urllib.request import urlopen
from parsel import Selector
from datetime import datetime
import pandas as pd

# import time
# import requests
# import pandas as pd
# from bs4 import BeautifulSoup
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from urllib.request import urlopen
# from parsel import Selector


# Coletar informações do Site utilizando selenium e beautifulsoap

# CHROME_PATH = "C:\\chromedriver\\chromedriver.exe"

# url = "https://br.widgets.investing.com/live-indices?theme=darkTheme&roundedCorners=true&pairs=166,27,172,177,170,175,176,23659,1043106,23658,174,14601,53094,178,179,956501,959210,24441,959206,40823"

# option = Options()
# option.headless = True
# driver = webdriver.Chrome(CHROME_PATH, chrome_options=option)
# driver.get(url)
# time.sleep(5)

# element = driver.find_element_by_xpath("//article[@id='pair_166']//div[@class='hiddenTwo last js-col-last pid-166-last']")
# html = element.get_attribute('outerHTML')
# soup = BeautifulSoup(html,'html.parser')
# print(soup.get_text())
# driver.quit()

def carregarIndicePagina():    
    indices = [] 
    url = "https://br.widgets.investing.com/live-indices?theme=darkTheme&roundedCorners=true&pairs=166,27,172,177,170,175,176,23659,1043106,23658,174,14601,53094,178,179,956501,959210,24441,959206,40823"
    data = datetime.now()
    try:
        html= urlopen(url, timeout=600000).read()    
    except :
        print("Falha na conexão...")
        return None
    
    retorno = str(html.decode("utf-8"))    

    #Obtém as informações do Html da página
    sel = Selector(text=retorno)      

    ind = [166,
        27,
        172,        
        170,
        175,
        176,
        23659,
        1043106,
        23658,
        174,
        14601,
        53094,
        178,
        179,
        956501,
        959210,
        24441,
        959206,
        40823]    

    colunas = ['S&P',
        'FTSE 100',
        'DAX',
        'Russell 2000',
        'Euro Stoxx 50',
        'SMI',
        'AEX',
        'Oslo OBX',
        'CAC 40',
        'IBEX 35',
        'BEL 20',
        'S&P/ASX 200',
        'Nikkei 225',
        'Hang Seng',
        'África do Sul 40',
        'Tadawul All Share',
        'S&P/TSX',
        'Shanghai',
        'STOXX 600']

    df = pd.DataFrame({'Indices':colunas,
        'Index':ind})
    # df.set_index('Index')    
    
    # S&P
    hora = '-1'
    for i in ind:
        cotacao = sel.css('.pid-'+str(i)+'-last::text').get()
        percentual = sel.css('.pid-'+str(i)+'-pcp::text').get()
        hora = sel.css('.pid-'+str(i)+'-time::text').get()
        retorno = str(hora).find(':')
        aberto = True
        if(retorno == -1):
            aberto = False
        indice = {
            'indice':str(df[df.Index == i].Indices.values[0]), 
            'data':data,
            'aberto':aberto,
            'cotacao':cotacao, 
            'percentual':percentual}
        indices.append(indice)
    
    df = pd.DataFrame(indices)
    return df
