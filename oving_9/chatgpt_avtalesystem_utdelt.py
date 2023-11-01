from datetime import datetime, timedelta

# Deloppgave a
class Avtale:
    def __init__(self, tittel, sted, starttidspunkt, varighet):
        self.tittel = tittel
        self.sted = sted
        self.starttidspunkt = starttidspunkt
        self.varighet = varighet

    def __str__(self):
        return f"Avtale: {self.tittel}\nSted: {self.sted}\nStarttidspunkt: {self.starttidspunkt}\nVarighet: {self.varighet} minutter"

# Deloppgave c
def opprett_avtale():
    tittel = input("Skriv inn tittel på avtalen: ")
    sted = input("Skriv inn sted for avtalen: ")

    while True:
        starttid_str = input("Skriv inn starttidspunkt (YYYY-MM-DD HH:MM): ")
        try:
            starttidspunkt = datetime.strptime(starttid_str, "%Y-%m-%d %H:%M")
            break
        except ValueError:
            print("Ugyldig format. Prøv igjen.")

    while True:
        varighet_str = input("Skriv inn varighet i minutter: ")
        try:
            varighet = int(varighet_str)
            break
        except ValueError:
            print("Ugyldig verdi. Skriv inn et heltall.")

    avtale = Avtale(tittel, sted, starttidspunkt, varighet)
    return avtale


# Deloppgave d
def skriv_ut_avtaler(avtaler, overskrift=""):
    print(overskrift)
    for indeks, avtale in enumerate(avtaler):
        print(f"[{indeks}] - {avtale.tittel}")


# Deloppgave e
def lagre_avtaler_til_fil(avtaler, filnavn):
    with open(filnavn, 'w') as file:
        for avtale in avtaler:
            file.write(f"{avtale.tittel},{avtale.sted},{avtale.starttidspunkt},{avtale.varighet}\n")


# Deloppgave f
def les_avtaler_fra_fil(filnavn):
    avtaler = []
    with open(filnavn, 'r') as file:
        for line in file:
            avtale_data = line.strip().split(',')
            tittel = avtale_data[0]
            sted = avtale_data[1]
            starttidspunkt = datetime.strptime(avtale_data[2], "%Y-%m-%d %H:%M")
            varighet = int(avtale_data[3])
            avtale = Avtale(tittel, sted, starttidspunkt, varighet)
            avtaler.append(avtale)
    return avtaler


# Oppgave g
def avtaler_på_dato(avtaler, dato):
    avtaler_på_datoen = []
    for avtale in avtaler:
        if avtale.dato == dato:
            avtaler_på_datoen.append(avtale)
    return avtaler_på_datoen


# Deloppgave h
def søk_avtaler(avtaler, søkeord):
    søkeord = søkeord.lower()
    filtrerte_avtaler = []
    for avtale in avtaler:
        if søkeord in avtale.tittel.lower():
            filtrerte_avtaler.append(avtale)
    return filtrerte_avtaler


if __name__ == "__main__":
    # Eksempel på bruk av klassen fra deloppgave a:
    tittel = "Møte"
    sted = "Kontor"
    starttidspunkt = datetime(2023, 6, 30, 14, 0)  # Eksempel på starttidspunkt (år, måned, dag, time, minutt)
    varighet = 60  # Eksempel på varighet i minutter

    avtale = Avtale(tittel, sted, starttidspunkt, varighet)
    print(avtale)

    # Eksempel på bruk av funksjonen fra deloppgave c:
    ny_avtale = opprett_avtale()
    print(ny_avtale)

    # Eksempel på bruk av funksjonen fra deloppgave e og f:
    avtale1 = Avtale("Møte Forskningsprosjekt 1", "Kontor", datetime(2023, 6, 30, 14, 0), 60)
    avtale2 = Avtale("Trening", "Treningsstudio", datetime(2023, 7, 1, 10, 30), 90)
    avtale3 = Avtale("Lunsj", "Restaurant", datetime(2023, 7, 2, 12, 0), 45)

    avtaler_liste = [avtale1, avtale2, avtale3]

    avtaler_liste.append(Avtale("Møte Foreskningsprosjekt 2", "Kontor", datetime(2023, 6, 23, 14, 0), 60))
    avtaler_liste.append(Avtale("Seminar 'forskningsprosjekt 1", "Kontor", datetime(2023, 6, 15, 14, 0), 60))
    avtaler_liste.append(Avtale("Møte", "Kontor", datetime(2023, 3, 10, 14, 0), 60))

    skriv_ut_avtaler(avtaler_liste, overskrift="Mine avtaler:")
    lagre_avtaler_til_fil(avtaler_liste, "avtaler.txt")

    ny_liste = les_avtaler_fra_fil("avtaler.txt")
    skriv_ut_avtaler(ny_liste, overskrift="Innleste avtaler")

    # Eksempel på bruk av funksjonen fra deloppgave g:
    dato = datetime(2023, 7, 1).date()
    avtaler_på_valgt_dato = avtaler_på_dato(avtaler_liste, dato)
    for avtale in avtaler_på_valgt_dato:
        print(avtale)
