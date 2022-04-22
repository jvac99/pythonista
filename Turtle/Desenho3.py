from turtle import *
import colorsys

t = turtles.Turttle()
s = turtles.Screen()

s.bgcolor('black')
t.speed(0)
n = 36
h = 0
for i in range(30):
    c = colorsys.hsv_to_rgb(h, 1, 0.8)
    h += 1/n
    t.color(c)
    t.circle(180)
    t.left(10)
