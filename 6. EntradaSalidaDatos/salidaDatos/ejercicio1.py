'''
Ejercicio 1

Escribir un programa que solicite al usuario un vocal en minuscula, y luego una letra en mayúsculas. El programa debe convertir la letra en minúscula y la vocal en mayúscula, y al final, deben ser concatenadas ambas


'''

vocal = input("Introduzca vocal minúscula: ")
letra = input("Introduzca letra mayúscula: ")

nuevaVocal = vocal.upper()
nuevaLetra = letra.lower()

print("El resultado es: ", nuevaVocal+nuevaLetra)