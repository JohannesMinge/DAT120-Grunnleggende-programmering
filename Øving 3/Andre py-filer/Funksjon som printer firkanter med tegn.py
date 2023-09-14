#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 11:10:28 2023

@author: johannes



Algoritme: 
----------------------------------------------------------
1) funksjon som lager figuren
    range y-retning
        range x-retning
            print antall tegn x ganger
        print ny linje som gjør det samme y ganger
2) få inputs fra brukeren på høyde, bredde og tegn
3) lag figuren ved å kalle funksjonen med de brukerbestemte parameterne

"""

def firkant(hoyde, bredde, tegn):
    for y in range(hoyde):
        for x in range(bredde):
            print(tegn, end="")
        print()
        


hoyde = int(input("Høyde: "))
bredde = int(input("Bredde: "))
tegn = input("Tegn: ")

print()
firkant(hoyde, bredde, tegn)