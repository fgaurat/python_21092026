from pprint import pprint
import traceback


def div(a, b):
    return a/b


def call_div(a, b):
    r = 0
    try:
        print("OPEN LOG")

        r = div(a, b)
    finally:
        print("CLOSE LOG")

    return r


def main():
    try:
        a = 2
        b = 0
        c = call_div(a, b)
        print(c)
    except ZeroDivisionError as e:
        print("erreur", e)
        traceback.print_exc()
    except TypeError as e:
        print("erreur", e)

    except Exception as e:
        print("erreur", e)
    else:
        print("pas d'erreur")
    finally:
        print("la suite du code")


if __name__ == '__main__':
    main()
