# Biblioteca API
Esta es una API RESTful para la gestión de una biblioteca.

## Clonar el Repositorio
Para clonar el repositorio, utiliza el siguiente comando en tu terminal:
    ```bash
git clone https://github.com/usuario/repo.git

- **Crear entorno virtual**
    ```bash 
python -m venv env

- **Activar entorno virtual windows | linux**
    ```bash 
.\env\Scripts\activate  |  source env/bin/activate

- **Instalar dependencias**
    ```bash 
pip install -r requirements.txt

- **Crear base datos manual o con comando**
    ```bash 
CREATE DATABASE biblioteca_db;

- **Configura las credenciales de conexión en el archivo settings.py**


- **Realizar las migraciones de base de datos**
    ```bash 
python manage.py migrate

- **Cargar datos iniciales (Bonus)**
    ```bash 
python manage.py loaddata datos_iniciales.json


- **Ejecutar la Aplicación**
    ```bash 
python manage.py runserver




#### Endpoints Autores
- **1. GET Listar Todos Autores**
  ```bash cmd
curl -X GET http://127.0.0.1:8000/api/autores/


- **2. POST Nuevo Autores**
  ```bash cmd
curl -X POST http://127.0.0.1:8000/api/autores/ -H "Content-Type: application/json" -d "{\"nombre\": \"Joaquin\", \"apellido\": \"Morales Arechiga\", \"fecha_nacimiento\": \"2007-03-06\"}"


- **3. GET Obtener Autor con id : 1**
  ```bash cmd
curl -X GET http://127.0.0.1:8000/api/autores/1/


- **4. PUT Modificar Autor con id : 1**
  ```bash cmd
curl -X PUT http://127.0.0.1:8000/api/autores/1/ -H "Content-Type: application/json" -d "{\"nombre\": \"Jhon\", \"apellido\": \"Lopez Mena\", \"fecha_nacimiento\": \"2000-01-01\"}"


- **5. DELETE Eliminar el primer Autor**
  ```bash cmd
curl -X DELETE http://127.0.0.1:8000/api/autores/1/

#### Endpoints Libros

- **1. GET Listar Todos Libros**
  ```bash cmd
curl -X GET http://127.0.0.1:8000/api/libros/


- **2. POST Nuevo Libro**
  ```bash cmd
curl -X POST http://127.0.0.1:8000/api/libros/ -H "Content-Type: application/json" -d "{\"titulo\": \"Libro Ejemplo\", \"fecha_publicacion\": \"2023-01-01\", \"autor\": 1}"


- **3. GET Obtener Libro con id : 1**
  ```bash cmd
curl -X GET http://127.0.0.1:8000/api/libros/1/


- **4. PUT Modificar Libro con id : 1**
  ```bash cmd
curl -X PUT http://127.0.0.1:8000/api/libros/1/ -H "Content-Type: application/json" -d "{\"titulo\": \"Nuevo Titulo\", \"fecha_publicacion\": \"2022-08-15\", \"autor\": 1}"



- **5. DELETE Eliminar el primer autor**
  ```bash cmd
curl -X DELETE http://127.0.0.1:8000/api/libros/1/


