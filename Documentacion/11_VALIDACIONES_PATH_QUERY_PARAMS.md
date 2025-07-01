
- **Para validaciones de los parámetros de ruta se usa la clase Path de la librería fastapi.**
- Funciona exactamente de la misma forma que las validaciones en los modelos de datos, solo que las validaciones de los parámetros de ruta se añaden en los parámetros de la función que corresponden a los parámetros de ruta.

```
from fastapi import Path
```

Validación de parámetros Path:

```
@app.get('/movies/{id}', tags=["Movie"])
def get_movie(id:int = Path(ge=0)) -> Movie | dict:  

    for movie in movies:
        if movie["id"] == id:
            return movie
    return {}
```

- **Para validar parámetros Query, solo tiene que importar la clase Query de fastapi y usarla de la misma forma que las validaciones de los modelos y parámetros de rutas.**

Validación de parámetros Query:

```
@app.get("/movies/", tags=["Movies"])
def get_movies_by_category(category: str = Query(min_length=5, max_length=20), year: str = Query(max_legth=4)) -> list[Movie] | dict:
    selected_movies = []
    for movie in movies:
        if category in movie["categories"] and movie["year"] == year:
            selected_movies.append(movie)
            return selected_movies
    return {}
```