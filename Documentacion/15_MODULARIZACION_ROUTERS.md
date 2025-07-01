
- En las carpetas que se van creando, se tiene que crear el archivo `__init__.py` para que la aplicación detecte que la carpeta es un módulo.

- Para usar el enrutador de FastAPI, ya no tiene que usar el objeto `FastAPI` de la librería fastapi.
- **Ahora tiene que usar el objeto `APIRouter`  de la librería fastapi.**

```
from fastapi import APIRouter
random_router = APIRouter()
```

```
 uvicorn src.main:app --reload
```


![[Pasted image 20250701140137.png]]

```
from fastapi import FastAPI as api, Body, Path, Query
from fastapi.responses import HTMLResponse as html, JSONResponse, PlainTextResponse, RedirectResponse, FileResponse

from src.routers.router_movie import movie_router
from src.routers.router_file import file_router
from src.routers.router_random import random_router

app = api() 
app.title = "App FastAPI" 
app.version = "0.0.1" 

app.include_router(router=movie_router)
app.include_router(router=file_router)
app.include_router(router=random_router)

@app.get("/", tags=['Home'], status_code = 500, response_description = "Mensaje de descripción de respuesta")

def home():

    return PlainTextResponse(content = "Home")
```

## Agregando Prefijo en las Rutas

Si mira, todas las rutas tienen una palabra que se repite

![[Pasted image 20250701141314.png]]

- Puede resumir estos añadiendo un prefijo, de la siguiente forma

```
app.include_router(prefix="/movies", router=movie_router)
```

> [!WARNING]
> Si va a agregar prefijos, tiene que eliminar la `/palabra` de los Endpoints.
> Solo tiene que dejar una `/` en los Endpoint, y con sus Path params, si los tiene.

> [!DANGER]
> - Cuidado al tener rutas similares, una puede sobrescribirse en otra. Lo ideal es tener a todas las rutas con un nombre único. Puede ser un nombre extra en la ruta.
> - Pero si tiene  varias rutas con el mismo nombre, y de diferente nombre tipo de petición, **No hay problema.**





