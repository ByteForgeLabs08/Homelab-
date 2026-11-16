# Linux Notizen

Prozesse

Ein Prozess ist ein laufendes Programm.

Wichtige Begriffe:

PID= Process ID
PPID= Parent Process ID
PID 1= systemd

Prozessstatus:

R= Running
S= Sleeping
Z= Zombie

ps= Zeigt Prozesse der aktuellen Benuzer an.
ps aux= Zeigt alle Prozesse an.
pgrep ssh= Sucht Prozesse nach Namen(ssh z.b)
top= Zeigt CPU-, RAM- und Prozessauslastung.
kill PID= beendet den Prozess sauber.
kill -9 PID= erzwingt das Beenden eines Prozesses.

Linux verwendet meist systemd zur Dienstverwaltung.

systemctl status ssh= Status prüfen(z.b ssh)
systemctl start ssh= Startet den Dienst(z.b ssh)
systemctl stop ssh= Stoppt den Dienst (z.b ssh)
syastemctl restart = Dienst wird neu gestartet.
systemctl --failed= Zeigt fehlerhafte Dienste an.

Troubleshooting:

Dienst | Status prüfen | Logs prüfen | Ursache finden | Lösung umsetzen

Logs

Logs liefern Informationen über Fehler und Systemereignisse.

journalctl= journal anzeigen.
journalctl -u ssh= Logs eines bestimmten Dienstes(z.b ssh)

Grundregel:

Welcher Dienst verursacht ein Problem?
Status prüfen.
Gezielt Logs dieses Dienstes auswerten.

Netzwerk

ip a= IP-Adresse anzeigen.
ip route= Routingtabelle anzeigen.
ping= erreichbarkeit testen.
ss -tulpin= Offene Ports anzeigen.

Gleiches Netz:Verbindung direkt.
Anderes Netz:Verbindung über Gateway.

Benutzer und Berechtigungen

whoami= aktueller Benutzer.
id= Benutzerinformationen.
sudo= Befehl als Administrator.
chmod= Ändert die Rechte.
chown= Besitzer ändern.
chgrp= Ändert die Gruppe.

Benutzer | Gruppe | Berechtigung

Monitoring

Aktuelles Projekt:

system_health.sh

Enthält:

-Hostname
-IP-Adresse
-Uptime
-SSH-Status
-Cron-Status
-RAM-Auslastung
-SWAP-Nutzung
-Load Average
-Failed Services
-Firewall-Status
-Gateway

Interpretation:

RAM-> MEM=Arbeitsspeicher

Swap: 0B genutzt=optimal.
Nutzung kann auf Speicherdruck hindeuten.

Load Average

Niedrig=gesund
Hoch= Ursache analysieren

Problem | Analyse | Ursache | Lösung
