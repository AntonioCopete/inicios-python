'''
Realizar un programa en el cual se declaren dos valores enteros por teclado utilizando el método __init__. 
Calcular después la suma, resta, multiplicación y división. 
Utilizar un método para cada una e imprimir los resultados obtenidos. Llamar a la clase Calculadora.


'''

class Calculadora():
    def __init__(self) :
        self._x = int(input("Introduzca el primer número: "))
        self._y = int(input("Introduzca el segundo número: "))

    def suma(self):
        return self._x+self._y

    def resta(self):
        return self._x-self._y

    def producto(self):
        return self._x*self._y

    def division(self):
        return self._x/self._y


calculadora = Calculadora()
print(calculadora.suma())
print(calculadora.resta())
print(calculadora.producto())
print(calculadora.division())

