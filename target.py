from turtle import Turtle
from random import randint
from math import floor
import time

t1 = Turtle()
circle_radius = 200
circle_inner_radius = 20
circle_diameter = circle_radius * 2
 
def origin_circle(turtle, radius, x, y, wn):
	wn.delay(0)
	turtle.penup()
	turtle.goto(x, y-radius)
	turtle.pendown()
	turtle.fill(True)
	turtle.circle(radius)
	turtle.fill(False)

def draw_bullseye(turtle, x, y, wn):
	color = True
	for radius in range(circle_radius, circle_inner_radius, -40):
		if color:
			turtle.fillcolor("red")
			#print("red")
		else:
			turtle.fillcolor("white")
			#print("white")
		origin_circle(turtle,radius,x,y,wn)
		color = not color

while True:
	t1.speed(0)
	wn = t1.getscreen()
	t1.ht()
	width = wn.window_width()
	height = wn.window_height()
	wn.screensize(width, height, None)
	x = randint( -(width/2) + circle_radius, (width/2) - circle_radius)
	y = randint( -(height/2) + circle_radius, (height/2) - circle_radius)
	print x, y
	print width, height
	draw_bullseye(t1, x, y, wn)
	time.sleep(3)
	t1.clear()
