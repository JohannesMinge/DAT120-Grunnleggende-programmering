import math

# Variabler 
#d = "diameter"
#b = "bredde"
#h = "hight"
#v = "vinkel"
#ratio = "ratio"

# Brukerbestemte parametere
ratio = 16/9
diameter = 50


# Funksjoner
v = math.atan(ratio**(-1))  #tar arktangens av mot/hos ved å flippe ratioen. 
h = diameter * math.sin(v)
b = h * ratio


# Print i tommer og cm
print("Høyde:",round(h), "tommer / ", round(h*2.54), "cm")
print("Bredde:", round(b), "tommer / ", round(b*2.54), "cm")
