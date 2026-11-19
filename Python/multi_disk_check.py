#!/usr/bin/env python3

#Füllstände mehrerer Festplatten(erstmal noch von Hand)
festplatten = [45, 99, 85, 95, 72, 80]

print("=" * 40)
print("Festplatten-Check")
print("=" * 40)

for fuellstand in festplatten:
    if fuellstand > 90:
        print(f"KRITISCH: {fuellstand} %")
    elif fuellstand >= 80:
        print(f"WARNUNG:{fuellstand} %")
    else:
        print(f"OK: {fuellstand} %")
print("=" * 40)
print(f"Geprüfte Festplatten: {len(festplatten)}")
