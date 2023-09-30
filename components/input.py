from reactpy import component, html
from reactpy.backend.fastapi import configure
from fastapi import FastAPI


#Componente principal que renderiza el resto
@component
def input(tipoInput,ancho):
    return html.div(
        html.input({
            "type": tipoInput,
            "style":{
                "width":ancho,
                "height":"50px",
                "border":"1px solid black",
                "border-radius":"2px",
                "font-size":"32px",
            }
        })
    )


app = FastAPI()
configure(app, input)