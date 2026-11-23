#Troubleshooting: HV01 fährt stündlich herunter.

Datum: 19.11.2026-23.11.2026
**System:** HV01 (Hyper-V Host, Windows Server 2019)

##Problem
-Bei der täglichen Arbeit/ Übung auf dem Host in Hyper-V im Labor, ist der Server einfach heruntergefahren.
-Überprüfung der Systeme nach dem Start, hat keinen Hinweis auf das Problem ergeben.
-Strom und Energieeinstellungen haben alles auf volle Leistung und es gibt keine Einstellung,
 die bei der inaktivität dieses Verhalten erklären würde.
-Ein Test im Betrieb,aber ohne aktives Arbeiten auf dem Host hat ebenso keinen Einfluss auf das Problem gehabt.
-Das Herunterfahren wurde vom SYSTEM veranlasst.
-Es war aber kein kaltes abschalten, der Host wurde ordnungsgemäß heruntergefahren.

-Durch das herunterfahren von dem Host(HV01) sind auch die dementsprechenden VMs im Labor, mit heruntergefahren.

##Analyse

-In der Ereignissanzeige gab es keinen Hinweis, warum das System herunterfährt. Ersichtlich war nur dass es von dem SYSTEM 
veranlasst wurde.
-Ebenso war erst das neue Update gemacht worden.
-Und seit paar Tagen lief das Veeam Appliance testweise und sollte als Backup Alternative getestet werden.
-Das Veeam hatte nach dem Neustart dann die Meldung, dass es ein Fehler gab und nicht ordnungsgemäß heruntergefahren wurde.
	* Um das Veeam als den Verursacher von dem Problem auszuschließen, habe ich das Veeam Appliance ausgelagert.
-Ich habe noch einen Test gestartet, um die Zeit zu messen und es waren auch beim dritten Mal exakt ne Stunde, zwischen dem 
Start und herunterfahren vom System. Somit konnte ich das Veeam als Opfer und nicht Verursacher des Problems ausschließen.

##Ursache

-Ich bin dann darauf gekommen den Befehl slmgr /dlv zu testen. Da das System nur "testweise" in dem Labor läuft, wurde 
von mir eine Windows Server Testlizenz für 180 Tage installiert. Und dann konnte ich sehen, dass die Lizenz ausgelaufen war.
Dies legte den Verdacht nahe, dass es einen Zusammenhang zwischen dem Herunterfahren und dem Ablauf der Lizenz gab.

##Lösungsversuch

`slmgr /dlv' - Festellung der abgelaufenen Lizenz.
`slmgr /rearm' - Versuch der reaktivierung der Lizenz. (6 mal theoretisch möglich)
-Es gab einen Fehler 0x80041008.
`slmgr /rearm-sku <ID>' - hat ebenfalls mit der Fehlermeldung geendet.

-Mir war also klar, dass ich die Lizenz ohne weiteres nicht verlängern kann und es gab noch zwei Alternativen.
1. Der Versuch eines Generic Keys und
2. Servermigration und das erneutes Aufsetzen von Windows Server.

Da es sich um ein reines Testlabor für meine persönlichen Übungen und Tests geht, war das jetzt kein Problem einen 
Generic Key zu verwenden. Denn das System ist trotzdem funktionsfähig, ohne dass Windows offiziell aktiviert ist.

##Lösung

Erstmal wurde es auf den Generic Key gesetzt, da es am wenigsten aufwändig war.
In der cmd als Administrator habe ich :
'DISM /online /Get-CurrentEdition` 
'DISM /online /Get-TargetEditions'
eingetippt.
Ziel war es herauszufinden, ob es überhaupt ein ServerStandardEval und ServerStandard in der Liste stehen, sonst wäre die 
Umwandlung nicht möglich gewesen.
Nachdem beides zutraf, habe ich folgenden Befehl getippt:
'DISM /online /Set-Edition:ServerStandard /Productkey:<NR.> /AcceptEula`

Nach dem Neustart habe ich dann slmgr /dlv getestet. Die Erwartung von TIMEBASED_EVAL wurde gegen VOLUME_KMSCLIENT ersetzt.
Danach wurde abgewartet, bis die Zeit abgelaufen ist und ob wieder das Herunterfahren ausgelöst wird. Das System lief aber 
einwandfrei und es wurde nichts mehr unterbrochen.

##Erkenntnisse

###1. Regelmäßige Ausfälle deuten auf Software hin.
Der Server fiel in einem festen Abstand von ca.65 Minute aus. Ein solches zeitliches Mustrer spricht eigentlich gegen ein 
Hardware defekt hin, denn der würde unkontrolliert stattfinden.
Es spricht eher für eine zeitgesteuerte Ursache, wie Lizenzprüfung, geplante Aufgaben oder Updates.

> Regelmäßiger Ausfall - Zeitplan - Software
> Unregelmäßiger Ausfall - Hardware, Strom, Temperatur.

###2. Nicht jeder Logeintrag ist die Ursache.

Veeam tauchte mehrfach mit Fehlern in der EreignisAnzeige auf und wurde zunächst als Ursache vermutet. Die Abstürze traten
jedoch auch auf, nachdem Veeam deaktiviert und deinstalliert war. Veeam war nicht der Auslöser, sondern hat lediglich Fehler
gemeldet, weil seine Dienste beim Herunterfahren hart beendet wurden.

> Ein Dienst, was beim Absturz Fehler meldet, ist oft das Opfer und nicht der Täter.

###3.Nur eine Änderung zur gleichen Zeit.

Währen der Fehlersuche habe ich mehrere Sachen gleichzeitig verändert( Veeam deaktiviert und die Energiespareinstellungen 
angepasst). Dadurch wäre bei einer Verbesserung nicht deutlich gewesen, was das Problem behoben hat. 
Es war ein lehrreicher Moment, sowas nicht nochmal zu tun. 
> Erst eine Änderung - beobachten - nächste Änderung

###5. Rechtzeitig eskalieren.

> Wissen, wann man aufhört zu probieren, ist auch eine Admin-Fähigkeit.

###6. Lizenlaufzeiten aktiv  überwachen. 

Evaluierungsversionen laufen nach 180 Tagen ab. Ohne Überwachung fällt das erst auf, wenn der Server bereits ausfällt.
Die Ablaufdaten gehören dokumentiert und in den Kalender eingetragen.
