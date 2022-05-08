'''
Escribir una función que reciba un número entero positivo y devuelva su factorial.

'''

numero = abs(int(input("Introduzca un número positivo: ")))

def getFactorial(num):
    factorial = 1
    for i in range(1, num+1):
        factorial = factorial*i
    
    print(factorial)


getFactorial(numero)