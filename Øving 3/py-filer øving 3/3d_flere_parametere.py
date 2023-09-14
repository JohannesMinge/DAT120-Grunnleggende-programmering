#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 10:50:09 2023

@author: johannes


d) Funksjon med flere parametere: Gitt funksjonen fakultet fra video-forelesningene, 
lag en funksjon som bruker denne funksjonen til å beregne resultatet for summen 
e(x) oppgitt i formelen under. Funksjonen skal ta inn x og M som parametere. 
Bruk x=2 og M=40 som default verdier Funksjonen skal returnere resultatet:

"""

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


print(e_x())


