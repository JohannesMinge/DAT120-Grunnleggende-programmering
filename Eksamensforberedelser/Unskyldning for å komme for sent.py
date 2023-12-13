#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 10:14:10 2023

@author: johannes
"""

class Avtale:
    def __init__(self, tidspunkt, person, ankomsstidspunkt, unskyldning):
        self.tidspunkt = tidspunkt
        self.person = person
        self.ankomsstidspunkt = ankomsstidspunkt
        self.unskyldning = unskyldning
    def __str__(self):
        return(f"{self.person} skulle levere {self.tidspunkt}, men kom {self.ankomsstidspunkt}. Ble heftet pga. {self.unskyldning}")
    
    
Karsten = Avtale("09:00", "Karsten", "10:20", "kul sang på radioen, men hadde med klementiner")
Johannes = Avtale("ila. ettermiddagen", "Johannes", "utpå kvelden", "gitarspilling")

print(Johannes)

        
        