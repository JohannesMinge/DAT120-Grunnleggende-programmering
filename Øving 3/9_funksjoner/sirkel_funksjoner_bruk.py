# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 08:52:57 2021

@author: erlen
"""

import sirkel_funksjoner_pakke as aos

radius = float(input("Skriv inn radius til sirkelen: "))
areal = aos.areal_sirkel(radius)
omkrets = aos.omkrets_sirkel(radius)
print(f"Areal: {areal:8.2f}, omkrets: {omkrets:8.2f}")
