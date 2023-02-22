# utils-python
Scripts para la instalación y configuración de sistemas de manera automatizada

a. Script para la instalación de docker-ce, portainer, mariadb y postgresql en un servidor linux

[docker-mariadb-postgres.py](https://github.com/darioaxel/utils-python/blob/main/docker-mariadb-postgres.py)

b. Script para configurar un router en Ubuntu Server que gestione dos redes, utilizando IPTABLES:
  RED A: 10.0.1.0   interfaz: enp0s2  
  RED B: 10.0.2.0   interfaz: enp0s8
  
 Al router se le asigna la última IP del rango y hace de firewall del exterior ante ambas redes. 
 Además se permite: 
   RED A: Acceso a internet
   > iptables --table nat -A POSTROUTING -o enp0s2 -j MASQUERADE
          Acceso mediante ssh
   > iptables -A INPUT -i enp0s3 -p tcp --dport ssh -j ACCEPT
          Acceso mediante ftp
   > iptables -A INPUT -i enp0s3 -p tcp --dport ftp -j ACCEPT")
          El resto de puertos queda cerrado
   > iptables -A INPUT -i enp0s3 -j DROP
   
   
   RED B:  Acceso mediante ssh
   > iptables -A INPUT -i enp0s8 -p tcp --dport ssh -j ACCEPT
          Acceso mediante ftp
   > iptables -A INPUT -i enp0s8 -p tcp --dport ftp -j ACCEPT")
          El resto de puertos queda cerrado
   > iptables -A INPUT -i enp0s8 -j DROP
   
   [router-2networks-iptables.py](https://github.com/darioaxel/utils-python/blob/main/router-2networks-iptables.py)
