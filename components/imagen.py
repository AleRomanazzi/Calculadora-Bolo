from reactpy import component, html
from reactpy.backend.fastapi import configure
from fastapi import FastAPI

@component
def imagen(src):
    return html.img({
            "src": src,
            "style": {
                "width": "100%",
                "transparency": "0.8"
                },
        }
    )

app = FastAPI()
configure(app, imagen)