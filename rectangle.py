
from calc_geo import CalcGeo
class Rectangle(CalcGeo):

    # Constructeur
    def __init__(self, longueur, largeur):
        if longueur > 0 and largeur > 0:
            self._longueur = longueur
            self._largeur = largeur
        else:
            self._longueur = 0
            self._largeur = 0

    def get_longueur(self):
        """ return valeur de la longueur"""
        return self._longueur

    def set_longueur(self, longueur):
        """ init valeur de la longueur"""
        if longueur > 0:
            self._longueur = longueur

    def get_largeur(self):
        """ return valeur de la largeur"""
        return self._largeur

    def set_largeur(self, largeur):
        """ init valeur de la largeur"""
        if largeur > 0:
            self._largeur = largeur

    def get_surface(self):
        return self._longueur * self._largeur

    def __str__(self):
        return f"Rectangle {self._longueur=}, {self._largeur=}"

    def __eq__(self, value):
        return value.get_longueur() == self._longueur \
            and value.get_largeur() == self._largeur

    longueur = property(get_longueur, set_longueur, doc="Propriété longueur")
    largeur = property(get_largeur, set_largeur, doc="Propriété largeur")


class Rectangle2(CalcGeo):

    # Constructeur
    def __init__(self, longueur, largeur):
        if longueur > 0 and largeur > 0:
            self._longueur = longueur
            self._largeur = largeur
        else:
            self._longueur = 0
            self._largeur = 0

    @property
    def longueur(self):
        """ return valeur de la longueur"""
        return self._longueur

    @longueur.setter
    def longueur(self, longueur):
        """ init valeur de la longueur"""
        if longueur > 0:
            self._longueur = longueur

    @property
    def largeur(self):
        """ return valeur de la largeur"""
        return self._largeur

    @largeur.setter
    def largeur(self, largeur):
        """ init valeur de la largeur"""
        if largeur > 0:
            self._largeur = largeur

    @property
    def surface(self):
        return self._longueur * self._largeur

    def __str__(self):
        return f"Rectangle {self._longueur=}, {self._largeur=}"

    def __eq__(self, value):
        return value.longueur == self._longueur \
            and value.largeur == self._largeur
