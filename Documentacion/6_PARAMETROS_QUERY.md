
```
localhost:5000/movies?category=action
```

- Los parámetros Query en FastAPI tienen que finalizar con "/", como buena práctica para evitar que se reemplace la ruta original.
- **A diferencia de los parámetros de ruta que se definen en la ruta (a nivel de código), los parámetros Query solo se definen en la función del Endpoint**
- Puede agregar tantos parámetros como quiera

```
@app.get("/movies/", tags=["Category Movie Endpoint"])
def get_movies_by_category(category: str, year: str):
    selected_movies = []
    for movie in movies:
        if category in movie["categories"]:
            selected_movies.append(movie)
    return selected_movies
```

