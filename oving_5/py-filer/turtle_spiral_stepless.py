#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 09:56:47 2023

@author: johannes
"""


import turtle
turtle.speed(0)
turtle.Screen().bgcolor("black")


### DEFINERER NOEN VARIABLER
x = 3
bigger_box = x*1.05
farge_liste = ["red", "yellow", "green", "blue"]
stepless_colors_list = [] #RRGGBB, hver går fra 
vinkel = 5
#kanter = 4


def firkant(x, farge):
    # FRA SENTRUM TIL HJØRNE
    turtle.penup()
    turtle.right(90)
    turtle.forward(x/2)
    turtle.right(90)
    turtle.forward(x/2)
    turtle.right(180)
    turtle.pendown()
    
    # SELVE FIRKANTEN
    for i in range(0, 4):
        turtle.pencolor(farge_liste[farge])
        turtle.forward(x)
        turtle.left(90)
    
    # FRA HJØRNE TIL SENTRUM
    turtle.penup()
    turtle.forward(x/2)
    turtle.left(90)
    turtle.forward(x/2)
    turtle.right(90)




### KJØRER FIRKANTEN

for j in range(1, 84):
    x = x    
    firkant(x, farge)
    turtle.right(vinkel)
    x = x + bigger_box
    farge = 
    

turtle.exitonclick()
turtle.done()


