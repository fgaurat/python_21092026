"""04 - Premier callback : relier une entrée à une sortie.

Un callback est une fonction Python appelée automatiquement par Dash
chaque fois qu'une propriété d'Input change. Sa valeur de retour est
écrite dans la propriété d'Output.

    Input("id-composant", "propriété")  ->  fonction  ->  Output("id-composant", "propriété")
"""

from dash import Dash, Input, Output, dcc, html

app = Dash(__name__)

app.layout = html.Div(style={"fontFamily": "sans-serif", "margin": "20px"}, children=[
    html.H1("Callback simple"),
    dcc.Input(id="nom", type="text", value="le monde"),
    html.H2(id="salutation"),
])


@app.callback(
    Output("salutation", "children"),
    Input("nom", "value"),
)
def saluer(nom):
    """Appelée à chaque frappe dans la zone de texte (et au chargement de la page)."""
    return f"Bonjour {nom} !"


if __name__ == "__main__":
    app.run(debug=True)
