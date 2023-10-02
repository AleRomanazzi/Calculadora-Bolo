from reactpy import component, html
from reactpy.backend.fastapi import configure
from fastapi import FastAPI

from components.navbar.boton_navbar import boton_navbar

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
        boton_navbar('CALCULAR', "./pantalla_input/input.py"),
        boton_navbar('Facundo', "https://www.linkedin.com/in/facundo-maidana-68a7b71b4/"),
        boton_navbar('Alejandro', "https://www.linkedin.com/in/alejandro-romanazzi/")
    )

app = FastAPI()
configure(app, ul_navbar)