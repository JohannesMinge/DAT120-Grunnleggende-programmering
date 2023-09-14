#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 15:43:00 2023

@author: johannes
"""

"""
Enkelt spill for to spillere: hver runde kaster hver spiller en sekssidet 
terning og legger resultatet til scoren til spilleren. Deretter blir 
spilleren spurt om vedkommende ønsker å fortsette. 
Vinneren er den som har så nært 21 poeng som mulig, men ikke over. 

"""
import random #en pakke som kan gi tilfeldige tall

spiller_1 = input("Navn til spiller 1: ")
spiller_2 = input("Navn til spiller 2: ")

score_spiller_1 = 0
score_spiller_2 = 0

spiller_1_onsker_aa_kaste = True
spiller_2_onsker_aa_kaste = True

while spiller_1_onsker_aa_kaste == True or spiller_2_onsker_aa_kaste == True:
    if spiller_1_onsker_aa_kaste: 
        print("Score for", spiller_1, ":", score_spiller_1)
        onsker_aa_kaste = input("Ønsker du å kaste? (j/n)")
        if onsker_aa_kaste == "j":
            terningverdi = random.randint(1, 6)
            score_spiller_1 += terningverdi
            print(spiller_1, " kastet: ", terningverdi, " og har nå ", score_spiller_1, "\n")
        else: 
            spiller_1_onsker_aa_kaste = False
            print("\n")
    if spiller_2_onsker_aa_kaste: 
        print("Score for", spiller_2, ":", score_spiller_2)
        onsker_aa_kaste = input("Ønsker du å kaste? (j/n)")
        if onsker_aa_kaste == "j":
            terningverdi = random.randint(1, 6)
            score_spiller_2 += terningverdi
            print(spiller_2, " kastet: ", terningverdi, " og har nå ", score_spiller_2, "\n")
        else: 
            spiller_2_onsker_aa_kaste = False
            print("\n")


if score_spiller_1 > 21:
    score_spiller_1 = -1
if score_spiller_2 > 21:
    score_spiller_2 = -1


if score_spiller_1 > score_spiller_2:
    print(spiller_1, " vant!")
elif score_spiller_2 > score_spiller_1:
    print(spiller_2, " vant!")
else:
    print("Uavgjort!")    
    

