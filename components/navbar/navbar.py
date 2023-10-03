from reactpy import component, html
from reactpy.backend.fastapi import configure
from fastapi import FastAPI

from components.navbar.ul_navbar import ul_navbar


@component
def navbar():
    return html.div({
        "style": {
            "background-color": "#419197",
            "color": "white",
            "display": "flex",
            "flex-direction": "column",
            "align-items": "center",
            "font-family": "consolas"
        }
    },
        html.h1({"style":{"color": "#F5FCCD"},},"DIABCALC"),
        html.p({"style": {"margin-top": "2px", "color": "#F5FCCD"},}, "CALCULADORA DE INSULINA"),
        ul_navbar()
    )


app = FastAPI()
configure(app, navbar)
