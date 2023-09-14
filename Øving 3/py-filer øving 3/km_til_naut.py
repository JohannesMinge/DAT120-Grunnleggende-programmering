#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 13:59:52 2023

@author: johannes
"""


def f_km_til_naut(avstand_km=0):
    avstand_naut = round(avstand_km / 1.852, 2)
    return avstand_naut


if __name__ == "__main__":
    avstand_km = float(input("Skriv inn avstanden i km: "))
    print(f"= {f_km_til_naut()} nautiske mil")



#original løsning ###############################
#avstand_km = input("Skriv inn avstanden i km: ")
#avstand_km = float(avstand_km)
#avstand_naut = avstand_km / 1.852
#print("Avstanden er", avstand_naut, "nautiske mil.")