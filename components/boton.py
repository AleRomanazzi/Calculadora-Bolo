from reactpy import component, html
from reactpy.backend.fastapi import configure
from fastapi import FastAPI


@component
def boton(texto):
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
            "background-image": "linear-gradient(to top, #a18cd1 0%, #fbc2eb 100%)"
        }
    },
    )


app = FastAPI()
configure(app, boton)
