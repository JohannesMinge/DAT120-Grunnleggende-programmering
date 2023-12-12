#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 12:42:24 2023

@author: johannes
"""

# Regner ut arealet til en ellipse
import math

a = int(input("Skriv inn største radius til elipsen: "))
b = int(input("Skriv inn minste radius til elipsen: "))

elipse = math.pi*a*b
print(elipse)