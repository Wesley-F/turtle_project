import math
import random
from turtle import *

wesley = Turtle()
tatem = Turtle()
olivia = Turtle()
courtney = Turtle()
veronica = Turtle()
liam = Turtle()
tyler = Turtle()
emma = Turtle()

wesley.speed(50)
wesley.penup()
wesley.goto(0,0)
wesley.pendown()
wesley.setheading(90)
wesley.color('blue')

tatem.speed(50)
tatem.penup()
tatem.goto(0,0)
tatem.pendown()
tatem.setheading(0)
tatem.color('red')

olivia.speed(50)
olivia.penup()
olivia.goto(0,0)
olivia.pendown()
olivia.setheading(270)
olivia.number = 10
olivia.color('green')

courtney.speed(50)
courtney.penup()
courtney.goto(0,0)
courtney.pendown()
courtney.setheading(180)
courtney.number = 10
courtney.color('purple')

veronica.speed(50)
veronica.penup()
veronica.goto(0,0)
veronica.pendown()
veronica.setheading(90)
veronica.number = 10
veronica.color('blue')

liam.speed(50)
liam.penup()
liam.goto(0,0)
liam.pendown()
liam.setheading(0)
liam.number = 10
liam.color('red')

tyler.speed(50)
tyler.penup()
tyler.goto(0,0)
tyler.pendown()
tyler.setheading(270)
tyler.number = 10
tyler.color('green')

emma.speed(50)
emma.penup()
emma.goto(0,0)
emma.pendown()
emma.setheading(180)
emma.number = 10
emma.color('purple')

number = 10

for _ in range(31):
    for _ in range(4):
        wesley.forward(number)
        wesley.left(90)
        tatem.forward(number)
        tatem.left(90)
        olivia.forward(number)
        olivia.left(90)
        courtney.forward(number)
        courtney.left(90)
        veronica.forward(number)
        veronica.right(90)
        liam.forward(number)
        liam.right(90)
        tyler.forward(number)
        tyler.right(90)
        emma.forward(number)
        emma.right(90)
        
    wesley.left(30)
    tatem.left(30)
    olivia.left(30)
    courtney.left(30)
    veronica.right(30)
    liam.right(30)
    tyler.right(30)
    emma.right(30)

    number += 10

