from fastapi import FastAPI as api
from fastapi.responses import Response, JSONResponse, PlainTextResponse
from fastapi.requests import Request

from src.routers.router_movie import movie_router
from src.routers.router_file import file_router
from src.routers.router_random import random_router
from src.utils.http_error_handler import HTTPErrorHandler

app = api() # Crear instancia de FastAPI
app.title = "App FastAPI" # Cambio del título de la documentación en Swagger
app.version = "0.0.1" # Agregando versión del proyecto para reflejar en la documentación

# app.add_middleware(HTTPErrorHandler)

@app.middleware("http")
async def http_error_handler(request: Request, call_next) -> Response | JSONResponse:
    print("Middleware is running")
    return await call_next(request)

app.include_router(prefix="/movies", router=movie_router)
#app.include_router(router=file_router)
#app.include_router(router=random_router)

@app.get("/", tags=['Home'], status_code = 500, response_description = "Mensaje de descripción de respuesta") 
def home():
    return PlainTextResponse(content = "Home")
