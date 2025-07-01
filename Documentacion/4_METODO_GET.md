
- Los métodos GET pueden enviar cualquier tipo de respuesta (JSON, String, HTML, Arrays, etc.).

Para enviar HTML desde un Endpoint tiene que usar esta librería

```
from fastapi.responses import HTMLResponse
```

```
return HTMLResponse('<h1>Hola mundo</h1>')
```

