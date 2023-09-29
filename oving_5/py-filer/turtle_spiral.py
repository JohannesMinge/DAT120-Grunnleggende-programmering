#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 12:58:50 2023

@author: johannes

Man kan bruke relativt enkle Python script med Turtle graphics for å tegne opp ulike 
mønstere. Lag et program som tegner mønsteret på figuren under. Du tegner mønsteret 
ved å tegne en serie med firkanter hvor hver side har ulik farge, hver firkant er 
litt større enn den foregående, og hver firkant er rotert litt i forhold til den 
forrige firkanten. Eksemplet i figuren under bruker fargenavnene red, yellow, green, blue. 
Du trenger ikke å bruke de samme fargene. To eksempler med gråtoner er vist på neste side. 
Du kan gjerne eksperimentere med å bruke ulike farger og se hvordan det ser ut.


- Senter er i sentrum av alle firkantene
- Hver side har en gitt farge
- Hver nye firkant er litt større og litt rotert

Hvordan den fungerer
- Innerste for-loop bygger firkanten med respektive farger
- Ytre for-loop lager ny firkant med økt størrelse og noe rotasjon
    - Må definere sentrum på et vis:
        Alt. 1) Trekk fra (1/2)r* siste side og gå inn 90* tilsvarende
        Alt. 2) Hypotenusen = √(2r**2) 270* fra der turtle kom fra


"""

import turtle
turtle.speed(0)
turtle.Screen().bgcolor("black")


### DEFINERER NOEN VARIABLER
x = 3
bigger_box = x*1.05
farge_liste = ["red", "yellow", "green", "blue"]
vinkel = 5
#kanter = 4


def firkant(x):
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
        turtle.pencolor(farge_liste[i])
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
    firkant(x)
    turtle.right(vinkel)
    x = x + bigger_box

turtle.exitonclick()
turtle.done()

























