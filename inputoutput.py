import json


def main():
    a = 2
    b = 3
    c = a/b

    # f-string
    result = f" valeur de {a=} / {b=} = c:{c:.2%}"

    print(result)
    l = [1, 2, 3]
    # result = f"{l[0]}, {l[1]}, {l[2]}"
    # result = "{0},{1},{2}".format(1,2,3)
    result = "{0},{1},{2}".format(*l)
    d = {
        "name": "Fred",
        "age": 50,
        "job": "dev",
    }
    l = [d, d]

    # result = f"Bonjour {d['name']}"
    result = "Bonjour {nom}, {travail}".format(nom=d['name'], travail=d['job'])
    result = "Bonjour {name}, {job} {age}".format(**d)
    # result = "Bonjour {name}, {job} {age}".format(name=d['name']...)
    print(result)
    result = "Bonjour {0[name]}, {1[name]}".format(*l)
    print(result)

    # f = open('le_fichier.txt','w')
    f = open('le_fichier.txt', 'a', encoding="utf-8")
    f.write("Bonjour 😊\n")

    f.close()

    # f = open('le_fichier.txt','r')
    f = open('le_fichier.txt')

    for line in f:
        print(line.strip())
        # print(line,end="")

    print(*f)

    f.close()

    d = {
        "name": "Fred",
        "age": 50,
        "job": "dev",
    }


    # import json
    # Ecriture JSON
    f = open('data.json','w')
    json.dump(d,f,indent=4)
    f.close()

    # Lecture JSON
    f = open('data.json','r')
    data = json.load(f)
    print(data)
    f.close()



if __name__ == '__main__':
    main()
