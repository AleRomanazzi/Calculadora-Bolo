from reactpy import component, html
from reactpy.backend.fastapi import configure
from fastapi import FastAPI


@component
def footer():
    return html.footer({
        "style": {
            "background-color": "#12486B",
            "color": "#fff",
            "padding": "50px 0",
            "text-align": "center",
            "font-family": "Arial",
        },
    },
        html.div(
            {
                "style": {"text-align": "center"},
                "class": "nombres",
            },
            html.p({"style": {
                "font-size": "16px",
                "margin": "5px 0",
            },
            },
                "Maidana Facundo, EISI884"),
            html.p({"style": {
                "font-size": "16px",
                "margin": "5px 0",
            },
            },
                "Romanazzi Alejandro, EISI806"),
    ),
        html.div(
            {
                "class": "copyright",
            }, "©Copyright; DiabCalc 2023. Todos los derechos reservados."
    ),

    )


app = FastAPI()
configure(app, footer)
