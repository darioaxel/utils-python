#!/usr/bin/env python

import os

# Desinstalar Docker si existia
os.system('sudo apt-get purge docker-ce -y')

# Instalar Docker CE
os.system('sudo apt-get update')
os.system('sudo apt-get install -y apt-transport-https ca-certificates curl gnupg lsb-release')
os.system('sudo mkdir -p /etc/apt/keyrings')
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

# Instalar MongoDB Community Edition como contenedor Docker
os.system('sudo docker volume create mongodb_data')
os.system('sudo docker run -d -p 27017:27017 --name mongodb --restart always -v mongodb_data:/data/db mongo')

# Instalar MongoDB Compass
os.system('wget https://downloads.mongodb.com/compass/mongodb-compass_1.36.0_amd64.deb')
os.system('sudo dpkg -i mongodb-compass_1.36.0_amd64.deb')
os.system('sudo apt-get install -f -y')  # Para instalar dependencias faltantes

# Instalar Visual Studio Code
os.system('wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg')
os.system('sudo install -o root -g root -m 644 microsoft.gpg /etc/apt/trusted.gpg.d/')
os.system('sudo sh -c \'echo "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main" > /etc/apt/sources.list.d/vscode.list\'')
os.system('sudo apt-get install -y apt-transport-https')
os.system('sudo apt-get update')
os.system('sudo apt-get install -y code')

print('Todo terminado!')

