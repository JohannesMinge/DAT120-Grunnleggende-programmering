#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 13:20:40 2023

@author: johannes
"""


# Mål: skriv ut hvilke av linjene i fil_1 hvor et likt tall finnes i fil_2
# Skriv ut linjenummer der dette stemmer, og minst ett av elementene til felles
# Bruk try/except for å hoppe over tomme linjer 

# STRATEGI:
# Lag en liste med alle verdiene i fil_2
# Lag lister til hver linje i fil_1 med respektive tall


# Liste med alle verdiene i fil_2:
liste_fil_2 = list()
with open("elementer.txt", "r") as fil_2:
    fil_2.readline()
    
    for linje in fil_2:
        try:
            liste_fil_2.append(linje)
        except: continue #hopper over linjer 



# Sammenlikner med fil_1:
with open("grupper.txt", "r") as fil_1: #åpner fila i lesemodus, og gir den et variabelnavn
    fil_1.readline()
    linjeteller = 1 #teller antall linjer. Bukes senere.
    
    for linje in fil_1: #går gjennom alle linjene i fil_1
        liste_pr_linje = "linje_"+[linje] = list() #bruker samme kode som i forrige oppgave. Lager en varabel kalt "liste_pr_linje" som skal ha formatet "liste_0", liste_1", "liste_2", "liste_3", etc. 
        hvert_tall = linje.split(,)
        for h in range(len(hvert_tall) #skal dele hver linje inn i enkelttall 
            enkelttall = hvert_tall[h] #finner indexen til hvert enkelt tall i strengen
        
            if enkelttall in liste_fil_2: 
                liste_pr_linje.append[enkelttall] #legger til hvert tall som finnes i begge filer i lista for den bestemte linja i fil_1
            else: continue
        
        print(f"Tallet {enkelttall} på linje {linjeteller} finnes i begge filer!")
        linjeteller +=1 #holder tellingen på hvilken linje vi er på. 




    