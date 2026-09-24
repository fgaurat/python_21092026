"""10 - Afficher les clients de la base avec dash_table.DataTable.

On réutilise le DAO du projet : l'application ne contient aucun SQL.
DataTable attend une liste de dict -> dataclasses.asdict convertit les DTO.
Étape suivante : voir customer_dash_app.py pour le CRUD complet.
"""

import sys
from dataclasses import asdict
from pathlib import Path

from dash import Dash, Input, Output, dash_table, dcc, html

# Permet d'importer customer_dao depuis le dossier parent
PROJET = Path(__file__).resolve().parent.parent
sys.path.append(str(PROJET))
from customer_dao import CustomerDAO  # noqa: E402

dao = CustomerDAO(PROJET / "customers_db.db")

app = Dash(__name__)

app.layout = html.Div(style={"fontFamily": "sans-serif", "margin": "20px"}, children=[
    html.H1("Clients"),
    dcc.Input(id="recherche", type="text", placeholder="Filtrer par nom…", debounce=True),
    html.P(id="nombre"),
    dash_table.DataTable(
        id="table",
        columns=[{"name": c, "id": c} for c in ["id", "first_name", "last_name", "email", "gender"]],
        page_size=10,
        sort_action="native",
        style_cell={"textAlign": "left"},
    ),
])


@app.callback(
    Output("table", "data"),
    Output("nombre", "children"),
    Input("recherche", "value"),
)
def filtrer(recherche):
    """Recharge les clients depuis la base, filtrés par nom si besoin."""
    clients = dao.find_by_last_name(f"%{recherche}%") if recherche else dao.find_all()
    return [asdict(c) for c in clients], f"{len(clients)} client(s)"


if __name__ == "__main__":
    app.run(debug=True)
