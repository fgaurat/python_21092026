"""DAO (Data Access Object) pour la table customers_tbl (SQLite).

Toute la logique SQL est regroupée ici : le reste du programme ne manipule
que des objets CustomerDTO et n'a jamais besoin de connaître la structure
de la base.
"""

import sqlite3
from typing import List, Optional

from customer_dto import CustomerDTO


class CustomerDAO:
    """Opérations CRUD sur la table customers_tbl.

    Chaque méthode ouvre sa propre connexion via un bloc ``with`` : la
    transaction est validée automatiquement en sortie de bloc, ou annulée
    en cas d'exception.

    Args:
        db_path: Chemin du fichier SQLite (par défaut ``customers_db.db``).
    """

    def __init__(self, db_path="customers_db.db"):
        self._db_path = db_path

    def _connect(self):
        """Ouvre une connexion SQLite avec accès aux colonnes par nom.

        Returns:
            sqlite3.Connection: Connexion dont les lignes sont des ``sqlite3.Row``.
        """
        conn = sqlite3.connect(self._db_path)
        conn.row_factory = sqlite3.Row  # accès aux colonnes par nom
        return conn

    @staticmethod
    def _row_to_dto(row) -> CustomerDTO:
        """Convertit une ligne SQL en CustomerDTO.

        Args:
            row: Ligne ``sqlite3.Row`` issue de customers_tbl.

        Returns:
            CustomerDTO: Le client correspondant à la ligne.
        """
        return CustomerDTO(
            id=row["id"],
            first_name=row["first_name"],
            last_name=row["last_name"],
            email=row["email"],
            gender=row["gender"],
            ip_address=row["ip_address"],
        )

    # CREATE
    def create(self, customer: CustomerDTO) -> CustomerDTO:
        """Insère un nouveau client en base.

        Args:
            customer: Client à insérer. Son attribut ``id`` est ignoré.

        Returns:
            CustomerDTO: Le même objet, avec ``id`` renseigné par la base.
        """
        sql = ("INSERT INTO customers_tbl(first_name, last_name, email, gender, ip_address)"
               " VALUES(?, ?, ?, ?, ?)")
        with self._connect() as conn:
            cur = conn.execute(sql, (
                customer.first_name,
                customer.last_name,
                customer.email,
                customer.gender,
                customer.ip_address,
            ))
            customer.id = cur.lastrowid
        return customer

    # READ
    def find_by_id(self, customer_id: int) -> Optional[CustomerDTO]:
        """Recherche un client par son identifiant.

        Args:
            customer_id: Identifiant (clé primaire) du client.

        Returns:
            CustomerDTO ou None si aucun client ne porte cet identifiant.
        """
        sql = "SELECT * FROM customers_tbl WHERE id = ?"
        with self._connect() as conn:
            row = conn.execute(sql, (customer_id,)).fetchone()
        return self._row_to_dto(row) if row else None

    def find_all(self) -> List[CustomerDTO]:
        """Retourne tous les clients, triés par identifiant croissant.

        Returns:
            list[CustomerDTO]: Liste éventuellement vide.
        """
        sql = "SELECT * FROM customers_tbl ORDER BY id"
        with self._connect() as conn:
            rows = conn.execute(sql).fetchall()
        return [self._row_to_dto(row) for row in rows]

    def find_by_last_name(self, last_name: str) -> List[CustomerDTO]:
        """Recherche les clients par nom de famille.

        La comparaison utilise ``LIKE`` : elle est insensible à la casse
        et accepte les jokers SQL ``%`` et ``_``.

        Args:
            last_name: Nom (ou motif) à rechercher, ex. ``"Dup%"``.

        Returns:
            list[CustomerDTO]: Clients correspondants, triés par identifiant.
        """
        sql = "SELECT * FROM customers_tbl WHERE last_name LIKE ? ORDER BY id"
        with self._connect() as conn:
            rows = conn.execute(sql, (last_name,)).fetchall()
        return [self._row_to_dto(row) for row in rows]

    # UPDATE
    def update(self, customer: CustomerDTO) -> bool:
        """Met à jour tous les champs d'un client existant.

        Args:
            customer: Client à mettre à jour. ``id`` doit être renseigné.

        Returns:
            bool: True si une ligne a été modifiée, False si l'id est inconnu.

        Raises:
            ValueError: Si ``customer.id`` vaut None.
        """
        if customer.id is None:
            raise ValueError("Impossible de mettre à jour un client sans id")
        sql = ("UPDATE customers_tbl"
               " SET first_name = ?, last_name = ?, email = ?, gender = ?, ip_address = ?"
               " WHERE id = ?")
        with self._connect() as conn:
            cur = conn.execute(sql, (
                customer.first_name,
                customer.last_name,
                customer.email,
                customer.gender,
                customer.ip_address,
                customer.id,
            ))
        return cur.rowcount == 1

    # DELETE
    def delete(self, customer_id: int) -> bool:
        """Supprime un client par son identifiant.

        Args:
            customer_id: Identifiant du client à supprimer.

        Returns:
            bool: True si une ligne a été supprimée, False si l'id est inconnu.
        """
        sql = "DELETE FROM customers_tbl WHERE id = ?"
        with self._connect() as conn:
            cur = conn.execute(sql, (customer_id,))
        return cur.rowcount == 1

    def count(self) -> int:
        """Retourne le nombre total de clients en base.

        Returns:
            int: Nombre de lignes dans customers_tbl.
        """
        with self._connect() as conn:
            return conn.execute("SELECT COUNT(*) FROM customers_tbl").fetchone()[0]
