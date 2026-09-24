"""08 - Plusieurs boutons dans un seul callback avec ctx.triggered_id.

Une même propriété de sortie ne peut être écrite que par un seul callback.
Quand plusieurs boutons modifient la même chose, on les met tous en Input
et on regarde lequel a déclenché l'appel avec ctx.triggered_id.
"""

from dash import Dash, Input, Output, State, ctx, html

app = Dash(__name__)

app.layout = html.Div(style={"fontFamily": "sans-serif", "margin": "20px"}, children=[
    html.H1("Compteur"),
    html.H2(id="valeur", children="0"),
    html.Button("-1", id="moins"),
    html.Button("+1", id="plus"),
    html.Button("Remise à zéro", id="reset"),
])


@app.callback(
    Output("valeur", "children"),
    Input("moins", "n_clicks"),
    Input("plus", "n_clicks"),
    Input("reset", "n_clicks"),
    State("valeur", "children"),
    prevent_initial_call=True,
)
def compter(_moins, _plus, _reset, valeur):
    """Modifie le compteur selon le bouton cliqué."""
    valeur = int(valeur)
    if ctx.triggered_id == "plus":
        valeur += 1
    elif ctx.triggered_id == "moins":
        valeur -= 1
    else:
        valeur = 0
    return str(valeur)


if __name__ == "__main__":
    app.run(debug=True)
