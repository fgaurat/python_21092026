from rectangle import Rectangle2


class Carre(Rectangle2):

    def __init__(self, cote):
        super().__init__(cote, cote)
        self._cote = cote

    @property
    def cote(self):
        return self._cote

    @cote.setter
    def cote(self, cote):
        self.longueur =cote 
        self.largeur =cote 
        self._cote = cote

    def __str__(self):
        return f"{__class__.__name__} {self._cote=}"
