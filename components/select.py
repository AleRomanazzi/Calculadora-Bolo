from reactpy import component, html, event

# options = [{label:value}]


@component
def select(options, change, name):
    list_options = [html.option({
        "value": option["value"],
        }, 
        option["label"]) for option in options]
    
    def handleChange(e):
        print(e)
        change(name, e["currentTarget"]['value'])
    return html.select({
        "on_change": handleChange,
        "style":{
            "padding":"0.4rem",
            "font-size": "18px",
            "margin-top": "10px",
        },
        }, list_options)
