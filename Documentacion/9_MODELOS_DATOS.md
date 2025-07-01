
# Creación de Esquemas o Modelos

- **Una de las principales características de FastAPI es la creación de los esquemas o modelos.**
- FastAPI se ayuda de una librería que ya viene integrada en la instalación.

- Esta librería se llama **Pydantic**
- **Es una librería que se encarga con todo lo relacionado con los datos y el tema de las validaciones.**

- En nuestros métodos tenemos que poner en los parámetros de las funciones de POST y PUT, todos los datos relacionados con una película.
- Agregar todos los datos en los parámetros de una función no es lo adecuado, ya que resultaría tedioso agregar 150 parámetros, si se requieren.

- **En casos como el ejemplo anterior es donde se pueden usar modelos de Pydantic.**

Ejemplo del uso de un modelo de Movie:

```
@app.post("/movies/", tags=["Movie"])
def create_movie(movie: Movie):
    movies.append(movie.model_dump())
    return movies
```

**El uso de los modelos, crea documentación de los modelos en Swagger:**

![[Pasted image 20250630225721.png]]

## Datos de modelo opcionales

- A diferencia de la función de POST, en la función de PUT no todos los datos del modelo son obligatorios.
- **Necesito que el campo id del modelo sea opcional**

- Use Optional de la librería typing y escribalo de esta forma:

```
from pydantic import BaseModel 
from typing import Optional

class Movie(BaseModel):
    id: Optional[int]
    title: str
    overview: str
    rating: float
    categories: list[str]
    year: str
```

**Ahora puede usar el modelo de datos movie, sin requerir obligatoriamente todos sus datos:**

```
@app.put("/movies/{id}", tags=["Movie"]) # Recibe un Request Path
def update_movies(id: int, movie:Movie):
    
    for mvie in movies:
        if mvie["id"] == id:
            mvie["title"] = movie.title
            mvie["overview"] = movie.overview
            mvie["rating"] = movie.rating
            mvie["categories"] = movie.categories
            mvie["year"] = movie.year
    return movies
```

- En el ejemplo anterior vio que el dato ID no es parte de movie, porque viene como un Path Param, y los demás con Body Params.

> [!DANGER]
> Recuerde que los modelos de datos hasta este momento, se han usado para Body Params.

# Modelos de Datos como Valores de Retorno en Funciones

```
@app.get("/movies", tags=["Movies"])
def moviesresponse() -> list[Movie]:
    return movies
```

















