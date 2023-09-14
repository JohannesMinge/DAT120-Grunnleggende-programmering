#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 09:04:45 2023

@author: johannes


Lag en funksjon som gir fakultet av brukerens tall. Få de til å skrive inn nytt tall hvis de skriver <=0

1) def fakultet(tallet)
    Funksjonen
        for i in range(1, tallet+1)
        print(i)
    Return(fakultet)
2) print())
    


"""


# Lag en funksjon som gir fakultet av brukerens tall. Få de til å skrive inn nytt tall hvis de skriver <=0

def positivt_tall(brukers_tall):
    tallet = int(input(brukers_tall))
    while tallet < 0:
        print("Tallet kan ikke være negativt.\n")
        tallet = int(input(brukers_tall))
    return tallet


def fakultet(brukers_tall):
    resultat = 1
    for i in range(1, tallet+1):
        resultat = resultat *i
    return resultat
    

tallet = positivt_tall("Fakultet av tallet: ")   

resultat = fakultet(tallet) #da bruker funksjon(fakultet) verdien fra funksjon(positivt_tall)
print(f"{tallet}! = {resultat}")