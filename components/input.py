from reactpy import component, html
from reactpy.backend.fastapi import configure
from fastapi import FastAPI


# Componente principal que renderiza el resto
@component
def input(cambiar, name):
    def handleChange(e):
        cambiar(name, e["currentTarget"]['value'])
        print(e["currentTarget"]['value'])
    return html.input({
        "on_change": handleChange,
        "type": "number",
        "name": name,
        "style": {
            "width": "200px",
            "height": "30px",
            "border": "1px solid black",
            "border-radius": "10px",
            "font-size": "24px",
            "padding": "0.3rem"
        },
    })


app = FastAPI()
configure(app, input)
