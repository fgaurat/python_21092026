import sqlite3
import csv
from pprint import pprint


def main():

    with open('MOCK_DATA.csv', newline='') as f:
        with sqlite3.connect("customers_db.db") as c:
            sql = "INSERT INTO customers_tbl(first_name,last_name,email,gender,ip_address)"
            sql += " VALUES(?,?,?,?,?)"
            reader = csv.DictReader(f)
            # first = next(reader)
            # second = next(reader)
            # all = list(reader)

            # pprint(all[0])
            for data in reader:
                del data['id']
                cur = c.cursor()

                print(data.values())
                cur.execute(sql,list(data.values()))
                # cur.execute(sql,
                #             (data['first_name'],
                #              data['last_name'],
                #              data['email'],
                #              data['gender'],
                #              data['ip_address'])
                #             )

    # with sqlite3.connect("customers_db.db") as c:
    #     cur = c.cursor()
    #     cur.execute(
    #         "INSERT INTO customers_tbl(first_name,last_name,email,gender,ip_address) VALUES('Fred','Gaurat','fred@gaurat.com','Male','127.0.0.1')"
    #     )


if __name__ == '__main__':
    main()
