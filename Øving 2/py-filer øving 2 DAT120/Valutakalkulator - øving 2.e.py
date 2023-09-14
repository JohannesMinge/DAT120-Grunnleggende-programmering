#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 15:14:12 2023

@author: johannes
"""

"""
 Basis while-løkke: Lag et program som konverterer en serie med beløp fra en valuta til en annen. 
Programmet skal starte med å lese inn navnene på de to valutaene og kursen mellom dem. 
Så skal programmet gå i ei løkke hvor det leser inn en verdi i den ene valutaen, 
konvertere den til den andre valutaen og skrive dette ut. 
Løkka skal avslutte når brukeren skriver inn tallet 0.

1) input valuta 1 og 2
2) input kurs valuta 1 og 2
3) while input !== 0
   - input(antall av valuta 1)
   - konvertere til valuta 2
   - print(konvertert valuta 2)
   

"""

valuta_1 = input("Skriv inn navnet på valuten du vil konvertere fra: ")
valuta_2 = input("Skriv inn navnet på valuten du vil konvertere til: ")

valutakurs = float(input("Skriv inn valutakursen: "))
print()
antall_valuta_1 = 1
#val1_til_val2 = valuta_1 / valutakurs


while antall_valuta_1 != 0:
    antall_valuta_1 = float(input(f"Hvor mange {valuta_1} vil du konvertere til {valuta_2}? \nSkriv 0 for å avslutte. "))
    antall_valuta_2 = antall_valuta_1 * valutakurs
    print(antall_valuta_1, valuta_1, " = ", round(antall_valuta_2, 3), valuta_2, "\n")
