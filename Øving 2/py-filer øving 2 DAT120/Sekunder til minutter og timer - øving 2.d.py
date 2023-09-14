#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 13:58:54 2023

@author: johannes
"""



"""
1) input antall sekunder
2) hvis sekunder > 60, begynn på min
    else: print(sekunder)
3) hvis min > 60, begynn på t

Restsekunder = sek - min*60

"""

sekunder = int(input("Skriv inn antall sekunder: "))
minutter = sekunder // 60
timer = minutter // 60

restsekunder = sekunder - minutter*60
restminutter = minutter - timer*60

if sekunder < 60:
    print(sekunder, "sekunder")
elif sekunder > 60 and minutter < 60:
    print(minutter, "minutter og ", restsekunder, "sekunder")
else:
    print(timer, "timer", restminutter, "minutter, og", restsekunder, "sekunder")
    