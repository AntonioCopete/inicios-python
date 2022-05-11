'''
Escribir una clase que se llame Areas(). A partir de un constructor se deben pasar los valores de Base y Altura. 
Luego, se debe calcular area de un cuadrado, triangulo y pentagono


'''

class Areas():
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def triangulo(self):
        area = self._x*self._y/2
        print("El área del triángulo es {}".format(area))

    def cuadrado(self):
        area = self._x*self._y
        print("El área del cuadrado es {}".format(area))

    def pentagono(self):
        area = self._x*self._y/5
        print("El área del pentágono es {}".format(area))



area = Areas(3,5)
area.triangulo()
area.cuadrado()
area.pentagono()