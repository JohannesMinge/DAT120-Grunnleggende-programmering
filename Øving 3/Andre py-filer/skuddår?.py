#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 15:53:49 2023

@author: johannes
"""

# Lag en funksjon for å finne ut om et år er et skuddår. Et år et et skuddår
# hvis det er delelig på 4, men ikke på 100. Et år som er deleleig på 100 er 
# likevel et skuddår hvis det er delelig på 400. 




### MITT FORSØK ###
#def skuddar():
    
#    if year % 4 == 0:
#        print("Året er et skuddår!")
#    elif year % 100 !=0:
#        print("Nei")
#    elif year % 100 != 0 and year % 400 == 0:
#        print("Nei")
#    else:
#        print("Året er ikke et skuddår")    

#year = int(input("Skriv inn året: "))


"""
### ENDRES VERSJON ###
"""

def skuddar(arstall):
    if arstall % 400 == 0:
        return True #delelig på 400 er alltid skuddår
    if arstall % 100 == 0:
        return False #fordi vi allerede har testet 400
    if arstall % 4 == 0:
        return True
    return False # kan sette den her fordi alle andre relevante svar allerede er returnert over


#if __name__ == "__main__":
#    arstall = int(input("Årstall: "))
#    if skuddar(arstall): # == True trengs ikke skrives, fordi if-løkker bygger på boolske verdier uansett
#        print("Det er et skuddår!")
#    else:
#        print("Det er ikke et skuddår.")


if __name__ == "__main__":
    arstall = 1
    while skuddar(arstall) == False:
        arstall = int(input("Årstall: "))
        print("Det er ikke et skuddår.")
    print("Det er et skuddår!")
        
        
        
        
        