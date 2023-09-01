from reactpy import component, html
from reactpy.backend.fastapi import configure
from fastapi import FastAPI

@component
def boton(colorTexto, colorFondo, texto):
    return html.input({
         "type": "submit",
         "value": texto,
         "style": {
             "color": colorTexto,
             "background-color": colorFondo,
             "padding": "1rem",
             "border-radius": "15%",
             "border": "1px solid white"
         }
         }, 
    )

app = FastAPI()
configure(app, boton)