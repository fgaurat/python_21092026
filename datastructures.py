
l = [10, 20, 30, 40, 50]
l.append(60)
print(l)
l.insert(3, 35)
print(l)
last_value = l.pop()
print(l)

l = [10, 20, 30, 40, 50]
l2 = []
for v in l:
    l2.append(v*2)

l2 = list(map(lambda i: i*2, l))

l2 = [v*2 for v in l]


lines = [
    "   ligne 01  ",
    "   ligne 02",
    "ligne 03.   "
]

clean_lines = [line.strip() for line in lines]
print(lines)
print(clean_lines)


print(50*"-")

t = 1, 2, 3, "toto"
# t[0] = 1000
print(t)
a, b, *c = 0, 1, 3, 4, 5

singleton = (1,)
print(50*'-')


s = {1, 2, 3, 3, 3, 4, 4, 5}


pairs = {2, 4, 6, 8}

s.add(7)
print(s)
print(s & pairs)


print(50*'-')
d = {
    "name": "Fred",
    "age": 50,
    "job": "dev"
}


print(d)
print(d["name"])


developpers = [
    {
        "name": "Fred",
        "age": 50,
        "jobs": ["dev", "formateur"]
    },
    {
        "name": "Nina",
        "age": 20,
        "jobs": "dev"
    },
    {
        "name": "Emilie",
        "age": 20,
        "jobs": "dev"
    }
]


# for d in developpers:
#     print(d['name'])


d = {
    "name": "Fred",
    "age": 50,
    "job": "dev"
}


print(d['name'])

for k, v in d.items():
    print(k, v)

l = [10, 20, 30, 40, 50]

for i, v in enumerate(l):
    print(i, v)

if 10 in l:
    print("ouiiiii")
