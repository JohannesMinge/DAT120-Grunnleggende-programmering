#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 11:40:22 2023

@author: johannes
"""

# Regn ut areal og omkrets til en sirkel
# brukeren skal oppgi radius

import math

r = float(input("Skriv inn radius til sirkelen: "))

areal = math.pi * r**2
omkrets = math.pi * 2*r

print("Omkrets = ", round(omkrets, 2))
print("Areal = ", round(areal, 2))