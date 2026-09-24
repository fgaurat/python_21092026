"""09 - Partager des données entre callbacks avec dcc.Store.

dcc.Store est un composant invisible qui conserve des données (JSON) côté
navigateur. Un callback l'écrit, d'autres le lisent : on évite ainsi de
recalculer ou de recharger les mêmes données plusieurs fois.

storage_type : "memory" (perdu au rechargement), "session" ou "local".
"""

import random

from dash import Dash, Input, Output, dcc, html

app = Dash(__name__)

app.layout = html.Div(style={"fontFamily": "sans-serif", "margin": "20px"}, children=[
    html.H1("Tirage aléatoire"),
    html.Button("Nouveau tirage", id="tirer"),
    dcc.Store(id="tirage", storage_type="memory"),
    html.P(id="valeurs"),
    html.P(id="stats"),
])


@app.callback(
    Output("tirage", "data"),
    Input("tirer", "n_clicks"),
)
def tirer(_):
    """Génère 10 nombres et les range dans le Store."""
    return [random.randint(1, 100) for _ in range(10)]


@app.callback(
    Output("valeurs", "children"),
    Input("tirage", "data"),
)
def afficher_valeurs(nombres):
    """Premier lecteur du Store : affiche les nombres."""
    return "Nombres : " + ", ".join(map(str, nombres))


@app.callback(
    Output("stats", "children"),
    Input("tirage", "data"),
)
def afficher_stats(nombres):
    """Second lecteur du Store : calcule quelques statistiques."""
    return f"Min : {min(nombres)} — Max : {max(nombres)} — Moyenne : {sum(nombres) / len(nombres):.1f}"


if __name__ == "__main__":
    app.run(debug=True)
