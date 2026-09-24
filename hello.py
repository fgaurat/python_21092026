# UpperCamelCase
# TheWorldIsFlat

# camelCase
# theWorldIsFlat

# kebab-case, train case spin case
# the-world-is-flat


import copy
print("Hello")

# snake_case
the_world_is_flat: bool = True  # False
if the_world_is_flat:
    print("Be careful not to fall off!")


# ceci est un commentaire

# spam = 1


# line = "On fait du Python"
# line = 'On fait du Python'
# line = 'L'orage gronde'
line = 'L\'orage gronde'
line = "L'orage gronde"
print(line)

path = "c:\test\new_project"
path = "c:\\test\\new_project"
path = r"c:\test\new_project"
print(path)


# lines = "Line 01\nLine 02\nLine 03\n"
lines = """
Line01
Line02
Line03
"""


"""
Ceci est un commentaire
sur plusieurs lignes
"""
print(lines)


a = 1
b = "3"

# l = "valeur de a:"+str(a)
l = a+int(b)

print(l)


print("😊"*50)
print("-"*50)
print("la suite")

p = "Python"
print(p[2])
print(p[0])
print(len(p))
# dernière valeur
print(p[len(p)-1])
print(p[-1])
print(p[-2])

print(p[0:2])  # [0:2] # [0:2[
print(p[2:4])  # [2:4] # [4:4[

print(p[:4])
print(p[4:])

print(p[-3:])


# print(p[1000])
print(p[2:1000])

l = [10, 20, 30, 40, 50]

print(l[0])  # Premier
print(l[-1])  # Dernier
print(l[1:4])  # Dernier

l.append(60)

print(l)

# l1 = l.copy()
l1 = l[:]

l[0] = 1000
print("la liste l", l)
print(l1)


l2 = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]


# l3 = l2.copy()
# l3 = copy.copy(l2)
# l3 = l2[:]  # copy

l3 = copy.deepcopy(l2)
l2[1][1] = 5000

print(50*'-')

# Fibonacci series:
# the sum of two elements defines the next

a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a+b
