"""TP DataTable – correction (étapes 1 à 4)."""

from dash import Dash, Input, Output, dash_table, dcc, html

PRODUITS = [
    {"nom": "Clavier", "categorie": "Informatique", "prix": 49.90, "stock": 12},
    {"nom": "Souris", "categorie": "Informatique", "prix": 19.90, "stock": 30},
    {"nom": "Écran 27\"", "categorie": "Informatique", "prix": 249.00, "stock": 0},
    {"nom": "Stylo", "categorie": "Bureau", "prix": 1.50, "stock": 200},
    {"nom": "Cahier", "categorie": "Bureau", "prix": 3.20, "stock": 85},
    {"nom": "Agrafeuse", "categorie": "Bureau", "prix": 8.90, "stock": 0},
    {"nom": "Casque", "categorie": "Audio", "prix": 89.00, "stock": 7},
    {"nom": "Enceinte", "categorie": "Audio", "prix": 59.00, "stock": 4},
]

app = Dash(__name__)

app.layout = html.Div(style={"fontFamily": "sans-serif", "margin": "20px", "width": "600px"}, children=[
    html.H1("Catalogue produits"),

    # Étape 3 : liste déroulante des catégories
    dcc.Dropdown(id="categorie", options=["Toutes", "Informatique", "Bureau", "Audio"],
                 value="Toutes", clearable=False),

    # Étapes 1 et 2 : le tableau (data est fourni par le callback)
    dash_table.DataTable(
        id="table",
        columns=[
            {"name": "Nom", "id": "nom"},
            {"name": "Catégorie", "id": "categorie"},
            {"name": "Prix (€)", "id": "prix"},
            {"name": "Stock", "id": "stock"},
        ],
        sort_action="native",
        page_size=5,
        style_header={"fontWeight": "bold", "backgroundColor": "#eee"},
        style_data_conditional=[
            {"if": {"filter_query": "{stock} = 0"}, "color": "red"},
        ],
    ),

    # Étape 4 : résumé
    html.P(id="resume"),
])


@app.callback(
    Output("table", "data"),
    Output("resume", "children"),
    Input("categorie", "value"),
)
def filtrer(categorie):
    """Filtre les produits par catégorie et calcule la valeur du stock."""
    if categorie == "Toutes":
        produits = PRODUITS
    else:
        produits = [p for p in PRODUITS if p["categorie"] == categorie]

    valeur = sum(p["prix"] * p["stock"] for p in produits)
    return produits, f"{len(produits)} produit(s) — valeur du stock : {valeur:,.2f} €".replace(",", " ")


if __name__ == "__main__":
    app.run(debug=True)
