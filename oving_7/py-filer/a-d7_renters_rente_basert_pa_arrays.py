#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 12:48:46 2023

@author: johannes

Kjør funksjonen i oppgave a) med rente 3 prosent og startverdi 300.000. For parameteren
«antall år» skal du kjøre funksjonen for hver verdi i lista fra oppgave b). Du skal lagre
resultatene i ei ny liste eller numpy array. Dette kan gjøres med en for-loop eller med å bruke
numpy arrays i stedet for lister.
"""

import numpy as np
import matplotlib.pyplot as plt

# OPPGAVE A
def renters_rente(verdi_start, years, rente):
    okningstall = 1.0 + rente/100
    verdi_final = verdi_start* (okningstall**years)
    return(verdi_final)




# OPPGAVE B: 
liste_heltall = []
for i in range(0, 21):
    liste_heltall.append(i)

array_heltall = np.array(liste_heltall)
#print(array_heltall)




# OPPGAVE C:
years = 10
verdi_start = 300000
rente = 3


renter_pr_aar = []
for j in liste_heltall:
    resultat = renters_rente(verdi_start, j, rente)
    renter_pr_aar.append(round(resultat))

print(renter_pr_aar)



# OPPGAVE D:
x_koordinater = liste_heltall
y_koordinater = renter_pr_aar

plt.title(f"Avkastning på {verdi_start} med {rente}% årlig avkastning.")
plt.xlabel("Antall år")
plt.xticks(liste_heltall)
plt.ylabel("Verdi på formuen") 

plt.plot(x_koordinater, y_koordinater, "o-", label="3% rente pr. år")
plt.grid(True)
plt.show()











