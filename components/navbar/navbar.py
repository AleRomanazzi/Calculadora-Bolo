from reactpy import component, html
from reactpy.backend.fastapi import configure
from fastapi import FastAPI

from components.navbar.ul_navbar import ul_navbar


@component
def navbar():
    return html.div({
        "style": {
            "background-color": "#7389AE",
            "color": "white",
            "display": "flex",
            "flex-direction": "column",
            "align-items": "center",
            "font-family": "consolas"
        }
    },
        html.h1("CALCULADORA DE BOLO"),
        ul_navbar()
    )


app = FastAPI()
configure(app, navbar)
