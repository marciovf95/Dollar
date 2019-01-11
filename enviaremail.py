# class ClassName(object):
# 	"""docstring for ClassName"""
# 	def __init__(self, arg):
# 		super(ClassName, self).__init__()
# 		self.arg = arg
		
import smtplib

def sendmail(text):	
	de = "python@pado.com.br"
	para  = "marcio.ferreira@pado.com.br".split()
	# para  = "milton.rossi@pado.com.br".split()

	msg = ("From: %s\r\nTo: %s\r\n\r\n"
		% (de, ", ".join(para)))

	line = text
	msg = msg + line

	server = smtplib.SMTP('correio.pado.com.br')
	server.sendmail(de, para, msg)
	server.quit()