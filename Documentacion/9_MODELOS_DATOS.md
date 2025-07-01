
# Creación de Esquemas o Modelos

- **Una de las principales características de FastAPI es la creación de los esquemas o modelos.**
- FastAPI se ayuda de una librería que ya viene integrada en la instalación.

- Esta librería se llama **Pydantic**
- **Es una librería que se encarga con todo lo relacionado con los datos y el tema de las validaciones.**

- En nuestros métodos tenemos que poner en los parámetros de las funciones de POST y PUT, todos los datos relacionados con una película.
- Agregar todos los datos en los parámetros de una función no es lo adecuado, ya que resultaría tedioso agregar 150 parámetros, si se requieren.

- **En casos como el ejemplo anterior es donde se pueden usar modelos de Pydantic.**
- 