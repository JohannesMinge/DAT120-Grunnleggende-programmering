#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 11:54:23 2023

@author: johannes

Oppgaven går på følgende:
1. Lag en klasse Rom. Hvert objekt av klassen Rom skal ha en romtype, en kapasitet (antall
folk som det er plass til i rommet) og et romnummer. (5%)
2. Lag en funksjon som tar inn ei liste med objekter av klassen Rom samt en kapasitet.
Funksjonen skal returnere ei liste som inneholder alle rommene som har minst denne
kapasiteten. Hensikten er å finne alle rommene som er store nok for en gitt gruppe med folk.
(6%)
3. Lag en __str__ metode for klassen Rom. Metoden skal returnere en streng av typen "Rom:
romnummer av romtype med kapasitet kapasitet" (5%)

"""

class Rom:
    def __init__(self, romtype, kapasitet, romnummer):
        self.romtype = romtype
        self.kapasitet = kapasitet
        self.romnummer = romnummer
        
    def __str__(self):
        return(f"Rom: {self.romnummer} av typen {self.romtype} med kapasitet {self.kapasitet} personer.")
        #returner "Rom: RUMNUMMER av ROMTYPE med KAPASITET" 

Turingsalen = Rom("lesesal", 50, "E454")

print(Turingsalen)

# personer_i_Turingsalen = int(input(f"Hvor mange personer er i rom {Turingsalen.romnummer}? "))
# print(f"{Turingsalen} Med nåværende bruk: {personer_i_Turingsalen} personer, er {personer_i_Turingsalen/Turingsalen.kapasitet*100}% av kapasiteten i bruk.")


rom_1 = Rom(input("Skriv inn nytt rom. \nSkriv inn romtype: "), input("Rommets kapasitet: "), input("Romnummer: "))
print(rom_1)
