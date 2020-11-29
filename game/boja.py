#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 16:06:59 2020

@author: TH
"""


import turtle
import random


wn = turtle.Screen()

wn.bgcolor('Black')
wn.title('Bouncing Ball Simulator')

wn.tracer(0)


balls = []


for _ in range(25):
    balls.append(turtle.Turtle())
    
colors = ['red', 'yellow', 'orange', 'purple', 'white', 'green', 'blue']  

shapes = ['circle', 'triangle', 'square']  

for ball in balls:
    # ball = turtle.Turtle()
    ball.shape(random.choice(shapes))
    ball.color(random.choice(colors))
    
    ball.penup()

    ball.speed(0)
    x = random.randint(-290, 290)
    y = random.randint(200, 400)
    ball.goto(x, y)


    ball.dy = 0

    ball.dx = random.randint(-3, 3)
    ball.da = random.randint(-5, 5)

gravity = 0.1

while True:
    
    wn.update()
    
    for ball in balls:
        ball.rt(ball.da)
        ball.dy -= gravity
        
        ball.sety(ball.ycor() + ball.dy)
        
        ball.setx(ball.xcor() + ball.dx)
        
        # Check for a wall collision
        
        if ball.xcor() > 300 or ball.xcor() < -300:
            ball.dx *= -1
            ball.da *= -1
        # Check for a Bounce
        if ball.ycor() < -300:
            ball.sety(-300)
            ball.dy *= -1
            ball.da *= -1

    # Check for collisions between the shapes
    
    for i in range(len(balls)):
        for j in range(i+1, len(balls)):
            # Check for collision
            
            if balls[i].distance(balls[j]) < 20:
                # balls[i].color(random.choice(colors))
                # balls[j].color(random.choice(colors))
                
                # temp_dx = balls[i].dx
                # temp_dy = balls[i].dy
                
                # balls[i].dx = balls[j].dx             
                # balls[i].dy = balls[j].dy
                
                # balls[j].dx = temp_dx
                # balls[j].dy = temp_dy
                
                balls[i].dx, balls[j].dx = balls[j].dx, balls[i].dx
                balls[i].dy, balls[j].dy = balls[j].dy, balls[i].dy
                balls[i].da *= -1
                balls[j].da *= -1
wn.mainloop()    