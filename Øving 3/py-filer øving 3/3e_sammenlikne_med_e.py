#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 13:21:54 2023

@author: johannes


Bruk av funksjon: Funksjonen i forrige deloppgave er en måte å estimere den 
matematiske konstanten e på. Skriv et script som sjekker hvor stor forskjellen 
er mellom kvadratrota av e(x) med default verdier og tallet e. Deretter skriv 
et script som sjekker dette for hver verdi av M mellom 1 og 100, hvor x 
fortsatt har default-verdien 2.


- Sjekk forskjell mellom e_x og e for hver verdi av M mellom 1 og 100
    - Lag en for-loop for alle tall for M
    - Sjekk resultatet opp mot e
    - print(resultat)

"""

import math
#Fakultet av 4: 1*2*3*4


def fakultet(n):
    if n < 0:
        return "Man kan ikke ta fakultet av et tall under 0."
    else:
        n_range = n
        resultat = 1
        for i in range(1, n_range+1):
            resultat = resultat *i
        return resultat
    

def e_x(x=2, M=40):
    summen = 0    
    for j in range(0, M+1):
        tall =  x**j / fakultet(j)
        summen = summen+tall
    return summen

#print((e_x()))



###    SAMMENLIKNE e_x MED e   ###

M = 100
for d in range(1, M):
    e_for_hver_d = math.sqrt(e_x(M = d))
    #print(f"{d}: {e_for_hver_d}")
    differanse = ((math.e - e_for_hver_d) / math.e)
    print(f"M = {d}, differansen er {differanse}%")
    
    


































