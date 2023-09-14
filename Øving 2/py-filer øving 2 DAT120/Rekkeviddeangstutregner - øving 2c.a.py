#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 13:54:39 2023

@author: johannes
"""




rekkevidde_km_str = input("Rekkevidden til din elbil i kilometer: ")
tur_lengde_km_str = input("Lengden til kjøreturen din i kilometer: ")
rekkevidde_km = int(rekkevidde_km_str)
tur_lengde_km = int(tur_lengde_km_str)



if tur_lengde_km/rekkevidde_km <= 0.8:
    print("Dette går fint! Du trenger ikke stoppe for å lade.")
elif tur_lengde_km/rekkevidde_km <=1 > 0.8:
    print("Dette kan gå på hengende håret, men du burde planlegge for én ladning.")
else:
    antall_ladinger = tur_lengde_km // rekkevidde_km
    print(f"Du trenger {antall_ladinger} ladinger")

