

# the_value = 42

# v = int(input("Valeur :"))
# v = 42
# if v > the_value:
#     print(">")
# elif v < the_value:  # else if
#     print("<")
# elif v == the_value:
#     print("Bravo !")
# else:
#     print("Erreur !")

print(50*'-')
l = ["Valeur 01", "Valeur 02", "Valeur 03", "Valeur 04", "Valeur 05"]


for the_value in l:
    print(the_value)


for i in range(len(l)):
    print(i, l[i])


l = [0, 1, 2, 3, 4, 5, 6]

for i in l:
    if i == 30:
        print('found !')
        break
    print(i)
else:
    print("pas trouvé!")


for i in l:
    # ririri
    pass


the_value = 42


print(50*"-")


def fib(n):    # write Fibonacci series less than n
    """Print a Fibonacci series less than n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()


# Now call the function we just defined:
fib(2000)


def fib2(n):
    """Return a list containing a Fibonacci series less than n."""
    l = []
    a, b = 0, 1
    while a < n:
        l.append(a)
        a, b = b, a+b

    return l


l2 = fib2(2000)
print(l2)


def hello(name, age):
    """Print a greeting to the given name."""
    print("Bonjour "+name+" "+str(age))


hello("Fred", 50)  # passage par position
hello(age=50, name="Fred")  # passage par keywords


i = 10


def f1(a=i):
    print(a)


i = 20
f1()


print(50*'-')


a = 3


def f():
    global a
    a = 2
    print("dedans", a)


print("avant", a)  # 3
f()  # 2
print("après", a)  # 3

print(50*'-')

# packing


def add(*v):
    print(v)
    result = 0
    for value in v:
        # result =result+value
        result += value

    return result


l = [10, 20, 30, 40, 50]
# unpacking
r = add(*l)
print(r)  # 150


r = add(10, 20, 30, 40, 50)
print(r)  # 150
r = add()
print(r)  # 150


def hello(**values):
    print(values)
    """Print a greeting to the given name."""
    # print("Bonjour "+name+" "+str(age))
    print("Bonjour", values["name"], values["age"])


hello(name="fred", age=50, job="dev")

print(50*'-')
l = [10, 20, 30, 40, 50]


def oldmult2(values):
    result = []
    for v in values:
        result.append(v*2)

    return result


def mult2(i):
    return i*2


l2 = mult2(l)
print(l2)  # [20, 40, 60, 80, 1000]
l2 = list(map(mult2, l))
print(l2)

l2 = list(map(lambda i: i*2, l))
print(l2)



