#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 15:00:04 2023

@author: johannes
"""

bokstaver = 2*int(input("Hvor mange bokstaver i alfabetet du bruker? 26 for engelsk og 29 for norsk. Skriv antallet: "))
tall = input("Skal du ha med tall? Skriv 'ja' eller 'nei': ")
if tall == "ja":
	tall = 10
else: tall = 0
spesialtegn = int(input("Hvor mange spesialtegn er tillatt? "))
A = int(input("Hvor mange tegn skal passordet bestå av? "))

M = bokstaver + tall + spesialtegn
kombinasjoner = M**A

print(f"Det finnes {kombinasjoner} ulike kombinasjoner med dette passordet.")