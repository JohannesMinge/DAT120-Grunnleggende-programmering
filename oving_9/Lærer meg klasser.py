#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 09:09:12 2023

@author: johannes
"""

# LÆRER OM KLASSER

class Person:
    def __init__(self, navn, alder, hobby):
        self.navn = navn
        self.alder = alder
        self.hobby = hobby

Ingrid = Person("Ingrid", 26, "tenke på babyen")
Johannes = Person("Johannes", 25, "stå på ski")
Karsten = Person("Karsten", 27, "kjøre tanks")
Armand = Person("Armand", 27, "se på kniver og klokker på Kickstarter")
Markus = Person("Markus", 28, "weeb")

# print("Hva liker disse tre vennene å gjøre?")
# print(f"Karsten liker å {Karsten.hobby}")
# print(f"Johannes liker å {Johannes.hobby}.")

print(f"Aldersforskjellen mellom Karsten og Johannes er {Karsten.alder-Johannes.alder} år.")
Johannes.alder += 1
print(f"Johannes har hatt bursdag og er nå {Johannes.alder} år gammel!")
print(f"Nå er aldersforskjellen mellom Karsten og Johannes {Karsten.alder-Johannes.alder} år.")


class Avtale:
    def __init__(self, tittel, tidspunkt, sted):
        self.tittel = tittel
        self.tidspunkt= tidspunkt
        self.sted = sted
        
topptur = Avtale("Topptur", "lørdag 09.12.23", "Hunnedalen")
topptur.sted = "Heimre Hunnefjell" #endrer stedet
# print(topptur.sted)


