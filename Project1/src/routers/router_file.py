from fastapi import APIRouter
from fastapi.responses import FileResponse

file_router = APIRouter()

# ENVIAR ARCHIVO
@file_router.get("/get_file", tags="File")
def get_file():
    return FileResponse("./file/Proyecto1-2.pdf")

@file_router.get("/get_img", tags=["Image"])
def get_img():
    return FileResponse("./file/camera-2931883_1280.jpg")


