'''
Realizar un programa que conste de una clase llamada Alumno que tenga como atributos el nombre y la nota del alumno. Definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.

'''

class Alumno():
    def __init__(self, nombre, nota):
        self._nombre = nombre
        self._nota = nota
    @property
    def nombre(self):
        print(self._nombre)

    @property
    def nota(self):
        print(self._nota)

    def resultado(self):
        puntaje = ""
        if(self._nota >= 5):
            puntaje = "aprobado"
        else:
            puntaje = "suspenso"

        print("{} ha obtenido una puntuación de {}, está {}".format(self._nombre,self._nota, puntaje))

alumno = Alumno("Pepe", 4)
alumno.resultado()