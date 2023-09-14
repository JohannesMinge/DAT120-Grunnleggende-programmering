#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 13:59:52 2023

@author: johannes
"""


def km_til_naut():
    avstand_km = float(input("Skriv inn avstanden i km: "))
    avstand_naut = avstand_km / 1.852
    return avstand_naut


if __name__ == "__main__":
    print(round(km_til_naut(), 2))



#original løsning ###############################
#avstand_km = input("Skriv inn avstanden i km: ")
#avstand_km = float(avstand_km)
#avstand_naut = avstand_km / 1.852
#print("Avstanden er", avstand_naut, "nautiske mil.")