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
	with urllib.request.urlopen('https://www.valor.com.br/valor-data') as response:
		html = response.read()

	soup = BeautifulSoup(html,'html.parser') #armazena o conteudo em html
	ips = soup.find(id="ticker-data").find_all("span") # procura em toda a HTML a Div Ticker-data dps procuras as Span dentro desta div
	patx = ips[2].get_text() # Pega o texto da 2 span
	abc = str(patx).replace(",",".")
	return abc


def salvarDollar(parametro): 
	cursor_interno = con.cursor()
	# temp = float(parametro)	
	sql = "INSERT INTO PADOPY_DOLLAR_API (VALOR) VALUES (TO_NUMBER({}))".format(parametro)
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
		return lista	

a = getDollarSalvo()
b = getDollar()

if (a == "Pendente"):
	salvarDollar(b)

a = getDollarSalvo()


while True:
	b = getDollar()
	if float(a[0]) == float(b):
		# time.sleep(1800)
		print(a[0],b)
		time.sleep(5)
	else:
		print("Salvando Novo Dollar")
		salvarDollar(b)
		a = getDollarSalvo()



# cur.execute("INSERT INTO PADOPY_DOLLAR_API (VALOR) VALUES ("+abc+")")
# db.commit()
# con.close()
#enviaremail.sendmail("Cotacao Ptax :"+abc)

#PADOPY_DOLLAR_API

# print(abc)

