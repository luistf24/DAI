# Ejercicio 3

from random import seed
from random import randint

def corchetes():

    aleatorio = randint(0, 1)

    S       = []
    A       = []
    B       = []
    salida  = ""

    S.append(("[", 'A'))
    S.append(("", 'B'))

    A.append(("]", 'B*'))
    A.append(("]", '*B'))

    B.append(("[", '*A'))
    B.append(("", 'E'))

    fin     = True
    actual  = S[aleatorio]

    while fin:
        if actual[1] == 'A':
            salida = actual[0] + salida
            actual = B[randint(0, 1)]

        elif actual[1] == '*A':
            salida = actual[0] + salida
            actual = A[randint(0, 1)]

        elif actual[1] == 'B':
            actual = B[randint(0, 1)]

        elif actual[1] == 'B*':
            salida = salida + actual[0] 
            actual = B[randint(0, 1)]

        elif actual[1] == '*B':
            salida = actual[0] + salida
            actual = B[randint(0, 1)]

        else:
            actual = 'E'
            fin = False

    return salida



