import turtle
import time
import random

retraso = 0.1
marcador = 0
marcadorAlto = 0

s = turtle.Screen()
s.setup(650,650)
s.bgcolor("gray")
s.title("Proyecto 2")

serpiente = turtle.Turtle()
serpiente.speed(1)
serpiente.shape("square")
serpiente.penup()
serpiente.goto(0,0)
serpiente.direction = "stop"
serpiente.color("green")

comida = turtle.Turtle()
comida.shape("circle")
comida.color("orange")
comida.penup()
comida.goto(0,100)
comida.speed(0)

cuerpo = []

texto = turtle.Turtle()
texto.speed()
texto.color("black")
texto.penup()
texto.hideturtle()
texto.goto(0,-260)
texto.write("Marcador: 0\tMarcador más alto: 0", align="center",font=("verdana",24,"normal"))
def arriba():
    serpiente.direction = "up"

def abajo():
    serpiente.direction = "down"

def derecha():
    serpiente.direction = "right"

def izquierda():
    serpiente.direction = "left"


def movimiento():
    if serpiente.direction == "up":
        y = serpiente.ycor()
        serpiente.sety(y+20)
    if serpiente.direction == "down":
        y = serpiente.ycor()
        serpiente.sety(y-20)
    if serpiente.direction == "right":
        y = serpiente.xcor()
        serpiente.setx(y+20)
    if serpiente.direction == "left":
        y = serpiente.xcor()
        serpiente.setx(y-20)

s.listen()
s.onkeypress(arriba, "Up")
s.onkeypress(abajo, "Down")
s.onkeypress(derecha, "Right")
s.onkeypress(izquierda, "Left")

while True:
    s.update()

    if serpiente.xcor() > 300 or serpiente.xcor() < -300 or serpiente.ycor() > 300 or serpiente.ycor() < -300:
        time.sleep(2)
        for i in cuerpo:
            i.clear()
            i.hideturtle()
        serpiente.home()
        serpiente.direction = "stop"
        cuerpo.clear()

        marcador = 0
        texto.clear()
        texto.write("Marcador: {}\tMarcador más alto: {}".format(marcador, marcadorAlto), align="center",font=("verdana",24,"normal"))



    if serpiente.distance(comida) < 20:
        x = random.randint(-250,250)
        y = random.randint(-250,250)
        comida.goto(x,y)

        nuevoCuerpo = turtle.Turtle()
        nuevoCuerpo.shape("square")
        nuevoCuerpo.color("green")
        nuevoCuerpo.penup()
        nuevoCuerpo.goto(0,0)
        nuevoCuerpo.speed(0)

        cuerpo.append(nuevoCuerpo)

        marcador+=10
        if marcador > marcadorAlto:
            marcadorAlto = marcador
            texto.clear()
            texto.write("Marcador: {}\tMarcador más alto: {}".format(marcador, marcadorAlto), align="center",font=("verdana",24,"normal"))


    total = len(cuerpo)
    for index in range (total -1,0,-1):
        x = cuerpo[index-1].xcor()
        y = cuerpo[index-1].ycor()
        cuerpo[index].goto(x,y)

    if total > 0:
        x = serpiente.xcor()
        y = serpiente.ycor()
        cuerpo[0].goto(x,y)

        

    movimiento()

    for i in cuerpo:
        if i.distance(serpiente) < 20:
            for i in cuerpo:
                i.clear()
                i.hideturtle()
            serpiente.home()
            cuerpo.clear()
    time.sleep(retraso)
    


turtle.done()