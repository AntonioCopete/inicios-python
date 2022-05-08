'''
Ejercicio 1

Crear un programa que pida al usuario una letra, y si es vocal, muestre el mensaje "Es vocal". Sino, decirle al usuario que no es vocal



'''


input = input("Introduzca una vocal: ")
letra = input.lower()


if(letra in "aeiou"):
    print("Es vocal")

else:
    print("No es vocal")