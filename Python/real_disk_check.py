#!/usr/bin/env python3
import shutil

#Mountpoints, die geprüft werden sollen
mountpoints =["/"]

print("=" * 40)
print("Festplatten-Check (echte Werte)")
print("=" * 40)

for mp in mountpoints:
    gesamt, belegt, frei = shutil.disk_usage(mp)
    prozent = round(belegt / gesamt *100, 1)
    frei_gb = round(frei / 1024**3, 1)

    if prozent >90:
        status = "KRITISCH"
    elif prozent >= 80:
        status = "WARNUNG"
    else:
        status = "OK"

    print(f"{status}: {mp} zu {prozent} % belegt ({frei_gb} GB frei)")

print("=" * 40)
