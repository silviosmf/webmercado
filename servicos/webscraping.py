import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

url = "https://stats.nba.com/players/traditional/"
CHROME_PATH = "C:\\chromedriver\\chromedriver.exe"

option = Options()
option.headless = False
driver = webdriver.Chrome(CHROME_PATH,chrome_options=option)

# driver = webdriver.Chrome(options=option)
driver.get(url)
time.sleep(5)

driver.find_element_by_xpath("//div[@class='nba-stat-table']//table//thead//tr//th[@data-field='FG3M']").click()
element = driver.find_element_by_xpath("//div[@class='nba-stat-table']//table")
html_content = element.get_attribute('outerHTML')

soup = BeautifulSoup(html_content,'html.parser')
table = soup.find(name='table')

df_full = pd.read_html(str(table))[0].head(50)

print('------------')
print(df_full)
# soup = BeautifulSoup(retorno, 'html.parser')
# table = soup.find(name='table')

# df_full = pd.read_html(str(table))[0].head(10)
# df = df_full[['Unnamed:0', 'PLAYER', 'TEAM', 'PTS']]
# df.columns = ['pos','player','team','total']

# print(df)

driver.quit()