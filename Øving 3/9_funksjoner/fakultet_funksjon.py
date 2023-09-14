# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 10:46:31 2021

@author: Erlend Tøssebro
"""

def les_positivt_heltall(beskjed):
    tall = int(input(beskjed))
    while tall < 0:
        print("Du må skrive inn et ikke-negativt heltall!")
        tall = int(input(beskjed))
    return tall


def fakultet(heltall):
    resultat = 1
    for i in range(1, tallet+1):
        print(i)
        resultat *= i  
    return resultat
    

tallet = les_positivt_heltall("Skriv inn hvilket tall " + 
                              "du ønsker fakultet av: ")
resultat = fakultet(tallet)
print(resultat)
