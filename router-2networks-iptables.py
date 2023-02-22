#!/usr/bin/python

import os

# Configuración de la interfaz de red para la red 10.0.1.0/24
os.system("ip link set enp0s3 up")
os.system("ip link set enp0s3 address 00:11:22:33:44:55")
os.system("ip -6 address add fd20:8b1e:bdef:0::1/64 dev enp0s3")
os.system("ip address add 10.0.1.254/24 dev enp0s3")
os.system("echo 1 > /proc/sys/net/ipv4/ip_forward")
os.system("iptables --table nat -A POSTROUTING -o enp0s2 -j MASQUERADE")
os.system("iptables -A INPUT -i enp0s3 -p tcp --dport ssh -j ACCEPT")
os.system("iptables -A INPUT -i enp0s3 -p tcp --dport ftp -j ACCEPT")
os.system("iptables -A INPUT -i enp0s3 -j DROP")

# Configuración de la interfaz de red para la red 10.0.2.0/24
os.system("ip link set enp0s8 up")
os.system("ip link set enp0s8 address 00:11:22:33:44:66")
os.system("ip -6 address add fd30:8b1e:bdef:0::1/64 dev enp0s8")
os.system("ip address add 10.0.2.254/24 dev enp0s8")
os.system("ip route add 10.0.1.0/24 via 10.0.2.254 dev enp0s8")
os.system("iptables -A INPUT -i enp0s8 -p tcp --dport ssh -j ACCEPT")
os.system("iptables -A INPUT -i enp0s8 -p tcp --dport ftp -j ACCEPT")
os.system("iptables -A INPUT -i enp0s8 -j DROP")

# Configuración del nombre del router y hosts
os.system("echo 'net-router' > /etc/hostname")
os.system("echo '127.0.0.1 localhost' > /etc/hosts")
os.system("echo '10.0.1.254 net-router' >> /etc/hosts")
os.system("echo '10.0.2.254 dhcpd' >> /etc/hosts")

# Configuración del servidor DHCP
os.system("apt-get update")
os.system("apt-get install -y isc-dhcp-server")
dhcp_conf = open('/etc/dhcp/dhcpd.conf', 'w')
dhcp_conf.write('subnet 10.0.1.0 netmask 255.255.255.0 {\n  range 10.0.1.10 10.0.1.200;\n  option routers 10.0.1.
