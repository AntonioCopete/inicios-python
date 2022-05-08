'''
Escribir un programa que pida un numero al usuario y muestre las tablas de multiplicar de ese numero



'''
numero = int(input("Escriba el número: "))

i= 0
while i <= 10:
    print("{} x {} es {}".format(numero, i, i*numero))
    i+= 1