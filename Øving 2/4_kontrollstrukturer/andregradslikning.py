# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 15:11:33 2021

@author: ERlend Tøssebro
"""

import math

a = int(input("Skriv inn tallet a: "))
b = int(input("Skriv inn tallet b: "))
c = int(input("Skriv inn tallet c: "))

verditest = b**2 - 4*a*c

if verditest > 0:
    losning1 = (-b + math.sqrt(verditest))/(2*a)
    losning2 = (-b - math.sqrt(verditest))/(2*a)
    print(f"Likningen har to løsninger: {losning1} og {losning2}")
elif verditest == 0:
    losning = (-b)/(2*a)
    print(f"Likningen har en løsning: {losning}")
else:
    print("Likningen har ingen løsninger")
