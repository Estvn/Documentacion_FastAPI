
- **Es importante validar los campos de los modelos hechos con pydantic.**
- Para añadir validaciones, importe la clase **Field** de pydantic.

```
from pydantic import Field
```

- Estos campos de validación se agregan en los modelos de datos.

He puesto una validación en el título (al menos 5 caracteres):

![[Pasted image 20250701080329.png]]

> [!NOTA]
> Las validaciones con pydantic incluso hacen validaciones a los datos que se retornar, es decir, a los datos almacenados.

```
from pydantic import BaseModel, Field, StringConstraints # Una clase de pydantic para crear modelos de datos
from typing import Optional, Annotated
# import datetime

class MoviePut(BaseModel):
    title: str = Field(min_length=5, max_length=15, default="Título random")
    overview: str = Field(min_length=15, max_length=50, default="Descripción random")
    rating: float = Field(ge=0, le=10, default = 10)
    categories: list[Annotated[str, StringConstraints(min_length=5, max_length=20)]]    
    year: str #= Field(le=datetime.date.today().year, ge=1900)
```












