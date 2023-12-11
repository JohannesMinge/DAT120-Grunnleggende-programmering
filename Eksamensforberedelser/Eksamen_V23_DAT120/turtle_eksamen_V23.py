#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 14:29:09 2023

@author: johannes
"""

import turtle #OBS! HUSK DETTE!!

bredde = int(input("Skriv inn bredden: "))
lengde = int(input("Skriv inn lengden: "))
farge = input("Skriv inn fargen (på engelsk, så Turtle forstår): ")

turtle.fillcolor(farge)
turtle.begin_fill()

for i in range(2):
	turtle.forward(bredde)
	turtle.left(90)
	turtle.forward(lengde)
	turtle.left(90)

turtle.end_fill()
turtle.done()

# PYTHON KRASJER, OG JEG VET IKKE HELT HVORFOR...