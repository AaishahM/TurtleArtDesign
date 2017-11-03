import turtle #brings in turtle
from functions import * #imports all the functions from that file
bob = turtle.Turtle()
turtle.colormode(255) #RGB colors
turtle.bgcolor(0,0,0)
bob.speed(0)

bob.width(1) #pen width
for times in range(350):
    bob.color(0,0,255)
    bob.left(120)
    bob.forward(times * 10)
    
bob.penup()
bob.home()#brings the turtle back to the point where it started(0,0)
bob.pendown()

bob.width(6)
for times in range(100):
    bob.color(times * 2,0,255)
    bob.left(60)
    bob.circle(times * 2)

for times in range(50):
    jump(bob,250,400)
    bob.color(times * 4,0,255)
    bob.left(60)
    bob.circle(times * 1)

for times in range(50):
    jump(bob,500,0)
    bob.color(times * 4,0,255)
    bob.left(60)
    bob.circle(times * 1)

for times in range(50):
    jump(bob,-250,400)
    bob.color(times * 4,0,255)
    bob.left(60)
    bob.circle(times * 1)

for times in range(50):
    jump(bob,-500,0)
    bob.color(times * 4,0,255)
    bob.left(60)
    bob.circle(times * 1)

for times in range(50):
    jump(bob,-250,-400)
    bob.color(times * 4,0,255)
    bob.left(60)
    bob.circle(times * 1)
    
for times in range(50):
    jump(bob,250,-400)
    bob.color(times * 4,0,255)
    bob.left(60)
    bob.circle(times * 1)
