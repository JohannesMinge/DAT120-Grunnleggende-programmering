#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 12:54:25 2023
@author: johannes


Oppgaver:
Gitt ei liste over antall sykkelpasseringer på noen målepunkter. Fila heter "sykkelpasseringer.txt"
og har følgende format:
id målepunkt;navn målepunkt;dato;antall passeringer
Du kan anta at denne fila ligger i samme mappe som Python scriptet.

a) Lag et Python script som leser denne fila og regner ut totalt antall passeringer (8%)

b) Endre scriptet slik at du kan skrive inn navn på en målestasjon og så regner den ut antall
passeringer bare for denne målestasjonen (3%)

c) Endre scriptet slik at du i tillegg kan skrive inn en måned og så regner den ut antall passeringer
den måneden for den målestasjonen. Du kan anta at datoen ligger som tekst i formatet ÅÅÅÅ- MM-DD (fire siffer for år - to siffer for måned - to siffer for dag) (3%)

d) Håndter exceptions som kan oppstå under lesing av fila. Linjer i fila som har feil format skal den
hoppe over (4%)
"""

# id målepunkt;navn målepunkt;dato;antall passeringer 



# Oppg. a) regn ut totalt antall passeringer
with open("sykkelpasseringer_2.txt", "r", encoding="UTF8") as fila:
    fila.readline()
    sum_passeringer = 0
    
    for linje in fila:
        try:
            komponenter = linje.split(";")
            passeringer = int(komponenter[3])
            sum_passeringer += passeringer
        except:
            continue
        
    print(f"Total antall passeringer: {sum_passeringer}")
    


# Oppg. b) totalt antall passeringer for bestemt målestasjon

maalepunkt = "Hafrsfjord" #input("Hvilken målestasjon vil du bruke? Hafrsfjord, Mosvannet eller Hillevaag? ")

with open("sykkelpasseringer_2.txt", "r", encoding="UTF8") as fila:
    fila.readline()
    sum_passeringer = 0
    
    for linje in fila:
        try:
            komponenter = linje.split(";")
            
            if maalepunkt == komponenter[1]:
                passeringer = int(komponenter[3])
                sum_passeringer += passeringer
        except: continue
        
    print(f"Antall passeringer for {maalepunkt}: {sum_passeringer}")



# Oppg. c) Regne ut for spesifikke måneder

maalepunkt = "Mosvannet" #input("Hvilken målestasjon vil du bruke? Hafrsfjord, Mosvannet eller Hillevaag? ")
mnd_bruker = "08"

with open("sykkelpasseringer_2.txt", "r", encoding="UTF8") as fila:
    fila.readline()
    sum_passeringer = 0
    
    for linje in fila:
        try:
            komponenter = linje.split(";")
            dato_komponenter = linje.split("-")
            
            if maalepunkt == komponenter[1] and mnd_bruker == dato_komponenter[1]:
                passeringer = int(komponenter[3])
                sum_passeringer += passeringer
        except: continue
        
    print(f"Antall passeringer for {maalepunkt} i måned {mnd_bruker}: {sum_passeringer}")







