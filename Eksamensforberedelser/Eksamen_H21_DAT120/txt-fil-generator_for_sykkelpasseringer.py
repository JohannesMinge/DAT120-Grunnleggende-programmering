#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 13:16:34 2023

@author: johannes
"""

"id målepunkt;navn målepunkt;dato;antall passeringer "

from random import randint
#ÅÅÅÅ-MM-DD

fila = open("sykkelpasseringer_2.txt", "w", encoding="UTF8")

dato = "2023-06-01"

"""
#Min kode som ikke fungerte
def datagenerator(id_maalepunkt, navn_malepunkt, antall_dager, passeringer_min, passeringer_max):
    for i in range(antall_dager):
        antall_passeringer = randint(passeringer_min, passeringer_max)
        fila.writelines(f"{id_maalepunkt};{navn_malepunkt};{dato};{antall_passeringer}\n")
        
        #Ny dag, nye muligheter :)
        dato_komponenter = dato.split("-")
        aar = int(dato_komponenter[0])
        mnd = int(dato_komponenter[1])
        dag = int(dato_komponenter[2])
        
        print(aar, mnd, dag)
        
        if dag <30:
            dag +=1
        else:
            if mnd <12: 
                mnd +=1
                dag = 1
            else: 
                aar +=1 
                mnd = 1 
                dag = 1
        dato = aar+"-"+mnd+"-"+dag


Mosvannet = datagenerator("Mos1", "Mosvannet", 478, 200, 760)
"""






from random import randint

fila = open("sykkelpasseringer_2.txt", "w", encoding="UTF8")

dato = "2023-01-01"

def datagenerator(id_maalepunkt, navn_malepunkt, antall_dager, passeringer_min, passeringer_max):
    global dato  # Use the global variable
    for i in range(antall_dager):
        antall_passeringer = randint(passeringer_min, passeringer_max)
        fila.writelines(f"{id_maalepunkt};{navn_malepunkt};{dato};{antall_passeringer}\n")

        # Ny dag, nye muligheter :)
        dato_komponenter = dato.split("-")
        aar = int(dato_komponenter[0])
        mnd = int(dato_komponenter[1])
        dag = int(dato_komponenter[2])

        if dag < 30:
            dag += 1
        else:
            if mnd < 12:
                mnd += 1
                dag = 1
            else:
                aar += 1
                mnd = 1
                dag = 1
        # Format the date components back into a string
        dato = f"{aar}-{mnd:02d}-{dag:02d}"



Mosvannet = datagenerator("Mos1", "Mosvannet", 350, 200, 623)
Hillevaag = datagenerator("Hille", "Hillevaag", 350, 320, 430)
Hafrsfjord = datagenerator("Sverd", "Hafrsfjord", 350, 120, 234)



# Close the file after writing data
fila.close()








"""

for i in range(30):
    antall_passeringer = randint(320, 570)
    fila.writelines(f"Mos1;Mosvannet maalepunkt;{dato};{antall_passeringer}\n")
    
    i.split("-")
    
    dato += 1    

dato = 230601
for i in range(30):
    antall_passeringer = randint(200, 400)
    fila.writelines(f"Sverd_i_fjell;Hafrsfjord maalepunkt;{dato};{antall_passeringer}\n")
    dato += 1  

dato = 230601
for i in range(30):
    antall_passeringer = randint(150, 320)
    fila.writelines(f"Hille2;Hillevaag maalepunkt;{dato};{antall_passeringer}\n")
    dato += 1  
"""

fila.close()