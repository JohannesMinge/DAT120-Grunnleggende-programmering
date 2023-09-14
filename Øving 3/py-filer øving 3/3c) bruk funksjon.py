#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 13:26:09 2023

@author: johannes
"""

"""

c) Bruk av funksjon og repetisjon kontrollstrukturer: Lag et script som bruker 
funksjonen fra oppgave b) til å konvertere en serie med avstander i kilometer 
til nautiske mil. Programmet skal inneholde ei løkke som leser inn en avstand 
i kilometer, bruker funksjonen fra forrige deloppgave til å konvertere den til 
nautiske mil, skriver ut avstanden i nautiske mil, og så går tilbake og leser 
neste avstand. Scriptet skal avslutte hvis brukeren skriver inn 0.

1) importer funksjon 1e
2) bruk funksjonen til å konvertere en serie avstander i km til naut. mil
    - Les inn avstander i km
    - Skriv ut hver avstand før den leser neste
3) Avslutte hvis brukeren skriver 0

"""


from km_til_naut import f_km_til_naut
resultat = 1


while resultat !=0:
    avstand_km = float(input("Skriv inn avstanden i km: "))
    resultat = f_km_til_naut(avstand_km)
    print(f"= {resultat} nautiske mil \n")



