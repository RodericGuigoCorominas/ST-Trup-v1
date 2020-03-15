#!/usr/bin/env python3
# -*- coding: utf-8 -*-



#Comentari andreu per veure el commit
import numpy as np
import numpy.random as random
import math
import turtle
from turtle import Turtle
from itertools import combinations
"""
Created on Fri Mar 13 14:13:42 2020



@author: guillemguigoicorominas
"""
class Human(Turtle):
    def __init__(self, infected = False):
        super(Human, self).__init__()
        self.infected = infected
        self.penup()
        self.goto(random.randint(-290, 290), random.randint(-290, 290))
        self.dx = 0
        self.dy = 0
        self.shape('circle')
        self.color(self.setcolor())
        self.speed(0)
                
    def accelerate(self):
        self.dy += random.randint(-1,2) * 0.1
        self.dx += random.randint(-1,2) * 0.1
        
    def move(self):
        self.sety(self.ycor() + self.dy)
        self.setx(self.xcor() + self.dx)
        self.accelerate()
        self.check_edge()
        
    def check_edge(self):
        if self.ycor() < -300 or self.ycor() > 300:
            self.dy *= -1
        if self.xcor() < -300 or self.xcor() > 300:
            self.dx *= -1
    
    def setcolor(self):
        color = 'green'
        if self.infected:
            color = 'red'
        return color
    
    def infect(self):
        self.infected = True
        self.color('red')

window = turtle.Screen()
window.tracer(0)

balls = [Human() for i in range(10)]
balls[0].infect()
global_position = [[ball.xcor(), ball.ycor()] for ball in balls]

while True:
    window.update()
    for ball in balls:
        ball.move()
    for ball_1, ball_2 in combinations(balls, 2):
        distance = math.sqrt(abs((ball_1.xcor()-ball_2.xcor())**2+(ball_1.ycor()-ball_2.ycor())**2))
        if distance < 12:
            if ball_1.infected:
                ball_2.infect()
            if ball_2.infected:
                ball_1.infect()
            ball_1.dx *= -1
            ball_2.dx *= -1
            ball_1.dy *= -1
            ball_2.dy *= -1

turtle.exitonclick()

