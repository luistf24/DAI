# Ejercicio 2

def sf(n):
    if n == 0 or n == 1:
        return 1
    else:
        return sf(n-1) + sf(n-2)

def suf():
    entrada = open("./archivos/entrada.txt", "r")
    salida  = open("./archivos/salida.txt", "w")

    numero  = int(entrada.read())

    salida.write(str(sf(numero)))

    entrada.close()
    salida.close()
