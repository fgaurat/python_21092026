"""07 - Afficher un graphique Plotly avec dcc.Graph.

La propriété 'figure' de dcc.Graph reçoit une figure Plotly :
un callback peut donc reconstruire le graphique à chaque interaction.
"""

import plotly.graph_objects as go
from dash import Dash, Input, Output, dcc, html

MOIS = ["Jan", "Fév", "Mar", "Avr", "Mai", "Juin"]
VENTES = {
    "Paris": [120, 135, 150, 145, 170, 190],
    "Lyon": [80, 95, 90, 110, 120, 125],
    "Marseille": [60, 70, 85, 80, 95, 105],
}

app = Dash(__name__)

app.layout = html.Div(style={"fontFamily": "sans-serif", "margin": "20px"}, children=[
    html.H1("Ventes par ville"),
    dcc.Checklist(id="villes", options=list(VENTES), value=["Paris"], inline=True),
    dcc.RadioItems(id="type", options=["Lignes", "Barres"], value="Lignes", inline=True),
    dcc.Graph(id="graphique"),
])


@app.callback(
    Output("graphique", "figure"),
    Input("villes", "value"),
    Input("type", "value"),
)
def mettre_a_jour_graphique(villes, type_graphique):
    """Construit une trace par ville cochée."""
    fig = go.Figure()
    for ville in villes:
        if type_graphique == "Lignes":
            fig.add_trace(go.Scatter(x=MOIS, y=VENTES[ville], name=ville, mode="lines+markers"))
        else:
            fig.add_trace(go.Bar(x=MOIS, y=VENTES[ville], name=ville))
    fig.update_layout(title="Ventes mensuelles", yaxis_title="Ventes (k€)")
    return fig


if __name__ == "__main__":
    app.run(debug=True)
