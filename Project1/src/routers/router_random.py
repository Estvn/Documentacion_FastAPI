from fastapi import APIRouter
from fastapi.responses import PlainTextResponse, JSONResponse, HTMLResponse as html

random_router = APIRouter()

# MÉTODO GET
# Generando una ruta tipo GET
# El parámetro tags es el nombre del Endpoint (se podrá ver en la documentación de Swagger)
# Los otros parámetros son para documentar más precisa la API
@random_router.get("/hola", tags=['Hola'])
def hola():
    return JSONResponse({"valor" : "hola"})

@random_router.get("/string", tags=["String"])
def string():
    return "Este endpoint retorna un String"

@random_router.get("/html", tags=["HTML"])
def htmlresponse():
    return html("<h1>Hola mundo!</h1>")
