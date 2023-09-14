#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 15:18:41 2023

@author: johannes
"""

a0 = int(input("Skriv inn hvilket tall vi skal starte på: "))
n = int(input("Skriv inn antall tall: "))-1
d = float(input("Skriv inn differansen mellom tallene: "))


#### MIN IDE ####
antall_entries = 0

print("")
while antall_entries <= n:
    print(a0)
    a0 += d
    antall_entries += 1




#### ALTERNATIV 2, ENDRES LØSNING ####

#for i in range(n):
    #verdi = a0 + i*d
    #print(verdi)

