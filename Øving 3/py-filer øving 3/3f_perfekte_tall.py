#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 14:31:09 2023

@author: johannes


Bruk av ferdig funksjon. 
Et perfekt tall er et tall hvor summen av faktorene er lik tallet selv. Tell 
med 1 men ikke tell med tallet selv. 

6 er et perfekt tall fordi 6 = 1 * 2 * 3 = 1 + 2 + 3. 
10 er ikke et perfekt tall siden 10 = 1 * 2 * 5, som er ulikt 1 + 2 + 5 = 8.

Lag en funksjon som tar inn et tall som parameter, sjekker om tallet er perfekt 
og returnerer resultatet som en boolsk verdi. Man kan finne faktorene i et tall 
med en for-loop som starter på 2 og slutter på eller rett etter tallet/2. Bruk 
den utdelte funksjonen «delelig» for å sjekke om et tall er delelig på et annet tall.

Lag også kode som lar brukeren skrive inn et heltall og deretter bruker funksjonen din for å
sjekke om tallet er perfekt.


1) Funksjon som finner perfekte tall(brukers_tall)
    - Gå gjennom alle heltall til brukers_tall-1 og sjekk om de er delelige på brukers_tall
    - Returner alle tall som er delelige på brukers_tall og adder de 
    - Sjekk om summen av tallene == brukers_tall

2) Forløkke som sjekker alle tall fra funksjonen fra 1-x



"""

def delelig(teller, nevner):
    if teller % nevner == 0:    # Bruker modulus-operatoren for å sjekke om teller er delelig på nevner
        return True
    else:
        return False


def perfekt_tall(brukers_tall):
    sum_tall = 0
    
    #Finn og adder alle delbare tall
    i = 1
    while i < brukers_tall:                     #Sjekker alle tall opp til brukers_tall
        if delelig(brukers_tall, i) == True:    #Sjekker om de er delelige på brukers_tall
            sum_tall = sum_tall + i             #Summerer de delbare tallene
        i = i+1                                 #Neste tall
    return (True if sum_tall == brukers_tall else False)


"""
### Kan brukes hvis 
brukers_tall = int(input("Skriv inn tallet: "))  
test_tall = perfekt_tall(brukers_tall)
print(test_tall)
"""


for j in range(2, 10000):
    if perfekt_tall(j) == True:
        print(f"{j} er et perfekt tall.")





#### ALTERNATIV 2 ###

#if tall == 6 or 28 or 496 or 8128 or 33550336 or 8589869056:
#    return True