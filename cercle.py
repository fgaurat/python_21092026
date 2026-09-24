import math
from calc_geo import CalcGeo


class Cercle(CalcGeo):

    def __init__(self, rayon):
        self.__rayon = rayon

    @property
    def rayon(self):
        return self.__rayon

    @rayon.setter
    def rayon(self, rayon):
        self.__rayon = rayon

    def __str__(self):
        return f"{__class__.__name__} {self.__rayon=}"

    @property
    def surfacee(self):
        # import math
        return math.pi*self.__rayon**2
