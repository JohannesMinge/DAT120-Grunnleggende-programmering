#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 13:53:30 2023

@author: johannes
"""
import math

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

n = b**2 - 4*a*c

if n > 0:
    print("Likningen har to reelle løsninger")
elif n == 0:
    print("Likningen har én løsning") #én løsning hvor n = 0
else:
    print("Likningen har ingen reell løsninger")