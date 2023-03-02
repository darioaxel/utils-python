import docker

# Configuración del cliente de Docker
docker_client = docker.from_env()

# Configuración del contenedor de MySQL
container_name = "mysql-container"
image_name = "mysql"
root_password = "password"
port_mapping = {"3306": "3306"}
environment_vars = {"MYSQL_ROOT_PASSWORD": root_password}
container = docker_client.containers.run(
    image_name,
    name=container_name,
    detach=True,
    ports=port_mapping,
    environment=environment_vars,
)

# Creación de la base de datos y las tablas
db_name = "profesoresDB"
table_profesores = """
CREATE TABLE IF NOT EXISTS Profesores (
  ID INT NOT NULL AUTO_INCREMENT,
  nombre VARCHAR(255) NOT NULL,
  correo_electronico VARCHAR(255) NOT NULL,
  PRIMARY KEY (ID)
);
"""
table_log = """
CREATE TABLE IF NOT EXISTS Log (
  ID INT NOT NULL AUTO_INCREMENT,
  Instante DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  accion TEXT NOT NULL,
  PRIMARY KEY (ID)
);
"""
container.exec_run(f"mysql -u root -p{root_password} -e 'CREATE DATABASE IF NOT EXISTS {db_name}'")
container.exec_run(f"mysql -u root -p{root_password} {db_name} -e '{table_profesores}'")
container.exec_run(f"mysql -u root -p{root_password} {db_name} -e '{table_log}'")

print(f"El contenedor de MySQL {container_name} se ha creado y la base de datos {db_name} con las tablas indicadas se ha creado correctamente.")
