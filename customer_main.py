"""Démonstration du cycle CRUD complet avec CustomerDAO et CustomerDTO."""

from customer_dao import CustomerDAO
from customer_dto import CustomerDTO


def main():
    """Enchaîne lecture, création, mise à jour et suppression d'un client."""
    dao = CustomerDAO("customers_db.db")

    print("Nombre de clients :", dao.count())

    # READ
    print(dao.find_by_id(1))
    for c in dao.find_all()[:3]:
        print(c)

    # CREATE
    nouveau = CustomerDTO("Jean", "Dupont", "jean@dupont.fr", "Male", "10.0.0.1")
    nouveau = dao.create(nouveau)
    print("Créé :", nouveau)

    # UPDATE
    nouveau.email = "jean.dupont@example.com"
    print("Mis à jour :", dao.update(nouveau), dao.find_by_id(nouveau.id))

    # DELETE
    print("Supprimé :", dao.delete(nouveau.id), dao.find_by_id(nouveau.id))


if __name__ == '__main__':
    main()
