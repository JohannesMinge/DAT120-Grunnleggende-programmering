#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 13:29:09 2023

@author: johannes

Lag et program som teller antall forekomster av hvert ord i en tekstfil. Brukeren skal skrive inn
navnet til tekstfila og programmet skal skrive ut antall forekomster av hvert ord i tekstfila. Du kan
gjøre dette ved å lage et dictionary som bruker ord som nøkkel og antall som verdi. Første gang du
ser ordet skal du sette det inn som ny nøkkel med verdien 1, seinere skal du øke verdien til ordet
med én for hver gang du leser ordet. Test programmet ditt følgende tekstfiler, som er lagt ved
øvingen.
- oving_1_som_rein_tekst.txt
- oving_2_som_markdown.md

Den siste er i et tekstformat som heter «Markdown», men kan i denne oppgaven behandles som rein
tekst. Markdown-filer er reine tekstfiler med enkle markeringer som sier hva som skal være
overskrifter og liknende.
Frivillig: Fjern tegnsetting fra ordene og gjør o


- Lag dictionary
    - Nøkkel: ord
    - Verdi: antall forekomster




"""

ordliste = dict()
# oving_1_som_rein_tekst.txt

#with open(input("Skriv inn navnet på fila: "), "r", encoding="UTF8") as fila:
with open("oving_1_som_rein_tekst.txt", "r", encoding="UTF8") as fila:
    for linje in fila: #Deler opp alle ordene, fjerner punktum og komma og setter alt til liten bokstav
        linje = linje.replace(".", " ") #måtte sette linje = linje for å bruke replace(). Fjerner punkturm.
        linje = linje.replace(",", " ")
        linje = linje.replace("(", " ")
        linje = linje.replace(")", " ")
        
        ordene = linje.split() #deler opp alle ordene i hver linje i fila
        for ordet in ordene:
            ordet = ordet.lower()
            
            if ordet in ordliste:
                teller = ordliste[ordet] #henter telleren til ordet
                teller = teller+1 #legger på 1 på telleren
                ordliste[ordet] = teller #oppdaterer telleren til ordet
            
            else: #lager ny entry i dictionariet for nytt ord
                ordliste[ordet] = 1 #teller for nytt ord
    ordliste_sortert = dict(sorted(ordliste.items(), key=lambda item: item[1], reverse=True)) #Tok denne fra ChatGPT, men den fungerer til å sortere ordlista i synkende rekkefølge.

    for ordet in ordliste_sortert: #printer det ferdige dictionariet
            print(f"Ordet «{ordet}» forekommer {ordliste[ordet]} ganger.")
        
    
        
        