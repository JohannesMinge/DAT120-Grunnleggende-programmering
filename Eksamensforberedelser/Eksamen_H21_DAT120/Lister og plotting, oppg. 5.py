#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 13:46:06 2023

@author: johannes
"""

import matplotlib.pyplot as plt

def funksjonen(tall):
	return tall**2 - tall*500

liste_x = []
liste_y = []

for i in range(-1000, 1001):
	liste_y.append(funksjonen(i))
	liste_x.append(i)
	

plt.plot(liste_x, liste_y, "o-")
plt.grid(True)
plt.show()