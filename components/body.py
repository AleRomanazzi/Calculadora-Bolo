from reactpy import component, html, use_state
from reactpy.backend.fastapi import configure
from fastapi import FastAPI
from components.boton import boton
from components.input import input
from components.food_select_container import foodSelector
from components.label import label
from mongoPython.conection import db


@component
def body():
    formstate, set_formstate = use_state(dict())
    # *crear la funcion calcular, usando el estado formstate
    # print(formstate)

    def addFormState(name, value):
        prev_dict = formstate.copy()
        new_dict = dict()
        new_dict[name] = value
        prev_dict.update(new_dict)
        set_formstate(prev_dict)

    calculus, setCalculus = use_state(0)

    def calculate(e):
        glucosa = int(formstate['glucosa'])
        ratio = int(formstate['ratio'])
        factor = int(formstate['factor'])
        porciones = int(formstate['porciones'])
        nombre_alimento = formstate['alimentos']
        categoria = formstate['categoria']
        carb = db[categoria].find_one({"Nombre": nombre_alimento})
        carb = float(carb['Carbohidratos totales'])
        var = round(((carb*porciones)/ratio)+((glucosa/factor)-2))
        if var < 1  : var = 1 
        setCalculus(var)

    return html.div({
        "style": {
            "background-color": "#B5BAD0",
            "font-family": "consolas",
        },
    },
        html.div(
            {"style": {
                 "display": "flex",
                 "flex-direction": "column",
                 "justify-content": "center",
                 "align-items": "center",
             },
             },
            label("Nivel de glucosa:"),
            input(addFormState, "glucosa"),
            label("Ratio:"),
            input(addFormState, "ratio"),
            label("Factor:"),
            input(addFormState, "factor"),
            label("Cantidad de Porciones:"),
            input(addFormState, "porciones"),
            label("Categoría y Alimento:"),
            foodSelector(addFormState),
            boton("Calcular", calculate, calculus),
            html.span({
                "style":{
                    "font-size":"24px",
                    },
                    },
                    f"Te tienes que suministrar:{calculus} unidades"
                )
            )
    )


app = FastAPI()
configure(app, body)
