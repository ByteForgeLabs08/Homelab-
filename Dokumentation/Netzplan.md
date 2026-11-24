#Netzplan fisi.lab

**Netz:** 172.16.29.0/24
**Gateway:** 172.16.29.1
**DNS:** 172.16.29.47 (DC01)

| Hostname       |    Rolle     |  IP-Adresse   | Statisch/DHCP |    Betriebssystem      |
| HV01           | Hyper-V-Host | 172.16.29.68  | statisch      | Windows Server 2019    |
| DC01           | Domain Contr.| 172.16.29.47  | statisch      | Windows Server 2022    |
|CLIENT01        | Client       | 172.16.29.49  | dynamisch     | Windows 11 Pro         |
|Ubuntu-Admin-Lab|Admin,Docker  | 172.16.29.45  | statisch      | Ubuntu LTS             |


##Docker-Dienste

|  Container  |      Host        |  Port außen -> innen  | 
| fisi-web01  | ubuntu-admin-lab | 8080:80               |




In PowerShell:

Get-VMNetworkAdapter -VMName * | Select-Object VMName, IPAddresses, SwitchName
zeigt alle Adressen und Clients in der Domäne!!!
