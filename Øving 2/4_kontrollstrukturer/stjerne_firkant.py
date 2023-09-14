# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 09:41:13 2021

@author: Erlend Tøssebro
"""

hoyde = int(input("Høyde: "))
bredde = int(input("Bredde: "))

for j in range(hoyde):
    for i in range(bredde):
        print("*", end="")
    print()
