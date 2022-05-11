'''
Escribir una clase en python que calcule pow(x, n)

x = es la base

n = es el exponente


'''

class Exponente():
    def __init__(self, x, n):
        self._x = x
        self._n = n

    def calculo(self):
        print(pow(self._x,self._n))

exponente = Exponente(3,5)
exponente.calculo()