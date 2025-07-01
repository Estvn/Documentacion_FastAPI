
- Primero vaya al command palette de VS Code y seleccione el interprete de Python que está dentro de la carpeta del entorno virtual que ha creado.

```
from fastapi import FastAPI as api

app = api() # Crear instancia de FastAPI

@app.get("/") # Generando una ruta tipo GET
def home():
    return "Hello World"
```

Use el siguiente comando para ejecutar el proyecto:

```
uvicorn main:app
```

- main es el nombre del archivo
- app es el nombre de la variable que tiene la instancia de FastAPI.

- Cuando ejecutamos nuestra aplicación, por defecto nos asigna el puerto 8000

**Para elegir manualmente el puerto, usamos el siguiente comando:**

```
uvicorn main:app --port 5000
```

- Cuando hacemos un cambio en nuestra aplicación, los cambios no se reflejan automáticamente

**Para que la aplicación refleje los cambios de nuestra aplicación automáticamente, usamos el siguiente comando:**

```
uvicorn main:app --port 5000 --reload
```

**Para lograr que el proyecto se pueda acceder a la red en la que estoy conectado, uso el siguiente comando:**

```
uvicorn main:app --port 500 --reload --host 0.0.0.0
```

















