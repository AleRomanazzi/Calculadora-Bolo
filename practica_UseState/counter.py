# import reactpy
# import asyncio
# import requests

# async def getPage(pagina):
#     response = await requests.get(
#         f"https://pokeapi.co/api/v2/pokemon?offset=${pagina}&limit=10")
#     data = await response.json()

# @reactpy.component
# def state():
#     initial_state = 0
#     listaPokemons, setListaPokemons = reactpy.hooks.use_state([])
#     pagina, setPagina = reactpy.hooks.use_state(initial_state)

import reactpy


def increment(last_count):
    return last_count + 1


def decrement(last_count):
    return last_count - 1


@reactpy.component
def counter():
    initial_count = 0
    count, set_count = reactpy.hooks.use_state(initial_count)
    return reactpy.html.div(
        f"Count: {count}",
        reactpy.html.button(
            {"on_click": lambda event: set_count(initial_count)}, "Reset"
        ),
        reactpy.html.button(
            {"on_click": lambda event: set_count(increment)}, "+"),
        reactpy.html.button(
            {"on_click": lambda event: set_count(decrement)}, "-"),
    )


reactpy.run(counter)
