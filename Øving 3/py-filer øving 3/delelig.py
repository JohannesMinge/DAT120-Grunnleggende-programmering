def delelig(teller, nevner):
    if teller % nevner == 0:    # Bruker modulus-operatoren for å sjekke om teller er delelig på nevner
        return True
    else:
        return False

