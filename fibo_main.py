# region les imports
import fibo
from fibo import fib as the_other_fib
# endregion

fibo.a


def fib(n):

    print("fib", n)


print("l'autre fichier")
print(__name__)  # __main__

fibo.fib(1000)
the_other_fib(1000)

def main():
    pass

if __name__=='__main__':
    main()
