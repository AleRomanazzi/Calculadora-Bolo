from reactpy import component, html
from reactpy.backend.fastapi import configure
from fastapi import FastAPI

from components.body import body
from components.navbar import navbar

#Componente principal que renderiza el resto
@component
def main():
    return html.div(
        navbar(),
        body(),
    )


app = FastAPI()
configure(app, main)