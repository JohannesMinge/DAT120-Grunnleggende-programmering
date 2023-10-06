#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 08:44:29 2023

@author: johannes

Unntakshåndtering for filer: Håndter alle unntak som kan oppstå i deloppgave c, inkludert
unntak som oppstår hvis fila inneholder ting som ikke kan tolkes som flyttall. Hvis et tall ikke
kan tolkes som flyttall skal programmet skrive ut hvilken linje som ikke kunne tolkes samt hva
som stod på den linja. Så skal programmet gå til neste linje og fortsette der. Slik vil
programmet produsere ei fil hvor alle gyldige flyttall er konvertert. Bruk den vedlagte fila
«test_utfil_innlagte_feil.txt». Merk at verdien «NaN» er et lovlig flyttall. Det står for «Not a
number» og er resultatet av noen matematiske operasjoner. Merk at Python sjelden gir dette
resultatet. Operasjoner som i for eksempel Java gir NaN som resultat for flyttall vil i Python gi
et komplekst tall, for eksempel hvis man tar kvadratrota av -1. Komplekse tall er pensum i
MAT100.

- Exceptions når innhold i fila som lastes ikke er flyttall 
- Skriv ut hvilken linje + innhold på linja
- Fortsett til neste linje og konverter dermed alle mulige tall i fila 

"""

def km_til_naut(avstand_km):
    avstand_naut = round(avstand_km / 1.852, 2)
    return avstand_naut


# Åpner filen med flyttall.
#ekstern_liste = open("oving_6_testfil.txt", "r") 


with open("oving_6_testfil_innlagte_feil.txt", "r") as ekstern_liste: #importerer den med et alias for å kunne behandle den videre
    entries = (ekstern_liste.readline(0)) #fikk ikke med første entry uten å skrive 0 i readline()
    
    
    #filnavn = input("Skriv inn navnet på fila du vil opprette: ") #Bruker skriver inn navn på ny fil
    x = 1
    with open("ny_fil_med_feil", "w", encoding="UTF8") as ny_fil: #Ny fil opprettes med aliaset ny_fil videre i scriptet
        for entries in ekstern_liste:
            entries = entries.strip() #løser problem med at exceptionen skrev ut newline etter {entries}, og dermed ødela formateringen. 
            try:
                entries = float(entries)
                ny_fil.write(f"{entries} km = {km_til_naut(entries)} nautiske mil\n")
            except:
                ny_fil.write(f"Kunne ikke tolke «{entries}» på linje {x} \n")
            x = x+1 #Fungerer som en teller, som holder styr på linja man er på
            
            
            




































