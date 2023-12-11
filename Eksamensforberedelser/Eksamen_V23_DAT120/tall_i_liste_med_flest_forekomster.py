#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 17:47:07 2023

@author: johannes
"""


from random import randint

random_liste = []

for i in range(200):
    tall = randint(0, 10)
    random_liste.append(tall)
    

liste1 = [1, 5, 7, 7, 3, 7, 8, 3, 3, 5, 6, 2]

Tallteller = dict()

for i in range(0, len(liste1)):
    if liste1[i] in Tallteller:
        teller = Tallteller[liste1[i]]
        teller += 1
        Tallteller[liste1[i]] = teller
    else: 
        Tallteller[liste1[i]] = 1

hoyeste_verdi = 0
verdi = 0
indeks_i_lista = 0

for i in Tallteller:
    verdi = Tallteller[liste1[i]]
    if verdi > hoyeste_verdi:
        hoyeste_verdi = verdi
        indeks_i_lista = i 
    else: continue
print(f"Tallet {liste1[indeks_i_lista]} forekommer flest ganger i lista, med {hoyeste_verdi} antall ganger.")



# for i in range(0, len(random_liste)):
#     if random_liste[i] in Tallteller:
#         teller = Tallteller[random_liste[i]]
#         teller += 1
#         Tallteller[random_liste[i]] = teller
#     else: 
#         Tallteller[random_liste[i]] = 1


# hoyeste_verdi = 0
# verdi = 0
# indeks_i_lista = 0

# for i in Tallteller:
#     verdi = Tallteller[random_liste[i]]
#     if verdi > hoyeste_verdi:
#         hoyeste_verdi = verdi
#         indeks_i_lista = i 
#     else: continue
# print(f"Tallet {liste1[indeks_i_lista]} forekommer flest ganger i lista, med {hoyeste_verdi} antall ganger.")










