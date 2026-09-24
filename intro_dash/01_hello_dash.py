"""01 - Première application Dash : le strict minimum.

Une application Dash = un objet Dash + un layout (l'arbre des composants).
Lancement : uv run intro_dash/01_hello_dash.py  puis http://127.0.0.1:8050
"""

from dash import Dash, html

app = Dash(__name__)

# Le layout décrit la page : ici un titre et un paragraphe.
app.layout = html.Div([
    html.H1("Bonjour Dash !"),
    html.P("Ma première application web en Python."),
])

if __name__ == "__main__":
    app.run(debug=True)  # debug=True : rechargement automatique à chaque modification
