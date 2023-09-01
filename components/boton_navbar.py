from reactpy import component, html
from reactpy.backend.fastapi import configure
from fastapi import FastAPI


@component
def boton_navbar(boton, direccion):
    return html.a({"href": direccion,
                   "style":{
                    "text-decoration": "none",
                    "color": "white" 
              }},
        html.li({
                "style":{
                    "padding":"1rem",
                    "list-style": "none"
                }
            },{boton})
            ) 

app = FastAPI()
configure(app, boton_navbar)