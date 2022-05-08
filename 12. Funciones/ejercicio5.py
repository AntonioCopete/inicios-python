'''
Crear un programa que tenga dos funciones, una que contenga el area de un cuadrado con argumentos de base y altura; y la otra el area de un circulo con argumento de radio
'''

base = float(input("Introduzca la base del cuadrado: "))
altura = float(input("Introduzca la altura del cuadrado: "))

def areaCuadrado(base, altura):
    return base*altura

print(areaCuadrado(base,altura))

radio = float(input("Introduzca la radio del circulo: "))

def areaCirculo(radio):
    return 3.14*(radio**2)

print(areaCirculo(radio))