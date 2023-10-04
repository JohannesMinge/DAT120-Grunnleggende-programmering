#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 09:55:23 2023

@author: johannes
"""

"""
Funksjon uten returverdi: Skriv en funksjon som skriver ut en adresse på et bestemt format. 
Funksjonen skal ta inn navn, gateadresse, postnummer og poststed som parametere 
og skrive ut dette på følgende format:

Til: <Navn>
<Gateadresse> 
<Postnummer> <Poststed>

"""

# Definerer funksjonen
def gateadresse(navn, adresse, postnummer, poststed):
    print(f"\nTil: {navn} \n{adresse} \n{postnummer} {poststed}\n")


# Setter brukerstyrte variabler
navn = str(input("Skriv inn navn: "))
adresse = str(input("Skriv inn adressen: "))
postnummer = str(input("Skriv inn postnummer: "))
poststed = str(input("Skriv inn poststed: "))


# Kjører fuksjonen
gateadresse(navn, adresse, postnummer, poststed)

