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

def gateadresse(person):
    navn = input("Navn: ")
    adresse = input("Gateadresse: ")
    postnummer = input("Postnummer: ")
    poststed= input("Poststed: ")
    
    #return navn, adresse, postnummer, poststed 
    print(f"Til: {navn} \n{adresse} \n{postnummer} {poststed}")

gateadresse(1) #hvorfor fungerer det å skrive et vilkårlig tall i parantesen 