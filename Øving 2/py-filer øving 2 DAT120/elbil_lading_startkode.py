



rekkevidde_km_str = input("Rekkevidden til din elbil i kilometer: ")
tur_lengde_km_str = input("Lengden til kj�returen din i kilometer: ")
rekkevidde_km = int(rekkevidde_km_str)
tur_lengde_km = int(tur_lengde_km_str)


if tur_lengde_km/rekkevidde_km <= 0.8:
    print("Dette g�r fint! Du trenger ikke stoppe for � lade.")
elif tur_lengde_km/rekkevidde_km <=1 > 0.8:
    print("Dette kan g� p� hengende h�ret, men du burde planlegge for �n ladning.")
else:
    antall_ladinger = tur_lengde_km // rekkevidde_km
    print(f"Du trenger {antall_ladinger} ladinger")

