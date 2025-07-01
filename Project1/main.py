from fastapi import FastAPI as api, Body, Path, Query
from fastapi.responses import HTMLResponse as html, JSONResponse, PlainTextResponse, RedirectResponse, FileResponse
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
# Los otros parámetros son para documentar más precisa la API
@app.get("/", tags=['Home'], status_code = 500, response_description = "Mensaje de descripción de respuesta") 
def home():
    return PlainTextResponse(content = "Home")

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
    return JSONResponse(content = {}, status_code = 404)

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
def create_movie(movie: Movie):
    movies.append(movie) # Agrega un objeto Movie en el arreglo
    return JSONResponse(content = [movie.model_dump() for movie in movies], status_code = 201) # Convierte los arreglos en diccionarios/JSON 
    # return RedirectResponse("/movies", status_code=303)

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

# ENVIAR ARCHIVO
@app.get("/get_file", tags="File")
def get_file():
    return FileResponse("./file/Proyecto1-2.pdf")

@app.get("/get_img", tags=["Image"])
def get_img():
    return FileResponse("./file/camera-2931883_1280.jpg")


