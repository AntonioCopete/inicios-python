'''
En la siguiente lista, debes hacer un programa que muestre los valores al usuario, a su vez, debe pedir dos datos y esos que sean ingresados deben ser sustituidos en el primer y segundo lugar:

[20, 50, "Curso", 'Python', 3.14]

'''

lista = [20, 50, "Curso", 'Python', 3.14]
primerDato = input("Introduzca el primer dato: ")
segundoDato = input("Introduzca el segundo dato: ")


lista[0] = primerDato
lista[1] = segundoDato

print("El nuevo valor de la lista es: {}".format(lista))