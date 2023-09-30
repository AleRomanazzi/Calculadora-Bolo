from reactpy import component, html
from reactpy.backend.fastapi import configure
from fastapi import FastAPI
from mongoPython.conection import db, lacteos

# Componente principal que renderiza el resto


@component
def select():
    return html.div(
        html.select(
            {
                "name": "select1"
            },
            html.option("Lácteos"),
            html.option("Azucarados"),
            html.option("Carnes"),
            html.option("Cereales"),
            html.option("Frutas"),
            html.option("Grasas"),
            html.option("Huevo"),
            html.option("Misceláneos"),
            html.option("Pescados"),
            html.option("Vegetales")
        ),
        html.select(
            html.option(i["Nombre"]) for i in lacteos.find({"Alimento": "Lácteos"}))
    )


def buscar():
    for i in lacteos.find({"Alimentos": "Lácteos"}):
        return html.option(i['Nombre'])


app = FastAPI()
configure(app, select)
