from pprint import pprint

from rectangle import Rectangle, Rectangle2

from carre import Carre
from cercle import Cercle


def main():
    r = Rectangle(4, 6)
    r1 = Rectangle(4, 6)
    r2 = Rectangle2(4, 6)

    r2.longueur = 22
    print(r2.surface)
    print(r2.longueur)
    print(r2.largeur)

    r.longueur = 1000
    print(r.longueur)
    print(r.get_longueur())
    r.set_longueur(-45)
    print(r.get_longueur())
    surface = r.get_surface()
    print(surface)

    s = str(r)
    print(s)

    if r == r1:
        print("ok")
    else:
        print("ko")

    # from carre import Carre

    c = Carre(2)
    print(c.cote)  # 2 ?
    print(c.surface)  # 4 ?
    print(c)

    ce = Cercle(2)

    print(ce.surface)


if __name__ == '__main__':
    main()
