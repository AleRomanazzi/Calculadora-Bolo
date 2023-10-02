from reactpy import component, html, use_state
from components.select import select
from mongoPython.conection import db


@component
def foodSelector(change):
    foodlist, setFoodlist = use_state(
        [i["Nombre"] for i in db["Lácteos"].find({"Alimento": "Lácteos"})])

    def handleCategoryChange(_, value):
        new_index = value
        setFoodlist([i["Nombre"]
                    for i in db[new_index].find({"Alimento": new_index})])
    return html.div(
        select([{"value": label, "label": label} for index, label in enumerate(['Lácteos', 'Azucarados', 'Carnes', 'Cereales', 'Frutas', 'Grasas', 'Huevo', 'Misceláneos', 'Pescados', 'Vegetales'])],
               handleCategoryChange, "categories"),
        select([{"value": label, "label": label} for index, label in enumerate(foodlist)], change, "alimentos"))
