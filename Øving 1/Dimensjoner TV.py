import math

ratio = 16/9
diameter = float(input("Skriv inn diameteren til skjermen i tommer: "))



# Funksjoner
v = math.atan(ratio**(-1))  #tar arktangens av mot/hos ved å flippe ratioen. 
h = diameter * math.sin(v)
b = h * ratio


# Print i tommer og cm
print("Høyde:",round(h), "tommer / ", round(h*2.54), "cm")
print("Bredde:", round(b), "tommer / ", round(b*2.54), "cm")
