#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 15:09:24 2023

@author: johannes

Skriv et Python program som regner ut arealet til en serie med sirkler. Det skal starte med en
sirkel med radius 1, deretter radius 2 og så videre. Brukeren skal oppgi antall sirkler til en input-
setning. En eksempel-utskrift hvis brukeren skriver inn 10 er oppgitt under. (5%)

"""


import math

print("Radiusen (r) til sirkler fra r=1 til r=n")
n = int(input("Hvor stor skal største sirkel være? "))

for i in range(1, n+1):
    radius = i
    areal = math.pi*i**2
    print(f"Areal for sirkel med radius {i} er {areal}.")