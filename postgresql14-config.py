import os

# Actualizar paquetes del sistema
os.system('sudo apt-get update')

# Instalar PostgreSQL 14
os.system('sudo apt-get install postgresql-14')

# Iniciar servidor PostgreSQL
os.system('sudo service postgresql start')

# Crear superusuario
os.system('sudo -u postgres createuser -s -e alumno')
os.system('sudo -u postgres psql -c "alter user alumno with password \'alumno\'"')

# Permitir conexión desde cualquier red y dispositivo
os.system('sudo echo "host all all 0.0.0.0/0 trust" >> /etc/postgresql/14/main/pg_hba.conf')
os.system('sudo sed -i "s/#listen_addresses = \'localhost\'/listen_addresses = \'*\'/g" /etc/postgresql/14/main/postgresql.conf')
os.system('sudo service postgresql restart')
