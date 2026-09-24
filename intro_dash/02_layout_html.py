"""02 - Construire une page avec les composants html.

Chaque balise HTML a son équivalent : html.Div, html.H1, html.Ul, html.A...
- children : le contenu (texte, composant ou liste de composants)
- style    : un dict de propriétés CSS en camelCase (backgroundColor, fontSize...)
"""

from dash import Dash, html

app = Dash(__name__)

carte_style = {
    "border": "1px solid #ccc",
    "borderRadius": "8px",
    "padding": "16px",
    "width": "200px",
}

app.layout = html.Div(style={"fontFamily": "sans-serif", "margin": "20px"}, children=[
    html.H1("Mise en page", style={"color": "#4C78A8"}),

    html.H2("Une liste"),
    html.Ul([html.Li("Python"), html.Li("Dash"), html.Li("Plotly")]),

    html.H2("Des cartes côte à côte (flexbox)"),
    html.Div(style={"display": "flex", "gap": "16px"}, children=[
        html.Div([html.H3("Clients"), html.P("1001")], style=carte_style),
        html.Div([html.H3("Commandes"), html.P("4520")], style=carte_style),
        html.Div([html.H3("Produits"), html.P("87")], style=carte_style),
    ]),

    html.Hr(),
    html.A("Documentation Dash", href="https://dash.plotly.com", target="_blank"),
])

if __name__ == "__main__":
    app.run(debug=True)
