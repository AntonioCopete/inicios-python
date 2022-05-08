'''
Imprimir por pantalla los numeros del 1 al 10, luego, pedir al usuario dos numeros y mostrar el rango de numeros entre ambas cifras


'''

for i in range(1,11):
    print(i)

inicioRango = int(input("Inserte el primer número del rango: "))
finalRango = int(input("Inserte el último número del rango: "))

for i in range(inicioRango, finalRango+1):
    print(i)