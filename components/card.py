from reactpy import component, html
from reactpy.backend.fastapi import configure
from fastapi import FastAPI

from components.imagen import imagen
from components.boton import boton

@component
def card(fondoBackground, titulo, texto, img, colorBoton, fondoBoton, textoBoton, display, flexDirection, justify, align):
    return html.div(
        {"style":{"background-color": fondoBackground,
                  "display": display,
                  "flex-direction": flexDirection,
                  "justify-content": justify,
                  "align-items": align
                  }}, 
        html.h2(titulo),
        html.p(texto),
        imagen(img),
        boton(colorBoton, fondoBoton, textoBoton)
        #aca va el boton (crear componente)
    )

app = FastAPI()
configure(app, card)