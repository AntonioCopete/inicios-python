'''
Pedir al usuario que ingrese 2 numeros, después, se debe mostrar el rango de esos 2 números, pero, solo imprimiendo los números que sean impares



'''

rangoInicio = int(input("Inserte el número de inicio del rango: "))
rangoFin = int(input("Inserte el número de fin del rango: "))

for i in range(rangoInicio, rangoFin+1):
    if(i % 2 == 0):
        continue
    print(i)