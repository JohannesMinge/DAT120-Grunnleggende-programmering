#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 16:00:54 2023

@author: johannes
"""

"""
Skriv et script som beregner verdien av følgende sum:
    
"""
print("Kvadratet av tallene 1 til 10 er:")
# SKRIV UT ALLE TALLENE
for n in range(1, 11):
    n = n**2
    print(f"{n}, ", end="")
    

# SKRIV UT ALLE TALLENE
print("\nSummen av disse tallene er: ", end="")
summen = 0

for n in range(1, 11):
    n = n**2
    summen = summen + n
print(summen)
    

