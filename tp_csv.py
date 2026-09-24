

from pprint import pprint


def main():
    with open('MOCK_DATA.csv', 'r') as f:
        # Lecture ligne par ligne
        # for line in f:

        #     clean_line = line.strip()
        #     splited_line = clean_line.split(',')
        #     print(splited_line)

        all_lines = [l.strip() for l in f.readlines()]
        first_line = all_lines[0].split(",")
        data = all_lines[1:]
        for line in data:
            splited_line = line.split(',')
            line_data_size = len(splited_line)  # taille de la liste

            # affichage d'un ligne
            # for i in range(line_data_size):
            #     id_col_name = first_line[i]
            #     id_value = splited_line[i]
            #     print(f"{id_col_name:<10} =====> {id_value}", end=" ")
            #     # print(id_col_name, id_value)

            for item in zip(first_line, splited_line):
                print(item)

            items = dict(zip(first_line, splited_line))

            print(items)


if __name__ == '__main__':
    main()
