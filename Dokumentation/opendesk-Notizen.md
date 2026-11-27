##Wer steht hinter OpenDesk und für wen wurde es ursprünglich gebaut?
-------------------------------------------------------------------------------------

Hinter OpenDesk steht der Zentrum für Digitale Souveränität der Öffentlichen Verwaltung GmbH

##Aus welchen Komponenten besteht OpenDesk?
----------------------------------------------------------------------------------------

Funktion			Funktionalcomponent
------------------------------------------------------------------------------------------
Chat&Collaboration		Element und Nordeck widgets
Collaborative Notes		Notizen aka Docs
Diagrameditor			Cryptpad ft. diagrams.net
Filemanagement			Nextcloud
Groupware			OX App Suite
Knowledge Management		XWiki
Portal & IAM			Nubus
Projectmanagement		Open-Project
Videoconference			Jitsi
Web-Office			Collabora


##Was braucht OpenDesk als Unterbau?
-----------------------------------------------------------------------------------------

OpenDesk arbeitet ausschlißlich in Clustern auf mehreren Servern.
Kubernetes und Container basiertes Arbeiten.

Kubernetes (K8s)- verwaltet viele Container auf mehreren Servern
Cluster- Mehrere Server, die zusammenarbeiten.
Helm/Helmfile- Installiert Anwendungen in Kubernetes nach Bauplan
Ingress Controller- Nimmt Anfragen von Aussen an und leitet es an den richtigen Dienst
Domain und DNS Service
Volume provisioner- Stellt Speicher für die Daten bereit
cert-manager / TLS- kümmert sich um HTTPS-Zertifikate

##Hardware:
---------------------------------------------------------------------------------------
Mindestangaben für eine Testversion:

CPU mindestens 12 Kerne x64 
RAM mindestens 32 GB, aber es wird mehr empfohlen
Speicher mehr als 10 GB
