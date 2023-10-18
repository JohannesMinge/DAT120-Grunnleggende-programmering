#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 12:39:57 2023

@author: johannes

b) Lag ei liste eller numpy array med alle heltall fra og med 0 til og med 20.
"""

import numpy as np

liste_heltall = []
for i in range(0, 21):
    liste_heltall.append(i)

array_heltall = np.array(liste_heltall)
#print(array_heltall)