# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 10:45:33 2021

@author: Erlend Tøssebro
"""

fortsetter = True

while fortsetter:
    prosentscore = int(input("Skriv inn en prosentscore: "))
    if prosentscore < 0:
        fortsetter = False
        break
    if prosentscore >= 90:
        print("A")
    elif prosentscore >= 80:
        print("B")
    elif prosentscore >= 60:
        print("C")
    elif prosentscore >= 50:
        print("D")
    elif prosentscore >= 40:
        print("E")
    else:
        print("F")
    