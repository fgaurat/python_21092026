"""Tests unitaires du DAO et du DTO client.

Les tests s'exécutent sur une base SQLite temporaire, créée avant chaque
test et supprimée après : la base de production customers_db.db n'est
jamais modifiée.

Lancement :
    python3 -m unittest test_customer_dao -v
"""

import os
import sqlite3
import tempfile
import unittest

from customer_dao import CustomerDAO
from customer_dto import CustomerDTO

SCHEMA = """
CREATE TABLE IF NOT EXISTS "customers_tbl" (
    "id"         INTEGER,
    "first_name" TEXT,
    "last_name"  TEXT,
    "email"      TEXT,
    "gender"     TEXT,
    "ip_address" TEXT,
    PRIMARY KEY("id" AUTOINCREMENT)
);
"""


class CustomerDTOTest(unittest.TestCase):
    """Vérifie le comportement du DTO."""

    def test_id_est_none_par_defaut(self):
        """Un client non encore inséré n'a pas d'identifiant."""
        client = CustomerDTO("Jean", "Dupont", "jean@dupont.fr", "Male", "10.0.0.1")
        self.assertIsNone(client.id)

    def test_str(self):
        """__str__ affiche l'id, le nom complet et l'e-mail."""
        client = CustomerDTO("Jean", "Dupont", "jean@dupont.fr", "Male", "10.0.0.1", id=7)
        self.assertEqual(str(client), "[7] Jean Dupont <jean@dupont.fr>")

    def test_egalite(self):
        """La dataclass compare les clients champ par champ."""
        a = CustomerDTO("Jean", "Dupont", "jean@dupont.fr", "Male", "10.0.0.1", id=1)
        b = CustomerDTO("Jean", "Dupont", "jean@dupont.fr", "Male", "10.0.0.1", id=1)
        c = CustomerDTO("Paul", "Dupont", "paul@dupont.fr", "Male", "10.0.0.2", id=2)
        self.assertEqual(a, b)
        self.assertNotEqual(a, c)


class CustomerDAOTest(unittest.TestCase):
    """Vérifie les opérations CRUD du DAO sur une base temporaire."""

    def setUp(self):
        """Crée une base vide et insère deux clients de référence."""
        fd, self.db_path = tempfile.mkstemp(suffix=".db")
        os.close(fd)
        with sqlite3.connect(self.db_path) as conn:
            conn.executescript(SCHEMA)

        self.dao = CustomerDAO(self.db_path)
        self.jean = self.dao.create(
            CustomerDTO("Jean", "Dupont", "jean@dupont.fr", "Male", "10.0.0.1"))
        self.marie = self.dao.create(
            CustomerDTO("Marie", "Martin", "marie@martin.fr", "Female", "10.0.0.2"))

    def tearDown(self):
        """Supprime le fichier de base temporaire."""
        os.remove(self.db_path)

    # CREATE
    def test_create_renseigne_id(self):
        """create() affecte l'identifiant généré par la base."""
        client = self.dao.create(
            CustomerDTO("Paul", "Durand", "paul@durand.fr", "Male", "10.0.0.3"))
        self.assertIsNotNone(client.id)
        self.assertEqual(self.dao.count(), 3)

    def test_create_persiste_les_donnees(self):
        """Le client relu en base a les mêmes valeurs que celui inséré."""
        relu = self.dao.find_by_id(self.jean.id)
        self.assertEqual(relu, self.jean)

    # READ
    def test_find_by_id_existant(self):
        """find_by_id() retourne le bon client."""
        self.assertEqual(self.dao.find_by_id(self.marie.id).email, "marie@martin.fr")

    def test_find_by_id_inconnu(self):
        """find_by_id() retourne None pour un identifiant inconnu."""
        self.assertIsNone(self.dao.find_by_id(9999))

    def test_find_all(self):
        """find_all() retourne tous les clients triés par identifiant."""
        clients = self.dao.find_all()
        self.assertEqual([c.id for c in clients], [self.jean.id, self.marie.id])

    def test_find_all_base_vide(self):
        """find_all() retourne une liste vide si la base ne contient rien."""
        self.dao.delete(self.jean.id)
        self.dao.delete(self.marie.id)
        self.assertEqual(self.dao.find_all(), [])

    def test_find_by_last_name(self):
        """find_by_last_name() filtre sur le nom de famille."""
        trouves = self.dao.find_by_last_name("Dupont")
        self.assertEqual(len(trouves), 1)
        self.assertEqual(trouves[0].first_name, "Jean")

    def test_find_by_last_name_avec_joker(self):
        """find_by_last_name() accepte les jokers SQL."""
        self.assertEqual(len(self.dao.find_by_last_name("M%")), 1)

    def test_find_by_last_name_sans_resultat(self):
        """find_by_last_name() retourne une liste vide si rien ne correspond."""
        self.assertEqual(self.dao.find_by_last_name("Inconnu"), [])

    # UPDATE
    def test_update_modifie_la_base(self):
        """update() enregistre les nouvelles valeurs."""
        self.jean.email = "nouveau@dupont.fr"
        self.assertTrue(self.dao.update(self.jean))
        self.assertEqual(self.dao.find_by_id(self.jean.id).email, "nouveau@dupont.fr")

    def test_update_id_inconnu(self):
        """update() retourne False si aucune ligne ne correspond."""
        fantome = CustomerDTO("X", "Y", "x@y.fr", "Male", "10.0.0.9", id=9999)
        self.assertFalse(self.dao.update(fantome))

    def test_update_sans_id(self):
        """update() lève ValueError si le client n'a pas d'identifiant."""
        with self.assertRaises(ValueError):
            self.dao.update(CustomerDTO("X", "Y", "x@y.fr", "Male", "10.0.0.9"))

    # DELETE
    def test_delete(self):
        """delete() supprime la ligne correspondante."""
        self.assertTrue(self.dao.delete(self.jean.id))
        self.assertIsNone(self.dao.find_by_id(self.jean.id))
        self.assertEqual(self.dao.count(), 1)

    def test_delete_id_inconnu(self):
        """delete() retourne False si l'identifiant n'existe pas."""
        self.assertFalse(self.dao.delete(9999))
        self.assertEqual(self.dao.count(), 2)

    # COUNT
    def test_count(self):
        """count() retourne le nombre de clients en base."""
        self.assertEqual(self.dao.count(), 2)


if __name__ == '__main__':
    unittest.main()
