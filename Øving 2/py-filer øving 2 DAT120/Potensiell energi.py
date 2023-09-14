#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 18:26:11 2023

@author: johannes
"""

m = float(input("Skriv inn massen til objektet i kg: "))
h = float(input("Skriv inn høyden til objektet i meter: "))

E_p = round(m*9.81*h)

print("Den potensielle energien til objektet er ", E_p, "joule")