import smtplib
def sendmail(erro):
	de = "python@pado.com.br"
	para  = "marcio.ferreira@pado.com.br".split()

	msg = ("From: %s\r\nTo: %s\r\n\r\n"
		% (de, ", ".join(para)))

	line = erro
	msg = msg + line

	server = smtplib.SMTP('correio.pado.com.br')
	server.sendmail(de, para, msg)
	server.quit()