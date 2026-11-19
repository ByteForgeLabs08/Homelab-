#!/usr/bin/env python3
load_average = float(input("Load Average:"))

if load_average >= 2.0:
    print("Kritisch")
elif load_average >= 1.0:
    print("Warnung")
else:
    print("OK")
