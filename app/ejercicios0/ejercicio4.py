import re

def apellido_n(string):
	match = re.search("[A-z]+ [A-Z]",string)

	if match != None:
		return string + " cumple el patrón"
	else:
		return string + " no cumple el patrón"


def correo(string):
	match = re.search("\w+@\w+\.[a-z]+",string)

	if match != None:
		return string + ' es un correo válido'
	else:
		return string + ' no es un correo válido'

def tarjeta_credito(string):
	match = re.search("[0-9]{4}((-|\s)[0-9]{4}){3}",string)

	if match != None:
		return string + ' es una tarjeta de credito'
	else:
		return string + ' no es una tarjeta de credito'
