
- Los parámetros de ruta son valores que podemos pasar dentro de la URL.

Por ejemplo, si queremos pasar un valor numérico, lo hacemos de esta forma:

```
proyecto.com/modulo/{parametro}
```

Para identificar el parámetros en los Endpoints de FastAPI, lo hacemos de esta forma:

```
@app.get("/movies/{id}", tags=["movies"])
```

- El nombre del parámetro de la ruta también se tiene que definir como parámetro en la función que ejecuta el Endpoint

```
@app.get('/movies/{id}', tags=["Movies with params"])
def get_movie(id:int):
    try:
        return movies[id]
    except IndexError:
        return {"error": "Movie not found"}
    except Exception as e:
        return {"error": str(e)}
```

