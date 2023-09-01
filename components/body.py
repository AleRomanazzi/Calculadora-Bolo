from reactpy import component, html
from reactpy.backend.fastapi import configure
from fastapi import FastAPI

from components.card import card
from components.imagen import imagen
from components.boton import boton

@component
def body():
    return html.div(
        card("#F9A825",
        'Calculadora Bolo',
              'lorem12',
                "https://imgs.search.brave.com/-fPOuEW6WdDGQVUSd1CPce6VllnYFDj8B2ndQqzHtg4/rs:fit:860:0:0/g:ce/aHR0cHM6Ly9wNC53/YWxscGFwZXJiZXR0/ZXIuY29tL3dhbGxw/YXBlci81NzIvNTE1/LzcxNy9jYWxjdWxh/dGUtY2FsY3VsYXRv/ci1jbGFzcy1sZWFy/bmluZy13YWxscGFw/ZXItcHJldmlldy5q/cGc",
                "white",
                "#00796B",
                "Probar",
                "flex",
                "column",
                "center",
                "center",
                ),
        card("#333333",
        'About us', 
             'Calculadora Bolo is an innovative input calculator business based in La Rioja, Argentina. We specialize in providing accurate and efficient solutions for all your calculation needs. With our user-friendly interface and advanced algorithms, we make complex calculations simple and hassle-free. Whether you are a professional or a student, our calculators are designed to help you save time and improve accuracy. Trust Calculadora Bolo to deliver reliable and precise results every time.', 
             'https://imgs.search.brave.com/4XA4vMboKmFHOa9v5hFs7x37Eht2AQQgBzCzhWn652w/rs:fit:860:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5pc3RvY2twaG90/by5jb20vaWQvMTA5/MTg1ODQ1MC9waG90/by9jb250YWN0LXVz/LXNpZ24tb24tYS13/b29kZW4tZGVzay5q/cGc_cz02MTJ4NjEy/Jnc9MCZrPTIwJmM9/RmY0ZW5JRlIyV0Mw/UUNhX0NTQjBSSEhh/TkpJLXQ2NFBhNlhC/dU5kZnV4ND0',
             "white",
             "blue",
             "Contactar",
             "flex",
            "column",
            "center",
            "center"
             )
        )


app = FastAPI()
configure(app, body)