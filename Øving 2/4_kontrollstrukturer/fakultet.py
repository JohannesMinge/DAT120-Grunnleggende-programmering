# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 08:48:11 2021

@author: Erlend Tøssebro
"""

tall = int(input("Skriv inn tallet du ønsker fakultet av: "))
while tall < 0:
    print("Fakultet for negative tal finnes ikke!")
    tall = int(input("Skriv inn tallet du ønsker fakultet av: "))

resultat = 1
for i in range(1, tall+1):
    print(i)
    resultat *= i
print("Etter for-løkka er ferdig")
print(resultat)
