##Wo bin ich und was mache ich?

Ich wil......			Wo bin ich?	Prompt erkennbar an:		Befehl(Beispiel):

den Bauplan lesen		VM im Ordner	elena@ubuntu-admin-lab:		cat docker-compose.yml
						~/Homelab/Docker/fisi-blog01$	

sehen,ob Container laufen	auf der VM	elena@ubuntu-admin-lab		docker compose ps/
										docker ps

die Logs lesen			auf der VM 	elena@ubuntu-admin-lab		docker compose logs -n 20 db

in den Container gehen		von der VM aus 	root@<Container-ID>		docker exec -it fisi-blog01 bash

Container verlassen		im Container 	root@<Container ID>		exit

Container ab/aufbauen		auf der VM	elena@ubuntu-admin-lab		docker compose down / up -d

##Docker - Wo Bin ich?
--------------------------------------------------------------------------------------------------------------

Prompt lesen :
benutzer@rechner:ordner$
elenaadmin@ubuntu-admin-lab = auf der VM
root@<Container ID> = im Container
$ = normaler Benutzer und # = root

##Docker - Drei Namen pro Container
---------------------------------------------------------------------------------------------------------------

|	Name	|	Beispiel	|	Benutzt bei	|
---------------------------------------------------------------------------------------------------------------
| Service	| blog,db		| docker compose	|
| Name		| fisi-blog01		| docker....		|
| Image		| wordpress		| nur der Karton	|

Im Zweifel docker compose ps

##Docker - wichtige Befehle
---------------------------------------------------------------------------------------------------------------

docker compose ps			#Dienste im Projektordner
docker compose logs -n 20 db		#letzte 20 Zeilen
docker compose logs -f blog		#live zuschauen (Strg+C beenden)
docker exec -it fisi-blog01 bash	#in den Container gehen
exit					#aus dem Container gehen
docker ps -a | less -S			#breite Ausgabe lesen

##Docker - Restart
---------------------------------------------------------------------------------------------------------------

restart: unless-stopped = startet nach Neustart selbst, außer ich habe ihn bewusst gestoppt.
Getestet am 26.11.2026: alle 4 Container liefen nach Neustart HV01.

##Logs lesen
---------------------------------------------------------------------------------------------------------------

IP am Anfang = wer angeklopft hat (Besucher, nicht Container)
200 = OK, 404 = nicht gefunden, 500 = Serverfehler

[Note] Hinweis, [Warning] Warnung, [ERROR] Fehler


##Docker- Netzwerke
----------------------------------------------------------------------------------------------------------------

docker network ls			#alle Netze
docker network inspect<netz> | grep -E "Name|Subnet|Gateway|IPv4Address"
docker exec <container> getent host <name> #DNS-Test

-Jedes Compose-Projekt bekommt eigenes Netz: <ordner>_default
-Gateway .1 = die VM, Contaqiner bekommen .2, .3 ...
IPs können sich ändern -> immer den Dienstnamen nutzen(z.b db)
-Container finden sich nur im selben Netz (eigenes DNS pro Netz)
