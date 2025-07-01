
- El método PUT puede enviar el identificador del elemento a actualizar como un Path Param, y los demás valores a actualizar como Body Params.

- En el método PUT se necesitan Path Params y Request Body.
- Ambos valores se agregan en los parámetros de la función, pero el parámetro de tipo Path no se le asigna el valor "= Body()".
- **La función del Endpoint DELETE no necesita Body Params.**

Método POST

```
@app.put("/movies/{id}", tags=["Movie"]) # Recibe un Request Path
def update_movies(
    id: int, # No se define Body()
    title: str = Body(),
    overview: str = Body(),
    rating: float = Body(),
    categories: list[str] = Body(),
    year: str = Body()):

    for movie in movies:
        if movie["id"] == id:
            movie["title"] = title
            movie["overview"] = overview
            movie["rating"] = rating
            movie["categories"] = categories
            movie["year"] = year
    return movies
```

Método DELETE:

```
@app.delete("/movies/{id}", tags=["Movie"])
def delete_movie(id: int):
    for movie in movies:
        if movie["id"] == id:
            movies.remove(movie)
    return movies
```