from reactpy import component, html
from reactpy.backend.fastapi import configure
from fastapi import FastAPI


@component
def boton(texto, calcular):
    return html.input({
        "type": "submit",
        "value": texto,
        "style": {
            "margin": "1rem 0",
            "color": "white",
            "border": "none",
            "padding": "1rem",
            "border-radius": "10%",
            "border": "1px solid white",
            "background-color": "#419197"
        },
        "on_click": calcular
    },
    )


app = FastAPI()
configure(app, boton)
