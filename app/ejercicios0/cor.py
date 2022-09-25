# Ejercicio 3

from random import seed
from random import randint

def corchetes(longitud_max):
    longitud = randint(2, longitud_max)
    corchetes = ""

    for i in range(longitud):
        cor_der = randint(0, 1)

        if cor_der == 0:
            corchetes += ']'
        else:
            corchetes += '['

    return  corchetes



def es_correcto(cadena_cor):
    numcor = 0

    for cor in cadena_cor:
        if cor == '[':
            numcor += 1
        else:
            numcor -= 1

            if numcor < 0:
                return cadena_cor + ' no es una cadena válida'

    if numcor == 0:
        return cadena_cor + ' es una cadena válida'
    else:
        return cadena_cor + ' no es una cadena válida'
