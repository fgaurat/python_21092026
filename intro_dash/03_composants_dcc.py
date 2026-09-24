"""03 - Les composants interactifs du module dcc (Dash Core Components).

Ils affichent des contrôles de saisie. Pour l'instant ils ne font rien :
on les connectera à du code Python avec les callbacks (exemple 04).
"""

from dash import Dash, dcc, html

app = Dash(__name__)

app.layout = html.Div(style={"fontFamily": "sans-serif", "margin": "20px", "width": "400px"}, children=[
    html.H1("Composants dcc"),

    html.Label("Zone de texte"),
    dcc.Input(id="texte", type="text", placeholder="Votre nom"),

    html.Label("Liste déroulante"),
    dcc.Dropdown(id="ville", options=["Paris", "Lyon", "Marseille"], value="Paris"),

    html.Label("Liste déroulante à choix multiples"),
    dcc.Dropdown(id="langages", options=["Python", "Java", "C#", "JavaScript"],
                 value=["Python"], multi=True),

    html.Label("Boutons radio"),
    dcc.RadioItems(id="niveau", options=["Débutant", "Intermédiaire", "Expert"], value="Débutant"),

    html.Label("Cases à cocher"),
    dcc.Checklist(id="options", options=["Newsletter", "Notifications"], value=[]),

    html.Label("Curseur"),
    dcc.Slider(id="age", min=0, max=100, step=5, value=30),

    html.Label("Date"),
    dcc.DatePickerSingle(id="date"),
])

if __name__ == "__main__":
    app.run(debug=True)
