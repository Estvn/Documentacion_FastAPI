
> [!DANGER]
> Los parámetros de tipo POST tienen que mandarse tipo request BODY

- **En el siguiente ejemplo**, los parámetros que se envían en un método POST se mandan de igual forma que los parámetros QUERY están siendo definidos como parámetros de la función.
- En los parámetros de la función POST puede enviar, str, int, list[], etc.

```
@app.post("/movies/")
def create_movie(
					id: int, title: str, overview: str,
                    rating: float, categories: list[str], year: str):
    movies.append({
        "id": id,
        "title": title,
        "overview": overview,
        "rating": rating,
        "categories": categories,
        "year": year
    })
    return movie[2]
```

Si dejamos la función de esta forma, los parámetros serán parte de la petición:

![[Pasted image 20250630161314.png]]

> [!DANGER]
> - A pesar de que los valores POST se pueden enviar por medio de la definición de los REQUEST PARAM, no es lo ideal.
> - **Importe la clase Body de FastAPI para enviar parámetros Body**
> 

# Clase Body para la Definición de Endpoint POST

**Importación de la clase Body**

```
from fastapi import Body
```

Definición de la función:

```
@app.post("/movies/")
def create_movie(
    id: int = Body(),
    title: str = Body(),
    overview: str = Body(),
    rating: float = Body(),
    categories: list[str] = Body(),
    year: str = Body()):
    movies.append({
        "id": id,
        "title": title,
        "overview": overview,
        "rating": rating,
        "categories": categories,
        "year": year
    })
    return movies[2]
```

Al insertar parámetros de tipo Body, ahora se solicita lo siguiente:

![[Pasted image 20250630172247.png]]

> [!IMPORTANT]
> Con el uso de la clase Body de FastAPI, los parámetros de la función POST son parámetros de tipo Body, y no Request.












