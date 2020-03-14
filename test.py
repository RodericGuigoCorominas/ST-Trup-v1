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
    def __init__(self, dimensions):
        super(Human, self).__init__()
        self.dimensions = dimensions
        self.x = random.randint(0, dimensions+1)
        self.y = random.randint(0, dimensions+1)
        #self.goto(self.x, self.y)
        self.speed_x = random.randint(-1,2)
        self.speed_y = random.randint(-1,2)
                
    def accelerate(self):
        self.speed_x += random.randint(-1,2)
        self.speed_y += random.randint(-1,2)
        
    def move(self):
        self.accelerate()
        self.x += self.speed_x
        self.y += self.speed_y
        self.setx(self.x)
        self.sety(self.y)
        #self.check_edge()
        
    def check_edge(self):
        if self.xcor() <= 0 or self.xcor() >= self.dimensions:
            self.speed_x *= -1
        if self.ycor() <= 0 or self.ycor() >= self.dimensions:
            self.speed_y *= -1
            
            
ball = Human(200)
ball.shape('circle')
ball.color('red')
ball.penup()
ball.speed(-5)
"""ball.goto(0,200)
ball.dy = 0
gravity = 0.1"""
while True:
    ball.move()
    
turtle.mainloop()