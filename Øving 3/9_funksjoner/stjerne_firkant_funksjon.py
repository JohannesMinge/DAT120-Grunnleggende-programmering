# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 11:22:14 2021

@author: Erlend Tøssebro
"""

def skriv_firkant(hoyde=5, bredde=5, tegn="*"):
    for j in range(hoyde):
        for i in range(bredde):
            print(tegn, end="")
        print()

hoyde = int(input("Høyde: "))
bredde = int(input("Bredde: "))

skriv_firkant(2, 4)
print("\n ny firkant \n")
skriv_firkant(hoyde, bredde, "#")
print("Ferdig")
