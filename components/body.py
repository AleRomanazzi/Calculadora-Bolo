from reactpy import component, html
from reactpy.backend.fastapi import configure
from fastapi import FastAPI

from components.card import card
from components.imagen import imagen
from components.boton import boton
from components.input import input
from components.select import select
from components.footer import footer

@component
def body():
    return html.div(
        input("select","300px"),
        input("number","300px"),
        input("number","300px"),
        input("number","300px"),
        input("number","300px"),
        select(),
        boton("Calcular")
        )


app = FastAPI()
configure(app, body)