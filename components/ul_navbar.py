from reactpy import component, html
from reactpy.backend.fastapi import configure
from fastapi import FastAPI

from components.boton_navbar import boton_navbar

@component
def ul_navbar():
    return html.ul({
            "style":{
                "display":"flex",
                "flex-direction": "row",
                "align-self": "center",
                "justify-content": "center"
            }
        },
        boton_navbar('Inicio', "https://google.com"),
        boton_navbar('Calcular', "https://google.com"),
        boton_navbar('Creditos', "https://google.com")
    )

app = FastAPI()
configure(app, ul_navbar)