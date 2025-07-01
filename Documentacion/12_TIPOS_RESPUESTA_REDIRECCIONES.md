
- Por defecto, las respuestas de la API son JSONs.
- **Se puede poner diferentes respuestas por cada función que retorna algo al cliente.**

```
from fastapi.responses import JSONResponse, PlainTextResponse
```

```
@app.delete("/movies/{id}", tags=["Movie"])
def delete_movie(id: int) -> list[Movie]:
    for movie in movies:
        if movie.id == id:
            movies.remove(movie)
    return JSONResponse(content = [movie.model_dump() for movie in movies])
```

- JSONResponse devuelve un JSON
- PlainTextResponse devuelve un texto plano sin formato

## Redirecciones

```
from fastapi.responses import RedirectResponse
```

```
@app.post("/movies/", tags=["Movie"])
def create_movie(movie: Movie):
    movies.append(movie)
    return RedirectResponse("/movies", status_code=303)
```

## Respuesta de Archivo

- Puede enviar como respuesta un archivo

```
from fastapi.responses import FileResponse
```

```
@app.get("/get_file", tags="File")
def get_file():
    return FileResponse("./file/Proyecto1-2.pdf")

@app.get("/get_img", tags=["Image"])
def get_img():
    return FileResponse("./file/camera-2931883_1280.jpg")
```


































