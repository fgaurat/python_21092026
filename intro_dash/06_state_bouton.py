"""06 - Bouton et State : ne déclencher le calcul qu'au clic.

- Input  : un changement déclenche le callback (ici : le clic, via n_clicks)
- State  : la valeur est lue au moment de l'appel, sans déclencher le callback
- prevent_initial_call=True : pas d'appel au chargement de la page
- PreventUpdate : annule la mise à jour des sorties
"""

from dash import Dash, Input, Output, State, dcc, html
from dash.exceptions import PreventUpdate

app = Dash(__name__)

app.layout = html.Div(style={"fontFamily": "sans-serif", "margin": "20px"}, children=[
    html.H1("Liste de tâches"),
    dcc.Input(id="tache", type="text", placeholder="Nouvelle tâche"),
    html.Button("Ajouter", id="ajouter", n_clicks=0),
    html.Ul(id="liste", children=[]),
])


@app.callback(
    Output("liste", "children"),
    Output("tache", "value"),
    Input("ajouter", "n_clicks"),
    State("tache", "value"),
    State("liste", "children"),
    prevent_initial_call=True,
)
def ajouter_tache(n_clicks, tache, taches):
    """Ajoute la tâche saisie à la liste, puis vide la zone de texte."""
    if not tache:
        raise PreventUpdate  # rien à ajouter : on ne touche à rien
    return taches + [html.Li(tache)], ""


if __name__ == "__main__":
    app.run(debug=True)
