#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 15:14:12 2023

@author: johannes


Unntakshåndtering: Legg inn håndtering av at bruker ikke skriver inn et lovlig tall i løsningen
på øving 2 oppgave e (valutakalkulatoren). Hvis brukeren skriver inn noe som ikke er et lovlig
flyttall skal brukeren få beskjed om det og få prøve på nytt.
   

"""

valuta_1 = "USD"
valuta_2 = "NOK"

valutakurs = 10.98
print()
antall_valuta_1 = 1
#val1_til_val2 = valuta_1 / valutakurs


while antall_valuta_1 != 0:
    try:
        antall_valuta_1 = float(input(f"Hvor mange {valuta_1} vil du konvertere til {valuta_2}? \nSkriv 0 for å avslutte. "))
        antall_valuta_2 = antall_valuta_1 * valutakurs
        print(antall_valuta_1, valuta_1, " = ", round(antall_valuta_2, 3), valuta_2, "\n")
    except:
        print("\nDu må skrive inn et tall. Prøv på nytt. \n")
        
   
