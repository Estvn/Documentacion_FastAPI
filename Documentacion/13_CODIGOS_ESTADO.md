
**Hay dos formas de agregar códigos de estado:**
1. Como parámetro en el retorno de la función
2. Asignar el código de estado por defecto en el parámetro del Endpoint

- **Las APIs de FastAPI retornan por defecto códigos de estado.**
- El uso de los códigos de estado es simple, lo agrega como parámetro dentro del JSONResponse o cualquier respuesta que esté enviando.

```
@app.get('/movies/{id}', tags=["Movie"])
def get_movie(id:int = Path(ge=0)) -> Movie | dict:  
    for movie in movies:
        if movie.id == id:
            return movie.model_dump()
    return JSONResponse(content = {}, status_code = 404)
```

```
@app.post("/movies/", tags=["Movie"])
def create_movie(movie: Movie):
    movies.append(movie) # Agrega un objeto Movie en el arreglo
    return RedirectResponse("/movies", status_code=303)
```

## Código de respuesta por defecto

- La API asigna códigos de respuesta por defecto en los Endpoints
- Para modificarlo, simplemente agregamos el parámetro status_code en el Endpoint con el código de respuesta deseado.

```
@app.get("/", tags=['Home'], status_code = 500, response_description="Mensaje de descripción de respuesta")
def home():
    return PlainTextResponse(content = "Home")
```
 
![[Pasted image 20250701111008.png]]

> [!IMPORTANT]
> Estos parámetros en el Endpoint se asignan para tener una documentación más cierta sobre la API.







