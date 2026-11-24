# fisi-web01

Einfacher nginx-Webserver im Docker-Container.

##Starten

docker run -d --name fisi-web01 -p 8080:80 --restart unless-stopped \-v ~/Homelab-/Docker/fisi-web01/html:/usr/share/nginx
/html:ro nginx

##Erreichbar

http://<IP-der-Ubuntu_VM>:8080

