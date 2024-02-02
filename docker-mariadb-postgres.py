#!/usr/bin/env python

import os
# Desinstalar Docker si existia
os.system('sudo apt-get purge docker-ce -y')

# Instalar Docker CE
os.system('sudo apt-get update')
os.system('sudo apt-get install -y apt-transport-https ca-certificates curl gnupg lsb-release')
os.system('sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc')
os.system('sudo chmod a+r /etc/apt/keyrings/docker.asc')
os.system('echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu jammy stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null')
os.system('sudo apt-get update')
os.system('sudo apt-get install -y docker-ce docker-ce-cli containerd.io')

# Instalar Portainer
os.system('sudo docker volume create portainer_data')
os.system('sudo docker run -d -p 9000:9000 --name portainer --restart always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer')

# Instalar MariaDB persistente
os.system('sudo docker volume create mariadb_data')
os.system('sudo docker run -d -p 3306:3306 --name mariadb --restart always -v mariadb_data:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=alumno -e MYSQL_USER=alumno -e MYSQL_PASSWORD=alumno mariadb')

# Instalar PostgreSQL persistente
os.system('sudo docker volume create postgres_data')
os.system('sudo docker run -d -p 5432:5432 --name postgres --restart always -v postgres_data:/var/lib/postgresql/data -e POSTGRES_PASSWORD=alumno -e POSTGRES_USER=alumno postgres')

# Instalar DBeaver-CE
os.system('wget https://dbeaver.io/files/dbeaver-ce_latest_amd64.deb')
os.system('sudo dpkg -i ./dbeaver-ce_latest_amd64.deb')
print('Todo terminado!')
