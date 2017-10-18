from turtle import *

def draw_star(x, y, points, length, line, fill):
    penup()
    goto(x - (length / 2), y)
    pendown()

    angle = 180 - (360 / points)

    color(line, fill)
    begin_fill()
    for i in range(points):
        forward(length)
        left(angle)
    end_fill()


bgcolor("black")
speed(10)

def teleport(x, y):
    penup()
    goto(x, y)
    pendown()
    
def click_draw(x, y):
    draw_star(x, y , 36, 100, "red", "blue")
    
draw_star(300, 0, 12, 200, "orange", "yellow")

onscreenclick(teleport)

draw_star(xcor(), ycor() , 36, 100, "red", "blue")
