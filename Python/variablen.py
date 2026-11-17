#!/usr/bin/env python3

# Systemwerte (noch von Hand eingetragen)

hostname = "ubuntu-admin-lab"
ram_gb = 4
load = 0.15
ssh_aktiv = True

# Ausgabe mit Typ

print (hostname, type(hostname))
print (ram_gb, type(ram_gb))
print (load, type (load))
print (ssh_aktiv, type (ssh_aktiv))


# Schöne Ausgabe mit f-String

print (f"Host: {hostname} | RAM: {ram_gb} GB | Load: {load} | SSH: {ssh_aktiv}")
