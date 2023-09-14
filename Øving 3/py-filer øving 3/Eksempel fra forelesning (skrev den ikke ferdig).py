#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 14:45:52 2023

@author: johannes


Lag en funksjon som regner ut energiproduksjonen til en turbin. 
Funksjonen din skal taparameterne strøm, tetthet, turbin_effekt og diameter til 
turbinen. Formelen forenergiproduksjonen er E= 0.5*turbin_effekt*tetthet*areal*strøm^3 
(strøm opphøyd i tredje).Funksjonen skal bruke følgende defaultverflier: 
tetthet=1000 (tettheten til vann), turbin-effekt=0,3 og diameter=1. 
Bruk funksjonen fra forrige deloppgave til å regne ut arealet fraradien. 
Husk at radien er halvparten av diameteren. Parameteren strøm skal ikke ha
noendefault verdi, men må alltid oppgis. Merk at samme funksjon kan brukes 
for bådevannturbiner og vindturbiner. For en vindturbin må man bruke 
tettheten til luft, som er 1,2.

"""

def effekt_vannturbin(strom, turbin_effekt=0.3, diameter=1, tetthet=1000):
    #setter verdier fra de man bruker/ender mest (her: strøm), til det man endrer minst (her: tetthet)
    effekt = 0.5*turbin_effekt * tetthet