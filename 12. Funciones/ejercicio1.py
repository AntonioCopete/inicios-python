'''
Crear un programa que tenga una lista, luego crear una funcion con la cual se van a pedir numeros al usuario para agregar a la lista.
Debes crear una segunda funcion en donde se ordenen los numeros pares e impares dentro de dos listas nuevas


'''
lista = [1, 2, 3, 4, 5, 6]
numero = int(input("Introduzca el número para añadir: "))


def añadir(num):
    lista.append(num)
    print(lista)

def ordenar ():
    lista.sort
    pares = []
    impares = []

    for num in lista:
        if(num % 2 == 0):
            pares.append(num)
        else:
            impares.append(num)
    print("Los valores pares son {}".format(pares))
    print("Los valores impares son {}".format(impares))

añadir(numero)
ordenar()
