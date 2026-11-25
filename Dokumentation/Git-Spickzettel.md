# Git-Spickzettel

Git-Workflow

1. Status prüfen
git status

2. Änderungen vormerken
git add

3. Commit erstellen
git commit -m "Beschreibung"

4. Nach GitHub hochladen
git push origin main

Merksatz:
git status -> git add -> git commit -> git push
Formulierung der Commit-Nachrichten.

Das Muster sieht in etwa so aus:

Verb + was + wo

Das Verb steht immer am Anfang, in der Grundform und groß geschrieben.

Die wichtigsten Verben:

Verb		Bedeutung		Beispiel
---------------------------------------------------------------
Add		hinzufügen(neu)		Add disk_check.py
Update		erweitern/aktualisieren Update Notes for Lession 3
Fix		Fehler beheben		Fix syntax error in variablen_type.py
Change/Use	umstellen		Use float in disk_check.py
Rename		umbenennen		Rename variablen.py to variablen_type.py
Remove		entfernen		Remove Testfile
Merge		zusammenführen		Merge commit message notes into Git-Spickzettel.md
Move		verschieben		Move Git-Spickzettel.md to Dokumentation


Vokabelhilfe:
-----------------------------------------------------------------
Deutsch:		Englisch:
Skript			script
Notizen			notes
Fehler			bug / error
Warnung			warning
Lektion			lesson
ausführbar machen	make executable
in / für		in / for
Tippfehler		typo
zusammenführen		merge
verschieben		move
Beispiel		example
Netzplan		network plan


##Änderungen ansehen 

Befehl			Bedeutung
---------------------------------------------------------------------
git diff datei		Zeigt, was sich geändert hat(rot '-'=entfernt; grün'+'=neu)
git log --oneline	Alle Commits als kurze Liste
git ls-files		Alle Dateien, die Git kennt mit Pfad


**Im 'git log'**

- 'Head -> main' = hier stehe ich gerade
- 'origin /main' = Stand auf GitHub
- Stehen beide auf dem selben Commit, sind lokal und GitHub synchron.

**Im 'git status'**
- 'ahead of 'origin/main' by 2 commits' = 2 Commits warten noch auf den Push


------------------------------------------------------------------------

##Zustände einer Datei

neue Datei: untracked -> add -> staged -> commit -> push
geänderte Datei: modified -> add -> staged -> commit -> push


Git speichert **nichts automatisch**. Jede Änderung braucht add + commit.
Git merkt sich auch Rechte: chmod +x macht eine Datei modified. (100644 -> 100755)

------------------------------------------------------------------------

##Commits sammeln

Mehrer commits nacheinander machen , am Ende **einmal** git push origin main.
Regel: **ein Commit pro Änderung**, damit die Historie lesbar bleibt.


-------------------------------------------------------------------------

##Datei verschieben, umbenennen,entfernen

Befehl				Bedeutung
-------------------------------------------------------------------------
git mv alt neu			Umbenennen/verschieben, Historie bleibt verbunden
git mv -f quelle ziel 		Verschieben und Ziel **überschreiben**(nur wenn sicher!)
git rm datei 			Aus Git **und** von der Festplatte löschen
git rm --caches datei		**Nur aus Git** entfernen, Datei bleibt auf der Festplatte


**Vor dem Verschieben prüfen**, ob es das Ziel gibt(ls), sonst ggf. mit dif vergleichen.

---------------------------------------------------------------------------------------

##Dateien vergleichen und zusammenführen (Linux)

Befehl 				Bedeutung
---------------------------------------------------------------------------------------
diff datei1 datei2		< nur in datei 1, > nur un Datei 2
cat a << b			Inhalt von a **an b anhängen**
cat a > b			b **überschreiben** alter Inhalt weg!


Fehler passiert? git restore datei holt die letzte committete Version zurück.

----------------------------------------------------------------------------------------


##Geheimnisse schützen

Datei 			Inhalt 					in Git?
----------------------------------------------------------------------------------------
env			echte Werte + Passwörter		nie
env.example		nur Platzhalter(leeres Formular)	ja
gitignore		Liste der Dateien, die Git ignoriert	ja

- gitignore **anlegen, bevor ** die .env entsteht.
- Was einmal gepusht wurde, bleibt in der Historie. Echtes Passwort auf GitHub gelandet?
 **Passwort ändern** , nicht nur löschen.
- Keine Passwörter in Doku-Dateien (z.b Netzplan)

-----------------------------------------------------------------------------------------

##Wichtige Regeln

- Bereits **gepushte** Commits nicht nicht nachträglich ändern (kleine Tippfehler bleiben einfach stehen)
- Dateinamen **exakt** schreiben , Groß-/Kleinschreibung zählt (Dokumentation ist nicht gleich dokumentation)
- **Tab-Taste** vervollständigt Namen und zeigt sofort, ob es einen Pfasd gibt.
- Leerzeichen zählen: /rearm ist nicht gleich / rearm, cd~ ist nicht gleich cd ~
