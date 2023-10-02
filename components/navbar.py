from reactpy import component, html
from reactpy.backend.fastapi import configure
from fastapi import FastAPI

from components.ul_navbar import ul_navbar

@component
def navbar():
    return html.div({
        "style": {
            "background-color": "#00796B",
            "color": "white",
            "display": "flex",
            "flex-direction": "column",
            "align-items": "center"                
    }
    },
        html.h1("CALCULADORA DE BOLO"),
        ul_navbar()
)

app = FastAPI()
configure(app, navbar)