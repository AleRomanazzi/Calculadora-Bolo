from reactpy import component, html
from reactpy.backend.fastapi import configure
from fastapi import FastAPI


@component
def boton(texto):
    return html.input({
        "type": "submit",
        "value": texto,
        "style": {
            "padding": "1rem",
            "border-radius": "10%",
            "border": "1px solid white",
        }
    },
    )


app = FastAPI()
configure(app, boton)
