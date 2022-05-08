'''
Crear un programa, que tenga una variable con la cadena “Te quiero solo como amigo”, y muestre la siguiente información:

• Imprima los dos primeros caracteres.

• Imprima los tres últimos caracteres.

• Imprima dicha cadena cada dos caracteres. Ej.: Si la cadena fuera “recta” debería imprimir rca

• Dicha cadena en sentido inverso. Ej.: Si la cadena fuera hola mundo! debe imprimir !odnum aloh

• Imprima la cadena en un sentido y en sentido inverso. Ej: Si la cadena es “reflejo” imprime reflejoojelfer.

'''

cadena = "Te quiero solo como amigo"
print("2 primeros caracteres: ", cadena[ : 2])
print("3 últimos caracteres: ", cadena[-3: ])
print("cada dos caracteres(impares): ",cadena[::2])
print("sentido inverso: ", cadena[::-1])
print("sentido normal e inverso: ",cadena+ cadena[::-1])