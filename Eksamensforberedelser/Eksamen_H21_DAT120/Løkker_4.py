#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 11:08:58 2023

@author: johannes
"""

tall = None
liste = []

while tall != 0:
	tall = int(input("Skriv inn et positivt tall. Skriv «0» for å avslutte.  "))
	if tall != 0:
            liste.append(tall)

max_liste = max(liste)
min_liste = min(liste)
gjennomsnitt_liste = sum(liste) / len(liste)

print(f"Maks: {max_liste}, min: {min_liste}, gjennomsnitt: {gjennomsnitt_liste}")