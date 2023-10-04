#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 13:40:59 2023

@author: johannes

a) Metode: Utvid funksjonen fra øving 3 oppgave a slik at den sjekker om postnummer faktisk
er et heltall. Bruk metoden <streng>.isdecimal() for å sjekke om en streng inneholder et lovlig
heltall.
- 


a. Frivillig: Sjekk at postnummer er eksakt 4 siffer langt ved å sjekke lengden på
strengen. Bruk len() funsjonen til å sjekke lengden til en streng.

"""


def gateadresse(navn, adresse, postnummer, poststed):
    print(f"\nTil: {navn} \n{adresse} \n{postnummer} {poststed}\n")


# Setter variabler til funksjonen. Kan erstattes med input() hvis det skal bestemmes av bruker. 
navn = "Johannes"
adresse = "Solborgveien"
postnummer = str(input("Skriv inn postnummer: "))
poststed = "Stavanger"

# Kjører fuksjonen
gateadresse(navn, adresse, postnummer, poststed)



# Sjekker om postnummeret er heltall og består av fire tall.
if postnummer.isdecimal() and len(postnummer) == 4:
    print("Postnummeret ser bra ut!")
else:
    print("Her har du skrevet noe feil - postnummer skal bestå av fire tall, og kun tall.")
