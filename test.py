#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import numpy.random as random
import turtle
from turtle import Turtle
"""
Created on Fri Mar 13 14:13:42 2020

@author: guillemguigoicorominas
"""
"""
import turtle
from turtle import Turtle
window = turtle.Screen()
ball = Turtle()
ball.shape('circle')
ball.color('red')
ball.penup()
ball.speed(0)
ball.goto(0,200)
ball.dy = 0
gravity = 0.1
while True:
    ball.dy -= gravity    
    ball.sety(ball.ycor() + ball.dy)
    if ball.ycor() < -300:
        ball.dy *= -1
    
turtle.mainloop()

"""
class Human(Turtle):
    def __init__(self):
        super(Human, self).__init__()
        #self.x = random.randint(0, dimensions+1)
        #self.y = random.randint(0, dimensions+1)
        #self.goto(self.x, self.y)
        self.dx = 0
        self.dy = 0
        self.count = 0
                
    def accelerate(self):
        self.dy += random.randint(-1,2) * 2
        self.dx += random.randint(-1,2) * 2
        
    def move(self):
        #self.accelerate()
        #self.x += self.speed_x
        #self.y += self.speed_y
        self.sety(self.ycor() + self.dy)
        self.setx(self.xcor() + self.dx)
        self.accelerate()
        self.check_edge()
        
    def check_edge(self):
        if self.ycor() < -300 or self.ycor() > 300:
            self.dy *= -1
        if self.xcor() < -300 or self.xcor() > 300:
            self.dx *= -1

balls = [Human() for i in range(3)]
window = turtle.Screen()

for ball in balls:
    ball.shape('circle')
    ball.color('red')
    ball.penup()
    ball.speed(0)
    #ball.goto(0,200)
    #ball.dy = 0
    #gravity = 0.1

while True:
    for ball in balls:
        ball.move()

turtle.exitonclick()
"""while True:
    ball.dy -= gravity
    ball.sety(ball.ycor() + ball.dy)
    if ball.ycor() < -300:
        ball.dy *= -1"""