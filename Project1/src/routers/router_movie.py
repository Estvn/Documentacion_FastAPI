from fastapi import Path, Body, Query, APIRouter
from fastapi.responses import JSONResponse, RedirectResponse

from ..models.model_movie import Movie, MoviePut
from ..database.database_movie import movies

movie_router = APIRouter()

@movie_router.get("/", tags=["Movie"])
def moviesresponse() -> list[Movie] | dict:
    return JSONResponse(content = [movie.model_dump() for movie in movies])

# ESTO ES UN PARÁMETRO DE RUTA
@movie_router.get('/{id}', tags=["Movie"])
# El parametro de la ruta se tiene que definir en la función para detectar
def get_movie(id:int = Path(ge=0)) -> Movie | dict:  
    for movie in movies:
        if movie.id == id:
            return movie.model_dump()
    return JSONResponse(content = {}, status_code = 404)

# PARÁMETRO QUERY
@movie_router.get("/by_category", tags=["Movie"])
def get_movies_by_category(category: str = Query(min_length=5, max_length=20), year: str = Query(max_legth=4)) -> list[Movie] | dict:
    selected_movies = []
    for movie in movies:
        if category in movie.categories and movie.year == year:
            selected_movies.movie_routerend(movie)
            return JSONResponse(content = [movie.model_dump() for movie in selected_movies])
    return JSONResponse(content = {})

#--------------------------------------------------------------------------------------
# METODOS POST

@movie_router.post("/", tags=["Movie"])
def create_movie(movie: Movie):
    movies.movie_routerend(movie) # Agrega un objeto Movie en el arreglo
    return JSONResponse(content = [movie.model_dump() for movie in movies], status_code = 201) # Convierte los arreglos en diccionarios/JSON 
    # return RedirectResponse("/movies", status_code=303)

#--------------------------------------------------------------------------------------
# METODOS PUT

@movie_router.put("/{id}", tags=["Movie"]) # Recibe un Request Path
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

@movie_router.delete("/{id}", tags=["Movie"])
def delete_movie(id: int) -> list[Movie]:
    for movie in movies:
        if movie.id == id:
            movies.remove(movie)
    return JSONResponse(content = [movie.model_dump() for movie in movies])
