



rekkevidde_km_str = input("Rekkevidden til din elbil i kilometer: ")
tur_lengde_km_str = input("Lengden til kjøreturen din i kilometer: ")

tur_lengde_km = int(tur_lengde_km_str)
rekkevidde_km = int(rekkevidde_km_str)
rekkevidde_km_2 = rekkevidde_km * 0.6


if tur_lengde_km/rekkevidde_km <= 0.8:
    print("Dette går fint! Du trenger ikke stoppe for å lade.")
elif tur_lengde_km/rekkevidde_km <=1 > 0.8:
    print("Dette kan gå på hengende håret, men du burde planlegge for én ladning.")
else: 
    #antall_ladinger = int((tur_lengde_km - rekkevidde_km*0.8 + rekkevidde_km_2) // (rekkevidde_km_2))   #trekker de 20% man bare bruker én gang fra likningen, slik at man kan regne ut hvor mange ganger man må lade opp 60% av bilens maksimale rekkevidde (altså 20%-80%)
    antall_ladinger = int((tur_lengde_km - rekkevidde_km*0.2) // (rekkevidde_km_2)) #trekker fra de 20% man må bruke opp før man begynner i 20%-80%-loopen
    print(f"Du trenger {antall_ladinger} ladinger")



