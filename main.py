__author__ = "Alexandra Gburova && Tomas Sabol"
import turtle
import random

pen = turtle.Turtle()
window = turtle.Screen()

# Window config
window.bgcolor("black")
window.title("solar system")
window.setup(width=1400, height=900)
pen.speed(0)


def sun():
    pen.penup()
    pen.begin_fill()
    pen.fillcolor("#FFD700")
    pen.pencolor("#FFD700")
    pen.goto(0, -50)
    pen.pendown()
    r = 100
    pen.circle(r)
    pen.end_fill()
    pen.penup()
    pen.hideturtle()


def mercury():
    pen.penup()
    pen.begin_fill()
    pen.fillcolor("#D2691E")
    pen.pencolor("#D2691E")
    pen.goto(80, -70)
    pen.pendown()
    r = 10
    pen.circle(r)
    pen.end_fill()
    pen.penup()
    pen.hideturtle()


def venus():
    pen.penup()
    pen.begin_fill()
    pen.fillcolor("#FFE4B5")
    pen.pencolor("#FFE4B5")
    pen.goto(-135, 80)
    pen.pendown()
    r = 13
    pen.circle(r)
    pen.end_fill()
    pen.penup()
    pen.hideturtle()


def earth():
    pen.penup()
    pen.begin_fill()
    pen.fillcolor("#00BFFF")
    pen.pencolor("#00BFFF")
    pen.goto(-10, -130)
    pen.pendown()
    r = 14
    pen.circle(r)
    pen.end_fill()
    pen.penup()

    # land on earth
    pen.goto(-8, -125)
    pen.begin_fill()
    pen.fillcolor("#228B22")
    pen.pencolor("#228B22")
    pen.pendown()
    r = 5
    pen.circle(r)
    pen.goto(-9, -120)
    pen.circle(r)
    pen.end_fill()
    pen.hideturtle()


def mars():
    pen.penup()
    pen.begin_fill()
    pen.fillcolor("#FF4500")
    pen.pencolor("#FF4500")
    pen.goto(80, 180)
    pen.pendown()
    r = 14
    pen.circle(r)
    pen.end_fill()
    pen.penup()
    pen.hideturtle()


def jupiter():
    pen.penup()
    pen.begin_fill()
    pen.fillcolor("#FFEBCD")
    pen.pencolor("#FFEBCD")
    pen.goto(-120, 200)
    pen.pendown()
    r = 40
    pen.circle(r)
    pen.end_fill()
    pen.penup()
    pen.hideturtle()


def saturn():
    pen.penup()
    pen.begin_fill()
    pen.fillcolor("#FAF0E6")
    pen.pencolor("#FAF0E6")
    pen.goto(250, -50)
    pen.pendown()
    r = 30
    pen.circle(r)
    pen.end_fill()
    pen.penup()


def uranus():
    pen.penup()
    pen.begin_fill()
    pen.fillcolor("#20B2AA")
    pen.pencolor("#20B2AA")
    pen.goto(-250, -20)
    pen.pendown()
    r = 18
    pen.circle(r)
    pen.end_fill()
    pen.penup()


def neptune():
    pen.penup()
    pen.begin_fill()
    pen.fillcolor("#0000CD")
    pen.pencolor("#0000CD")
    pen.goto(-280, -200)
    pen.pendown()
    r = 19
    pen.circle(r)
    pen.end_fill()
    pen.penup()


def star():
    for i in range(100):     # specific number of stars
        x = random.randint(-650, 650)
        y = random.randint(-350, 350)
        pen.goto(x, y)
        pen.pendown()
        pen.color("#F3F3F3")
        pen.fillcolor("#F3F3F3")
        for i in range(5):
            pen.forward(3)
            pen.right(30)
            pen.right(130)
            pen.forward(3)
            pen.left(90)
        pen.penup()
        pen.hideturtle()


sun()
mercury()
venus()
earth()
mars()
jupiter()
saturn()
uranus()
neptune()
star()

window.mainloop()
