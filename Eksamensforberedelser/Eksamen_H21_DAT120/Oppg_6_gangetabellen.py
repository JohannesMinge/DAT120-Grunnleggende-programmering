#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 13:50:31 2023

@author: johannes
"""

# Skriv ut en gangetabell
# Start på 1, gå opp til brukerbestemt størrelse

tabellstr = int(input("Skriv inn størrelsen på tabellen: "))

#Tabellstørrelse: n
print(f"Tabellstørrelse: {tabellstr}")

#Heading
for j in range(1, tabellstr+1):
	print(f"  {j}", end="")
print("")

#Streken
for i in range(4*tabellstr):
	print("-", end="")
print()

#Regner ut for hvert tall
for y in range(1, tabellstr+1):
	print(f"{y}:  ", end="")
	for x in range(1, tabellstr+1):
		n = x*y
		x +=1
		print(f"{n}  ", end="")
	print("")
	
    
    
