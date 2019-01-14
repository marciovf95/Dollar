import urllib.request
from bs4 import BeautifulSoup
import re
import enviaremail
import cx_Oracle 
global cursor
import time

try:	
	# con = cx_Oracle.connect('usuario/senha@ip:porta/schema')
	
	cursor = con.cursor()		
except:
	enviaremail.sendmail("BO ao Abrir connect com o Banco")

def getDollar():
	try: 
		with urllib.request.urlopen('https://www.valor.com.br/valor-data') as response:
			html = response.read()

		soup = BeautifulSoup(html,'html.parser') #armazena o conteudo em html
		ips = soup.find(id="ticker-data").find_all("span") # procura em toda a HTML a Div Ticker-data dps procuras as Span dentro desta div
		patx = ips[3].get_text() # Pega o texto da 2 span
		abc = str(patx).replace(",",".")
		teste = float(abc)
		return teste
	except Exception as e:
		s = str(e)
		enviaremail.sendmail("Erro "+s+" <--")
		exit()


def salvarDollar(parametro): 
	cursor_interno = con.cursor()	
	sql = "INSERT INTO PADOPY_DOLLAR_API (VALOR) VALUES (TO_NUMBER({}))".format(parametro)
	enviaremail.sendmail("Novo Dollar Casatrado Valor : "+parametro+" Ptax")
	print(sql)
	cursor_interno.execute(sql)	
	con.commit()
	return "Salvo"


def getDollarSalvo():
	cursor.execute("SELECT MAX(VALOR) KEEP (DENSE_RANK FIRST ORDER BY DATA DESC) VALOR FROM PADOPY_DOLLAR_API WHERE DATA BETWEEN TRUNC(SYSDATE) AND SYSDATE")
	dollarSalvo = cursor.fetchone()
	if(dollarSalvo[0] is None) :
		return "Pendente"
	else:
		lista = list(dollarSalvo)
		return float(lista[0])	


a = getDollarSalvo()
b = getDollar()	


if (a == "Pendente"):
	salvarDollar(b)


a = getDollarSalvo()


while True:
	b = getDollar()
	if float(a) == float(b):		
		print(a,b)
		time.sleep(1800)
	else:
		print("Salvando Novo Dollar")
		salvarDollar(b)
		a = getDollarSalvo()


