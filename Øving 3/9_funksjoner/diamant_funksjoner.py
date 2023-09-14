# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 10:00:34 2021

@author: Erlend Tøssebro
"""


def skriv_ei_linje_skraa_venstre(storrelse, x, y):
    if y == storrelse-x-1:
        print("*", end="")
    else:
        print(" ", end="")


def skriv_ei_linje_skraa_hoyre(x, y):
    if y == x+1:
        print("*", end="")
    else:
        print(" ", end="")


def skriv_linje(storrelse, y):
    for x in range(storrelse):
        skriv_ei_linje_skraa_venstre(storrelse, x, y)
    for x in range(storrelse-1):
        skriv_ei_linje_skraa_hoyre(x, y)
    print()
    

storrelse = int(input("Hvor stor skal diamanten være? "))

for y in range(storrelse):
    skriv_linje(storrelse, y)
for y in range(storrelse-2, -1, -1):
    skriv_linje(storrelse, y)
