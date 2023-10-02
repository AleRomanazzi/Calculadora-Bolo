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
    return html.div(
        html.form({"method": "POST", "name": "sopa"},
                  input("number", "300px", addFormState, "glucosa"),
                  input("number", "300px", addFormState, "ratio"),
                  input("number", "300px", addFormState, "factor"),
                  input("number", "300px", addFormState, "porciones"),
                  foodSelector(addFormState),
                  boton("Calcular")
                  )
    )


app = FastAPI()
configure(app, body)
