from reactpy import component, html, event
from reactpy.backend.fastapi import configure
from reactpy import use_state
from fastapi import FastAPI
from mongoPython.conection import db, lacteos

# Componente principal que renderiza el resto


@component
def select(cambiar):
    categories = ['Lácteos', 'Azucarados', 'Carnes', 'Cereales',
                  'Frutas', 'Grasas', 'Huevo', 'Misceláneos', 'Pescados', 'Vegetales']

    list_categories = [html.option({"value": text}, text)
                       for text in categories]

    chosed, set_chosed = use_state(categories[0])

    def handleChange(e):
        print(e)
        cambiar(e["target"]["name"], e["currentTarget"]['value'])

    return html.div(
        html.select(
            {"id": "categories",
             "on_change": handleChange},
            list_categories
        ),
        html.select(
            html.option(i["Nombre"]) for i in db[chosed].find({"Alimento": chosed}))
    )


def buscar():
    for i in lacteos.find({"Alimentos": "Lácteos"}):
        return html.option(i['Nombre'])


app = FastAPI()
configure(app, select)
