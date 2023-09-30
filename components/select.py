from reactpy import component, html
from reactpy.backend.fastapi import configure
from fastapi import FastAPI
from mongoPython.conection import db, lacteos

# Componente principal que renderiza el resto


@component
def select():
    categories = ["Lácteos", "Azucarados", "Carnes", "Cereales",
                  "Frutas", "Grasas", "Huevo", "Misceláneos", "Pescados", "Vegetales"]
    list_categories = [html.option(text) for text in categories]
    return html.div(
        html.select(
            {
                "name": "select1"
            },
            list_categories
        ),
        html.select(
            html.option(i["Nombre"]) for i in lacteos.find({"Alimento": "Lácteos"}))
    )


def buscar():
    for i in lacteos.find({"Alimentos": "Lácteos"}):
        return html.option(i['Nombre'])


app = FastAPI()
configure(app, select)
