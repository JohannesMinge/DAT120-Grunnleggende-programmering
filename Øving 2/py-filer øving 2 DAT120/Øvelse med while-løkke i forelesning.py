#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 14:41:24 2023

@author: johannes
"""

"""
Serie med tall, regne ut summen
Avslutte når ∑ >1000
Skriv ut 

"""

print("Scriptet leser inn en serie tall og avslutter når summen av tallene overstiger 1000.")

summen = 0 #passer på at den restartes når scriptet restarter
antall_enties = 0
hoyeste = -1000000 #definerer et ekstremt lavt tall, slik at brukeren alltid vil sette input høyere enn det
laveste = 1000000 #motsatt av overnevnte


while summen <= 1000:
    n = float(input("Skriv inn et tall: "))
    summen += n #betyr summen = summ + tall
   
   
    if hoyeste < n:
        hoyeste = n
    if laveste > n:
        laveste = n
    antall_enties += 1

print("")
if summen >= 1000:
    print("Game over. Summen er over 1000.")
print("Summen er: ", summen)
print("Høyeste tall du skrev inn er: ", hoyeste)
print("Laveste tall du srev inn er: ", laveste)
print("Gjennomsnittet ble: ", summen/antall_enties)

    

