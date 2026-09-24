import sqlite3


def main():
    with sqlite3.connect("customers_db.db") as c:
        cur = c.cursor()
        cur.execute(
            "INSERT INTO customers_tbl(first_name,last_name,email,gender,ip_address) VALUES('Fred','Gaurat','fred@gaurat.com','Male','127.0.0.1')"
        )


if __name__ == '__main__':
    main()
