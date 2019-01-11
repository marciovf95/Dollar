import cx_Oracle 
import myrequire
import enviaremail

# python -m pip install cx_Oracle --upgrade
# https://cx-oracle.readthedocs.io/en/latest/installation.html

def open():
	try:
		
		cursor = con.cursor()		
	except:
		enviaremail.sendmail("BO ao Abrir connect com o Banco")
	finally:
  		print("The 'try except' is finished")
    return cursor 


def close():
	try:
		con.close()
	except:
		enviaremail.sendmail("BO do Boroguido")




