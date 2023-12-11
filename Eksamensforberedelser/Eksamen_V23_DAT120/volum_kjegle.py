#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 15:21:29 2023

@author: johannes
"""

def kjegle(radius, hoyde):
    volum = (3.14*radius*radius*hoyde)/3
    return volum

liten_kjegle = kjegle(2, 10)
print(f"Volumet er: {liten_kjegle}")