# Ejercicio 1

# n1      = int(input('Introduce un número: '))

def criba(n1):

    numeros = []
    for i in range(2,n1+1):
        numeros.append((i, True))

    ite = 0

    while numeros[ite][0]**2 < n1:
        multiplo = numeros[ite][0]

        if numeros[ite][1] == True:
            while numeros[ite][0]+multiplo <= n1:
                if numeros[ite+multiplo][1] == True:
                    numeros[ite+multiplo] = (numeros[ite+multiplo][0], False)
            
                multiplo += numeros[ite][0]
            
        ite += 1
    
    salida = []
    for i in numeros:
        if i[1] == True:
            salida.append(i[0]) 

    return salida

