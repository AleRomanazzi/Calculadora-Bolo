from reactpy import component, html
from reactpy.backend.fastapi import configure
from fastapi import FastAPI


@component
def label(texto):
    return html.label(
        {"style": {
            "margin-top": "20px",
            "margin-bottom": "5px",
            "font-size": "18px"
            },
            },texto)

app = FastAPI()
configure(app, label)
