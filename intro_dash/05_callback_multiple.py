"""05 - Plusieurs entrées et plusieurs sorties.

Les arguments de la fonction arrivent dans l'ordre des Input,
les valeurs retournées (tuple) vont dans l'ordre des Output.
"""

from dash import Dash, Input, Output, dcc, html

app = Dash(__name__)

app.layout = html.Div(style={"fontFamily": "sans-serif", "margin": "20px", "width": "400px"}, children=[
    html.H1("Calcul d'IMC"),
    html.Label("Poids (kg)"),
    dcc.Slider(id="poids", min=40, max=150, step=1, value=70,
               marks={i: str(i) for i in range(40, 151, 20)}),
    html.Label("Taille (cm)"),
    dcc.Slider(id="taille", min=140, max=210, step=1, value=175,
               marks={i: str(i) for i in range(140, 211, 10)}),
    html.H2(id="imc"),
    html.P(id="categorie"),
])


@app.callback(
    Output("imc", "children"),
    Output("categorie", "children"),
    Output("categorie", "style"),  # une sortie peut aussi être le style d'un composant
    Input("poids", "value"),
    Input("taille", "value"),
)
def calculer_imc(poids, taille):
    """Recalcule l'IMC dès que l'un des deux curseurs bouge."""
    imc = poids / (taille / 100) ** 2
    if imc < 18.5:
        categorie, couleur = "Insuffisance pondérale", "orange"
    elif imc < 25:
        categorie, couleur = "Corpulence normale", "green"
    else:
        categorie, couleur = "Surpoids", "red"
    return f"IMC : {imc:.1f}", categorie, {"color": couleur, "fontWeight": "bold"}


if __name__ == "__main__":
    app.run(debug=True)
