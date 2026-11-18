#!/usr/bin/env python3

#Benutzer nach dem Füllstand fragen
eingabe = input("Festplatten-Füllstand in Prozent:")
print("Typ der Eingabe:", type(eingabe))

#In Zahl umwandeln:
fuellstand = float(eingabe)
print("Typ nach der Umwandlung:", type(fuellstand))

#Vergleich:
ueber_grenze = fuellstand > 80
print(f"Füllstand: {fuellstand} % | Über 80%: {ueber_grenze}")
