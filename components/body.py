from reactpy import component, html, use_state
from reactpy.backend.fastapi import configure
from fastapi import FastAPI

from components.card import card
from components.imagen import imagen
from components.boton import boton
from components.input import input
from components.select import select
from components.footer import footer
from components.food_select_container import foodSelector
from components.label import label

@component
def body():
    formstate, set_formstate = use_state(dict())
    # *crear la funcion calcular, usando el estado formstate

    def addFormState(name, value):
        prev_dict = formstate.copy()
        new_dict = dict()
        new_dict[name] = value
        prev_dict.update(new_dict)
        set_formstate(prev_dict)

    print(formstate)

    #Implementar lista y ciclo for para generar labels e inputs para mejora de codigo
    lista = ["glucosa", "ratio", "factor", "porciones"]
    return html.div({
        "style":{
            "background-color": "#0093E9",
            "background-image": "linear-gradient(160deg, #0093E9 0%, #80D0C7 100%)"
            },
            },
        html.form(
            {"method": "POST", 
             "name": "sopa",
             "style": {
                 "display": "flex",
                 "flex-direction": "column",
                 "justify-content": "center",
                 "align-items": "center",
             },
             },
                  label("Nivel de glucosa:"),                
                  input("number", addFormState, "glucosa"),
                  label("Ratio:"),
                  input("number", addFormState, "ratio"),
                  label("Factor:"),
                  input("number", addFormState, "factor"),
                  label("Cantidad de Porciones:"),
                  input("number", addFormState, "porciones"),
                  label("Categoria y Alimento:"),
                  foodSelector(addFormState),
                  boton("Calcular")
                  )
    )


app = FastAPI()
configure(app, body)
