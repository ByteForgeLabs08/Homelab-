#!/usr/bin/env python3

# Füllstand abfragen und umwandeln.
eingabe = input("Festplatten-Füllstand in Prozent:")
fuellstand = float(eingabe)

#Bewerten
if fuellstand > 90:
    print(f"KRITISCH: Festplatte zu {fuellstand} % voll!")
elif fuellstand >= 80:
    print(f"Warnung: Festplatte zu {fuellstand} % voll.")
else:
    print(f"OK: Festplatte zu {fuellstand} % voll.")
