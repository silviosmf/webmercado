import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from urllib.request import urlopen
from parsel import Selector


# url = "https://br.widgets.investing.com/live-indices?theme=darkTheme&roundedCorners=true&pairs=166,27,172,177,170,175,176,23659,1043106,23658,174,14601,53094,178,179,956501,959210,24441,959206,40823"
url = "https://stats.nba.com/players/traditional/"
html = ''
try:
    html= urlopen(url, timeout=600000).read()    
except :
    print("Falha na conexão...")

# soup = BeautifulSoup(html,'html.parser')
# table = soup.find(name='table')

# df_full = pd.read_html(str(table))
retorno = str(html.decode("utf-8")) 
sel = Selector(text=retorno)   
principal = sel.xpath("//table").get()

print('------------')
print(principal)

# print(table)
# option = Options()
# option.headless = True
# driver = webdriver.Chrome("C:\\chromedriver\\chromedriver.exe")
# driver.get(url)
# time.sleep(5)
# element = driver.find_element_by_xpath("//main[@class='respTbl']")
# print(element)
# driver.find_element_by_xpath("//div[@class='nba-stat-table']//table//thead//tr//th[@data-field='FG3M']").click()
# element = driver.find_element_by_xpath("//div[@class='nba-stat-table']//table")
# html_content = element.get_attribute('outerHTML')

# soup = BeautifulSoup(html_content,'html.parser')
# table = soup.find(name='table')

# df_full = pd.read_html(str(table))[0].head(10)

# print('------------')
# print(df_full)
# soup = BeautifulSoup(retorno, 'html.parser')
# table = soup.find(name='table')

# df_full = pd.read_html(str(table))[0].head(10)
# df = df_full[['Unnamed:0', 'PLAYER', 'TEAM', 'PTS']]
# df.columns = ['pos','player','team','total']

# print(df)

# driver.quit()