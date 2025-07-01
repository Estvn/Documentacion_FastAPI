from fastapi import FastAPI as api, Body, Path, Query
from fastapi.responses import HTMLResponse as html, JSONResponse
from data import movies
from ModelMovie import Movie, MoviePut # Importando el modelo de datos
# import datetime

app = api() # Crear instancia de FastAPI
app.title = "App FastAPI" # Cambio del título de la documentación en Swagger
app.version = "0.0.1" # Agregando versión del proyecto para reflejar en la documentación

#-----------------------------------------------------------------------------
# MÉTODO GET

# Generando una ruta tipo GET
# El parámetro tags es el nombre del Endpoint (se podrá ver en la documentación de Swagger)
@app.get("/", tags=['Home']) 
def home():
    return JSONResponse({"valor" : "Hello World!"})

@app.get("/hola", tags=['Hola'])
def hola():
    return JSONResponse({"valor" : "hola"})

@app.get("/string", tags=["String"])
def string():
    return "Este endpoint retorna un String"

@app.get("/html", tags=["HTML"])
def htmlresponse():
    return html("<h1>Hola mundo!</h1>")

@app.get("/movies", tags=["Movies"])
def moviesresponse() -> list[Movie] | dict:
    return JSONResponse(content = [movie.model_dump() for movie in movies])

# ESTO ES UN PARÁMETRO DE RUTA
@app.get('/movies/{id}', tags=["Movie"])
# El parametro de la ruta se tiene que definir en la función para detectar
def get_movie(id:int = Path(ge=0)) -> Movie | dict:  
    for movie in movies:
        if movie.id == id:
            return movie.model_dump()
    return JSONResponse(content = {})
    '''
    try:
        return movies[id]
    except IndexError:
        return {"error": "Movie not found"}
    except Exception as e:
        return {"error": str(e)}
    '''

# PARÁMETRO QUERY
@app.get("/movies/", tags=["Movies"])
def get_movies_by_category(category: str = Query(min_length=5, max_length=20), year: str = Query(max_legth=4)) -> list[Movie] | dict:
    selected_movies = []
    for movie in movies:
        if category in movie.categories and movie.year == year:
            selected_movies.append(movie)
            return JSONResponse(content = [movie.model_dump() for movie in selected_movies])
    return JSONResponse(content = {})

#--------------------------------------------------------------------------------------
# METODOS POST

@app.post("/movies/", tags=["Movie"])
def create_movie(movie: Movie) -> list[Movie]:
    movies.append(movie) # Agrega un objeto Movie en el arreglo
    return JSONResponse(content = [movie.model_dump() for movie in movies]) # Convierte los arreglos en diccionarios/JSON 

#--------------------------------------------------------------------------------------
# METODOS PUT

@app.put("/movies/{id}", tags=["Movie"]) # Recibe un Request Path
def update_movies(id: int, movie:MoviePut) -> list[Movie]:
    for mvie in movies:
        if mvie.id == id:
            mvie.title = movie.title
            mvie.overview = movie.overview
            mvie.rating = movie.rating
            mvie.categories = movie.categories
            mvie.year = movie.year
    return JSONResponse(content = [movie.model_dump() for movie in movies])

#--------------------------------------------------------------------------------------
# METODOS DELETE

@app.delete("/movies/{id}", tags=["Movie"])
def delete_movie(id: int) -> list[Movie]:
    for movie in movies:
        if movie.id == id:
            movies.remove(movie)
    return JSONResponse(content = [movie.model_dump() for movie in movies])



















