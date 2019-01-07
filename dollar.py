import urllib.request
from bs4 import BeautifulSoup
import re

with urllib.request.urlopen('https://www.valor.com.br/valor-data') as response:
   html = response.read()

soup = BeautifulSoup(html,'html.parser') #armazena o conteudo em html

ips = soup.find(id="ticker-data").find_all("span") # procura em toda a HTML a Div Ticker-data dps procuras as Span dentro desta div

patx = ips[2].get_text() # Pega o texto da 2 span

print(patx)

