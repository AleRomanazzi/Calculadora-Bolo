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

    # * capta el conjunto de datos de control en un diccionario (función principal)
    def addFormState(name, value):
        prev_dict = formstate.copy()
        new_dict = dict()
        new_dict[name] = value
        prev_dict.update(new_dict)
        set_formstate(prev_dict)

    # crear el estado que almacenará el cálculo
    calculus, setCalculus = use_state("")

    # captar la coleccion de datos del estado actual 1 por 1,
    # obtener carbohidratos por nombre y calcular
    def calculate(e):
        glucosa = int(formstate['glucosa'])
        ratio = int(formstate['ratio'])
        factor = int(formstate['factor'])
        porciones = int(formstate['porciones'])
        nombre_alimento = formstate['alimentos']
        categoria = formstate['categoria']
        carb = db[categoria].find_one({"Nombre": nombre_alimento})
        carb = float(carb['Carbohidratos totales'])
        var = round(((carb*porciones)/ratio)+((glucosa - 150)/factor))
        texto = "unidades"
        if var < 1:
            var = 1
            texto = "unidad"
        
        setCalculus(f"Te tienes que suministrar: {var} {texto}")

    # * mostrar el cuerpo de la función
    return html.div({
        "style": {
            "background-color": "#78D6C6",
            "font-family": "verdana",
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
            label("Factor de sensibilidad de insulina:"),
            input(addFormState, "factor"),
            label("Cantidad de Porciones:"),
            input(addFormState, "porciones"),
            label("Categoría y Alimento:"),
            foodSelector(addFormState),
            boton("Calcular", calculate),
            html.div({"style": {"font-size": "24px"
                                ,"margin": "1rem 0 2rem 0" }, }, calculus)
    )
    )


app = FastAPI()
configure(app, body)
