#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 13:09:02 2023

@author: johannes


Filhåndtering: Skriv et program som leser inn ei fil som inneholder en serie med flyttall. Anta
at flyttallene er avstander i kilometer. For hvert tall skal du bruke funksjonen fra øving 3
oppgave b til å konvertere avstanden til nautiske mil. 


Deretter skal programmet skrive ut avstanden i nautiske mil til ei ny fil. 
Brukeren av programmet skal oppgi navn på den første 
fila og navn på den andre fila. Bruk den vedlagte fila 
«oving_6_testfil.txt» for å teste koden din.

"""

def km_til_naut(avstand_km):
    avstand_naut = round(avstand_km / 1.852, 2)
    return avstand_naut


# Åpner filen med flyttall.
#ekstern_liste = open("oving_6_testfil.txt", "r") 


with open(input("Skriv inn filnavnet til fila du vil åpne: "), "r") as ekstern_liste: #importerer den med et alias for å kunne behandle den videre
    entries = (ekstern_liste.readline(0)) #fikk ikke med første entry uten å skrive 0 i readline()


    filnavn = input("Skriv inn navnet på fila du vil opprette: ") #Bruker skriver inn navn på ny fil
    with open(filnavn, "w", encoding="UTF8") as ny_fil: #Ny fil opprettes med aliaset ny_fil videre i scriptet
        for entries in ekstern_liste:
            entries = float(entries)
            
            
            ny_fil.write(f"{entries} km = {km_til_naut(entries)} nautiske mil\n")
        # ny_fil.close() #for-loopen skriver inn alle entries i den nye fila, før den lukkes. Hadde ikke trengt dette med with-løkka


    
ekstern_liste.close() #avslutter scriptet med å lukke fila med flyttall.