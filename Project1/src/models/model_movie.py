from pydantic import BaseModel, Field, StringConstraints, validator # Una clase de pydantic para crear modelos de datos
from typing import Optional, Annotated
# import datetime

# gt -> greater than
# ge -> greater or equal
# lt -> less than
# le -> less or equal

class MoviePut(BaseModel):
    title: str 
    overview: str = Field(min_length=15, max_length=50, default="Descripción random")
    rating: float = Field(ge=0, le=10, default = 10)
    categories: list[Annotated[str, StringConstraints(min_length=5, max_length=20)]] # Valida los valores del arreglo
    year: str #= Field(le=datetime.date.today().year, ge=1900)

    # Valores por defecto para los datos del modelo (sin relevancia)
    model_config = {
        "json_schema_extra" : {
            "id": 1,
            "title" : "Título",
            "overview": "Descripción rápida",
            "rating": 10,
            "categories": ["action"],
            "year": "2025"
        }
    }

    @validator('title')
    def validate_title(cls, value):
        if len(value) < 5:
            raise ValueError("El título debe tener más de 15 caracteres")
        if len(value) > 15:
            raise ValueError("El título debe tener menos de 15 caracteres")
        return value

class Movie(MoviePut):
    id: Optional[int]


