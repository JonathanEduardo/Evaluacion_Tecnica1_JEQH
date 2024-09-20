# Biblioteca API
Esta es una API RESTful para la gestión de una biblioteca.
This is a RESTful API for managing a library.

## Clonar el Repositorio
- **Para clonar el repositorio, utiliza el siguiente comando en tu terminal:**
- **To clone the repository, use the following command in your terminal:**
```bash
git clone https://github.com/JonathanEduardo/Evaluacion_Tecnica1_JEQH.git
```

- **Crear entorno virtual**
- **Create a virtual environment**
```bash 
python -m venv env
```

- **Activar entorno virtual windows | linux**
- **Activate virtual environment for Windows | Linux**
```bash 
.\env\Scripts\activate  |  source env/bin/activate
```

- **Instalar dependencias**
- **Install dependencies**
```bash 
pip install -r requirements.txt
```

- **Crear base datos manual o con comando**
- **Create Data Base manually or using a command**
```bash 
CREATE DATABASE biblioteca_db;
```

- **Configura las credenciales de conexión en el archivo settings.py**
- **Set up the database connection credentials in the settings.py file**


- **Realizar las migraciones de base de datos**
- **Make database migration**
```bash 
python manage.py migrate
```

- **Cargar datos iniciales json**
- **Load initial data json**
```bash 
python manage.py loaddata datos_iniciales.json
```


- **Ejecutar la Aplicación**
- **Run Application**
```bash 
python manage.py runserver
```




#### Endpoints Autores
- **1. GET Listar Todos Autores**
- **1. GET List All Authors**
```bash
curl -X GET http://127.0.0.1:8000/api/autores/
```


- **2. POST Nuevo Autores**
- **2. POST New Author**
```bash cmd
curl -X POST http://127.0.0.1:8000/api/autores/ -H "Content-Type: application/json" -d "{\"nombre\": \"Joaquin\", \"apellido\": \"Morales Arechiga\", \"fecha_nacimiento\": \"2007-03-06\"}"
```


- **3. GET Obtener Autor con id : 1**
- **3. GET Retrieve Author with ID: 1**
```bash
curl -X GET http://127.0.0.1:8000/api/autores/1/
```

- **4. PUT Modificar Autor con id : 1**
- **4. PUT Update Author with ID: 1**
```bash c
curl -X PUT http://127.0.0.1:8000/api/autores/1/ -H "Content-Type: application/json" -d "{\"nombre\": \"Jhon\", \"apellido\": \"Lopez Mena\", \"fecha_nacimiento\": \"2000-01-01\"}"
```

- **5. DELETE Eliminar el primer Autor**
- **5. PUT Delete Author with ID: 1**
```bash cmd
curl -X DELETE http://127.0.0.1:8000/api/autores/1/
```
#### Endpoints Libros

- **1. GET Listar Todos Libros**
- **1. GET List All Books**
```bash cmd
curl -X GET http://127.0.0.1:8000/api/libros/
```

- **2. POST Nuevo Libro**
- **2. POST New Book**
```bash cmd
curl -X POST http://127.0.0.1:8000/api/libros/ -H "Content-Type: application/json" -d "{\"titulo\": \"Libro Ejemplo\", \"fecha_publicacion\": \"2023-01-01\", \"autor\": 1}"
```

- **3. GET Obtener Libro con id : 1**
- **3. GET Retrieve Book with ID: 1**
```bash cmd
curl -X GET http://127.0.0.1:8000/api/libros/1/
```

- **4. PUT Modificar Libro con id : 1**
- **4. PUT Update Book with ID: 1**
```bash cmd
curl -X PUT http://127.0.0.1:8000/api/libros/1/ -H "Content-Type: application/json" -d "{\"titulo\": \"Nuevo Titulo\", \"fecha_publicacion\": \"2022-08-15\", \"autor\": 1}"
```


- **5. DELETE Eliminar el primer autor**
- **5. PUT Delete Book with ID: 1**
```bash cmd
curl -X DELETE http://127.0.0.1:8000/api/libros/1/
```

