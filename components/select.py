from reactpy import component, html


@component
def select(options, change, name):
    list_options = [html.option({
        "value": option["value"],
    }, option["label"]) for option in options]
    list_options.append(html.option(
        {"value": "", "selected": "true", "disabled": "true"}, "Selecciona un elemento"))

    def handleChange(e):
        change(name, e["currentTarget"]['value'])
    return html.select({
        "on_change": handleChange,
        "style": {
            "padding": "0.4rem",
            "font-size": "18px",
            "margin-top": "10px",
            "font-family": "verdana",
        },
    }, list_options)
