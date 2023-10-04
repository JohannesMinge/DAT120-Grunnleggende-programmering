#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 13:09:02 2023

@author: johannes


Filhåndtering: Skriv et program som leser inn ei fil som inneholder en serie med flyttall. Anta
at flyttallene er avstander i kilometer. For hvert tall skal du bruke funksjonen fra øving 3
oppgave b til å konvertere avstanden til nautiske mil. Deretter skal programmet skrive ut
avstanden i nautiske mil til ei ny fil. Brukeren av programmet skal oppgi navn på den første
fila og navn på den andre fila. Bruk den vedlagte fila «oving_6_testfil.txt» for å teste koden
din.

"""

def km_til_naut(avstand_km):
    avstand_naut = round(avstand_km / 1.852, 2)
    return avstand_naut


if __name__ == "__main__":
    avstand_km = float(input("Skriv inn avstanden i km: "))
    print(f"= {km_til_naut(avstand_km)} nautiske mil")
    
    

