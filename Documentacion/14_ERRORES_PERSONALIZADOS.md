
- Si usa la clase Field para agregar validaciones en los modelos de datos, esta opción le dará un mensaje de error por defecto. 
- **Si quiere tener mensajes de error por defecto tiene que dejar de usar la clase Field, y usar validator de la librería pydantic.**

```
from pydantic import validator, Field
```

```
class MoviePut(BaseModel):
    title: str
    overview: str = Field(min_length=15, max_length=50, default="Descripción random")
    rating: float = Field(ge=0, le=10, default = 10)
    categories: list[Annotated[str, StringConstraints(min_length=5, max_length=20)]]    
    year: str #= Field(le=datetime.date.today().year, ge=1900)


    @validator('title')
    def validate_title(cls, value):
        if len(value) < 5:
            raise ValueError("El título debe tener más de 15 caracteres")
        if len(value) > 15:
            raise ValueError("El título debe tener menos de 15 caracteres")
        return value
```

- Este validador se usa para tener validaciones más personalizadas. 
- Este validador envía nuestro mensaje de error en el JSON por defecto como respuesta a un error.

![[Pasted image 20250701114458.png]]










