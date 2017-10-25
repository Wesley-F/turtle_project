from turtle import *
import random

stars = Turtle()
rocket = Turtle()

rocket.shape("rocket")

bgcolor("black")
stars.speed(10000)
points = 36

def draw_star(x, y, points, length, line, fill):
    stars.penup()
    stars.goto(x - (length / 2), y)
    stars.pendown()

    angle = 180 - (360 / points)

    stars.color(line, fill)
    stars.begin_fill()
    for i in range(points):
        stars.forward(length)
        stars.left(angle)
    stars.end_fill()
    
def teleport(x, y):
    stars.penup()
    stars.goto(x, y)
    stars.pendown()
    
def click_draw(x, y):
    teleport(x,y)
    if points >= 36:
        draw_star(x, y , points, 100, "white", "yellow")
    if points < 36:
        draw_star(x, y, points, 50, "white", "grey")

def increase_points():
    global points
    points += 12

def decrease_points():
    global points
    points -= 12

def draw_background():
    for n in range(6):
        stars.penup()
        stars.goto(random.randint(-400, 400), random.randint(-400, 400))
        stars.pendown()

        red_amount   = random.randint( 0,  30) / 100.0
        blue_amount  = random.randint(50, 100) / 100.0
        green_amount = random.randint( 0,  30) / 100.0
        stars.pencolor((red_amount, green_amount, blue_amount))

        circle_size = random.randint(10, 40)
        stars.pensize(random.randint(1, 5))

        for i in range(6):
            stars.circle(circle_size)
            stars.left(60)

        stars.pensize(1)

def rocket():
    while True:
        rocket.left(random.randint(0, 360)
        rocket.forward(random.randint(10, 100)


            
#"""""""""""""""""""""""""""""""""""""#
#"""""""CREATE SEPERATE TURTLES"""""""#
#"""""""""""""""""""""""""""""""""""""#

draw_background()
rocket()
             
listen()    
onkey(increase_points, "Up")
onkey(decrease_points, "Down")
    
onscreenclick(click_draw)
