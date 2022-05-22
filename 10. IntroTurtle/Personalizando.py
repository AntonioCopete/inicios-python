import turtle

s = turtle.Screen()
t = turtle.Turtle()

s.bgcolor("red")
s.title("Proyecto turtle")

t.shapesize(10, 5, 1)
t.shapesize(5,10,1)
t.shapesize(3,3,3)

t.fillcolor("orange")
t.forward(100)

t.pencolor("white")
t.forward(100)

t.color("green", "blue")
t.right(90)
t.forward(100)

t.pensize(5)
t.forward(100)

turtle.done()