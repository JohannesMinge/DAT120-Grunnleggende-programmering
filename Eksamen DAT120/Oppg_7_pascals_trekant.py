#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 13:17:50 2023

@author: johannes
"""

# Strategi:
# lag liste for hver rad
# lag Pascals trekant med hver liste 
# legg inn en en kommentar i koden om at apostrof ikke brukes i genitiv på norsk, kun på engelsk, slik at man skriver "Pascals", ikke "Pascal's". :)


antall_linjer = int(input("Skriv inn antall linjer i Pascals trekant: "))

"""
# Listelager:
# Målet med denne koden er å lage like mange lister som antall linjer, som skal ha formatet "liste_0", liste_1", "liste_2", "liste_3", etc. 
for j in range(antall_linjer):
    liste_[j] = list()


# Pyramidebygger:
# Målet her er å lage Pascals trekant med listene fra listelageren overfor. Jeg antar at listelageren fungerer som tilsiktet. 
for i in range(antall_linjer):
    #Lager to variabler som refererer til linja som bygges + forrige linje
    liste = str("liste_"+[i]) #litt usikker på om syntaxen "str("liste_"+[i]) kommer til å fungere, men antar videre at dette fungerer.
    forrige_liste = liste_[i-1]
    
    if i != 0: #unngår to ting: 1) å legge til to "1" i første linje. 2) Feil som oppstår i første linje da forrige linje ikke finnes. 
        liste.append(1) #sørger for at alle starter med 1
        for k in range(1:([i-1])): #tar deretter neste tall frem til nest siste, siden siste tall vil gi en error da det ikke finnes i forrige liste
            liste.append(forrige_liste[k] + (forrige_liste[k-1]))
    liste.append(1) #legger til "1" som siste tall i alle listene. (= første tall på første linje)

    print(liste)
"""


#Korrigert av ChatGPT
antall_linjer = int(input("Skriv inn antall linjer i Pascals trekant: "))

# Listelager:
listelager = []  # Changed the variable name from liste_ to listelager, and initialized it as an empty list
for j in range(antall_linjer):
    listelager.append(list())

# Pyramidebygger:
for i in range(antall_linjer):
    liste = listelager[i]  # Corrected the syntax to access listelager
    forrige_liste = listelager[i - 1] if i != 0 else []  # Handled the case when i is 0

    liste.append(1)  # Ensure all lines start with 1
    for k in range(1, i):  # Changed the range parameters
        liste.append(forrige_liste[k] + forrige_liste[k - 1])
    if i != 0:  # Ensure the first line doesn't append 1 twice
        liste.append(1)

    print(liste)
