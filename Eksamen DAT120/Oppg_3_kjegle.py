#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 13:27:33 2023

@author: johannes
"""

# Regn ut volum til kjegle
# Bruker oppgir radius
# Skriv ut volum til kjegle

import math #for å bruke pi mer nøyaktig enn hva jeg husker selv 

radius = int(input("Skriv inn radiusen til kjegla: "))
hoyde = int(input("Skriv inn høyden til kjegla: "))

volum = 1/3 * math.pi * radius**2 * hoyde 

print(f"Volumet til kjegla er: {volum}.")
