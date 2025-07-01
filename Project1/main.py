from fastapi import FastAPI as api, Body
from fastapi.responses import HTMLResponse as html
from data import movies

app = api() # Crear instancia de FastAPI
app.title = "App FastAPI" # Cambio del título de la documentación en Swagger
app.version = "0.0.1" # Agregando versión del proyecto para reflejar en la documentación

#-----------------------------------------------------------------------------
# MÉTODO GET

# Generando una ruta tipo GET
# El parámetro tags es el nombre del Endpoint (se podrá ver en la documentación de Swagger)
@app.get("/", tags=['Home']) 
def home():
    return {"valor" : "Hello World!"}

@app.get("/hola", tags=['Hola'])
def hola():
    return {"valor" : "hola"}

@app.get("/string", tags=["String"])
def string():
    return "Este endpoint retorna un String"

@app.get("/html", tags=["HTML"])
def htmlresponse():
    return html("<h1>Hola mundo!</h1>")

@app.get("/movies", tags=["Movies"])
def moviesresponse():
    return movies

# ESTO ES UN PARÁMETRO DE RUTA
@app.get('/movies/{id}', tags=["Movie"])
# El parametro de la ruta se tiene que definir en la función para detectar
def get_movie(id:int):  
    for movie in movies:
        if movie["id"] == id:
            return movie
        
    return []
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
def get_movies_by_category(category: str, year: str):
    selected_movies = []
    for movie in movies:
        if category in movie["categories"] and movie["year"] == year:
            selected_movies.append(movie)
    return selected_movies

#--------------------------------------------------------------------------------------
# METODOS POST

@app.post("/movies/", tags=["Movie"])
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
    return movies

#--------------------------------------------------------------------------------------
# METODOS PUT

@app.put("/movies/{id}", tags=["Movie"]) # Recibe un Request Path
def update_movies(
    id: int,
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

#--------------------------------------------------------------------------------------
# METODOS DELETE

@app.delete("/movies/{id}", tags=["Movie"])
def delete_movie(id: int):
    for movie in movies:
        if movie["id"] == id:
            movies.remove(movie)
    return movies



















