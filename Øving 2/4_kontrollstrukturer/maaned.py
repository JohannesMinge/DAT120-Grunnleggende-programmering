# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 14:29:50 2021

@author: Erlend Tøssebro
"""

tall_streng = input("Skriv inn et tall for en måned: ")
maaned = int(tall_streng)
if maaned < 1 or maaned > 12:
    print("ugyldig måned")
else:
    print("Gyldig måned")

