"""DTO (Data Transfer Object) représentant un client de la table customers_tbl."""

from dataclasses import dataclass
from typing import Optional


@dataclass
class CustomerDTO:
    """Conteneur de données pour un client.

    Ne contient aucune logique d'accès à la base : il sert uniquement à
    transporter les données entre le DAO et le reste du programme.

    Attributes:
        first_name: Prénom du client.
        last_name: Nom du client.
        email: Adresse e-mail.
        gender: Genre (ex. "Male", "Female").
        ip_address: Adresse IP du client.
        id: Identifiant en base. Vaut None tant que le client n'a pas été inséré.
    """

    first_name: str
    last_name: str
    email: str
    gender: str
    ip_address: str
    id: Optional[int] = None

    def __str__(self):
        """Retourne une représentation lisible : [id] Prénom Nom <email>."""
        return f"[{self.id}] {self.first_name} {self.last_name} <{self.email}>"
