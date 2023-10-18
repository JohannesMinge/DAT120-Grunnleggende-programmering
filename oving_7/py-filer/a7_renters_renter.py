#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 12:05:20 2023

@author: johannes

Definer en funksjon som beregner verdien på et innskudd i en bank etter et oppgitt antall år.
Funksjonen skal ta inn startverdi på innskuddet, renter, og antall år. Rente skal være oppgitt i
prosent. Funksjonen skal først regne om renta til et økningstall med formelen okningstall =
1.0 + rente/100. (rente deles på 100 siden det er prosent). Deretter skal funksjonen regne ut
verdi som startverdi*okningstall**(antall år)
.

"""

# Innskudd i en bank i x antall år


def renters_rente(verdi_start, years, rente):
    okningstall = 1.0 + rente/100
    verdi_final = verdi_start* (okningstall**years)
    return(verdi_final)


years = 10
verdi_start = 300000
rente = 7
print(f"{renters_rente(verdi_start, years, rente)}, etter {years} år")