# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 08:38:10 2021

@author: Erlend Tøssebro
"""

import math

def areal_sirkel(radius):
    areal = math.pi*radius*radius
    return areal


def omkrets_sirkel(radius):
    return 2.0*math.pi*radius
    

radius_streng = input("Skriv inn radius til sirkelen: ")
radius_bruker = float(radius_streng)
areal_global = areal_sirkel(radius_bruker)
print(f"Arealet ble: {areal_global:8.2f}")
omkrets = omkrets_sirkel(radius_bruker)
print(f"Omkretsen ble: {omkrets:8.2f}")
