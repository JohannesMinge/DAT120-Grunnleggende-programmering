#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 08:50:30 2023

@author: johannes
"""

"""
strategi:
    lag funksjon 
    opprett dictionary
    gå gjennom lista og legg til nøkler og verdier i dict eller oppdater verdier på eksisterende år
    returner dict
    
Format: [«1984: 3», «1987: 6», «1979: 2», «1984: 2», …]
"""


def aarstall_dict(liste)
    dict = dict()
    
    for i in range(len(liste)) #går gjennom lista og legger til nøkler og verdier i dict
        liste.strip(«, »)
        komponenter = liste.split(": ")
        nokkel = komponenter[0]
        verdi = komponenter[1]
        
        if liste[i] in dict: #ser om årstallet allerede finnes. Hvis det gjør det, oppdateres tallet
            gammel_verdi = dict[liste[i]]
            ny_verdi = gammel_verdi + verdi #oppdaterer verdien her ved å legge sammen gammel og ny verdi
            dict[liste[i]] = ny_verdi #oppdaterer verdien i dictionariet
        else: #finnes ikke årstallet i dictionariet, oprrettes det med tilhørende verdi. 
            dict[nokkel] = verdi
    
    return dict #returnerer dictionariet 



# Skriver ut dictionariet sortert etter år:

dictionary = aarstall_dict(liste) #bruker funksjonen til å lage et dictionary i denne deloppgaven som skal brukes i scriptet videre. 
nokkel_liste = list(dictionary.keys()) #lager en liste av dictionariet som blir gitt av forrige funksjon.

sortert_nokkel_liste = nokkel_liste.sort()
for k in range(len(sortert_nokkel_liste))
    aarstall = sortert_nokkel_liste[k] #finner årstall
    verdi = dictionary[sortert_nokkel_liste[k]] #finner verdi
    print(f"{aarstall}: {verdi}") #skriver ut årstallet og verdien, formatert slik det kom inn








# Rettet av ChatGPT:
def aarstall_dict(liste):
    dictionary = dict()

    for entry in liste:
        entry = entry.strip("«,»")  # Remove unwanted characters
        komponenter = entry.split(": ")
        nokkel = komponenter[0]
        verdi = int(komponenter[1])  # Convert verdi to integer

        if nokkel in dictionary:
            gammel_verdi = dictionary[nokkel]
            ny_verdi = gammel_verdi + verdi
            dictionary[nokkel] = ny_verdi
        else:
            dictionary[nokkel] = verdi

    return dictionary


# Example usage:
input_liste = ["«1984: 3»", "«1987: 6»", "«1979: 2»", "«1984: 2»"]
dictionary = aarstall_dict(input_liste)

# Sort keys and print results
sortert_nokkel_liste = sorted(dictionary.keys())
for aarstall in sortert_nokkel_liste:
    verdi = dictionary[aarstall]
    print(f"{aarstall}: {verdi}")







