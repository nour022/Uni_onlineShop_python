import sqlite3
from datetime import date


class DB_data:
    def __init__(self):
        self.conn = sqlite3.connect("Daten/db/database.db")
        self.cursor = self.conn.cursor()

    def getData_user(self, user):
        # print(self.cursor)
        # SELECT-Abfrage ausführen

        self.cursor.execute(f"SELECT * FROM Login Where Username ='{user}'")
        # Alle Zeilen abrufen
        rows = self.cursor.fetchall()
        return rows

    def getData_card(self, art="*"):
        if art != "*":
            self.cursor.execute(f"Select * from Produkt WHERE art = '{art}'")
            rows = self.cursor.fetchall()
            return rows
        else:
            self.cursor.execute(f"Select * from Produkt")
            rows = self.cursor.fetchall()
            return rows

    def getData_card_k(self, art="*", verkaufer="*"):
        if art != "*":
            self.cursor.execute(f"Select * from Produkt WHERE art = '{art}'")
            rows = self.cursor.fetchall()
            return rows
        else:
            self.cursor.execute(f"Select * from Produkt WHERE verkaufer='{verkaufer}' ")
            rows = self.cursor.fetchall()
            return rows

    def getData_card_wk(self, typ):
        self.cursor.execute(f"Select * from Produkt Where ID='{typ}'")
        rows = self.cursor.fetchall()
        return rows

    def getData_einkaufsWagen(self, user):
        self.cursor.execute(
            f"""
		SELECT Produkt.id,Produkt.Hersteller,Produkt.Ps,Produkt.KMh,Produkt.Preis,Produkt.Baujahr,Produkt.Anzahl,Produkt.Photo,Produkt.verkaufer, COUNT(Einkaufswagen.productnumer) AS Anzahl,Produkt.Typ,Einkaufswagen.id
,Produkt.art FROM Einkaufswagen
JOIN Produkt  ON Einkaufswagen.productnumer = Produkt.id WHERE Einkaufswagen.user = '{user}'
GROUP BY Produkt.id;
		"""
        )
        rows = self.cursor.fetchall()
        return rows

    def insert_user(self, username, password, full_name):
        # INSERT-Statement ausführen
        insert_query = "INSERT INTO Login (Username, Fullname, Password, Roll, Budget) VALUES (?, ?, ?, ?, ?)"
        values = (username, full_name, password, "User", 500000.0)
        self.cursor.execute(insert_query, values)
        # Änderungen in der Datenbank speichern
        self.conn.commit()

    def update_budget(self, budg, username):
        insert_query = "UPDATE Login SET Budget = ? WHERE Username = ?"
        values = (budg, username)
        self.cursor.execute(insert_query, values)
        self.conn.commit()

    def insert_card(self, Hersteller, Typ, ps, kmh, preis, baujahr, an, img, vk, art):
        insert_query = "INSERT INTO Produkt (Hersteller, Typ, Ps, KMh, Preis, Baujahr, Anzahl, Photo, verkaufer,art) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?,?)"
        values = (Hersteller, Typ, ps, kmh, preis, baujahr, an, img, vk, art)

        self.cursor.execute(insert_query, values)
        # Änderungen in der Datenbank speichern
        self.conn.commit()

    def insert_to_cart(self, user, vk, pid):
        # INSERT-Statement ausführen
        data = (user, vk, pid)

        insert_query = "INSERT INTO Einkaufswagen ( user, verkaufer, productnumer) VALUES ( ?, ?, ?)"
        self.cursor.execute(insert_query, data)

        # Änderungen in der Datenbank speichern
        self.conn.commit()

    def UserDatemDb(self, username):
        datas = self.getData_user(username)
        datum = date.today()
        usernames = datas[0][0]
        roll = datas[0][3]
        Budget = datas[0][4]
        FullName = datas[0][1]
        try:
            with open("./Daten/login.csv", "w") as file:
                file.write(f"{FullName} | {usernames} | {roll} | {Budget} | {datum}")
        except FileNotFoundError:
            with open("./Daten/login.csv", "a") as file:
                file.write(f"{FullName} | {usernames} | {roll} | {Budget} | {datum}")

    def getUserDaten(self):
        with open("./Daten/login.csv") as data:
            return data.readline().split(" | ")

    def delet_card(self, id):
        insert_query = f"delete from Produkt where id='{id}'"
        self.cursor.execute(insert_query)
        self.conn.commit()

    def delet_order(self, id, user):
        insert_query = (
            f"delete from Einkaufswagen where productnumer='{id}' AND user = '{user}'"
        )
        self.cursor.execute(insert_query)
        self.conn.commit()

    def delet_order_value(self, id, user):
        insert_query = f"delete from Einkaufswagen where id='{id}' AND user = '{user}'"
        self.cursor.execute(insert_query)
        self.conn.commit()

    def update_card(self, Hersteller, Typ, ps, kmh, preis, baujahr, an, img, id, art):
        insert_query = "UPDATE Produkt SET Hersteller = ?, Typ = ?, Ps = ?, KMh = ?, Preis = ?, Baujahr = ?, Anzahl = ?, Photo = ?, art = ? WHERE id = ?"
        values = (Hersteller, Typ, ps, kmh, preis, baujahr, an, img, art, id)

        self.cursor.execute(insert_query, values)
        self.conn.commit()

    def update_card_auf_lager(self, an, id):
        insert_query = "UPDATE Produkt SET Anzahl= ? Where id= ?"
        values = (an, id)
        self.cursor.execute(insert_query, values)
        self.conn.commit()

    # Todo where verkufer unsername
    def search(
            self, search_index, search_value, verkaufer, min_price="von", max_price="bis"
    ):
        if search_index == "Auf Lager":  # TODO change the attribut in DB Auf Lager
            search_index = "Anzahl"
        query_conditions = (
            f"{search_index} = '{search_value}' AND verkaufer = '{verkaufer}'"
        )
        if min_price != "von" and max_price != "bis":
            query_conditions += f" AND Preis >= {min_price} AND Preis <= {max_price}"
        if min_price == "von" and max_price != "bis":
            query_conditions += f" AND Preis <= {max_price}"
        if min_price != "von" and max_price == "bis":
            query_conditions += f" AND Preis >= {min_price}"
        if (
                (search_index == "" or search_value == "")
                and min_price != "von"
                and max_price != "bis"
        ):
            query_conditions = f"verkaufer = '{verkaufer}' AND Preis >= {min_price} AND Preis <= {max_price}"
        if (
                (search_index == "" or search_value == "")
                and min_price != "von"
                and max_price == "bis"
        ):
            query_conditions = f"verkaufer = '{verkaufer}' AND Preis >= {min_price}"
        if (
                (search_index == "" or search_value == "")
                and min_price == "von"
                and max_price != "bis"
        ):
            query_conditions = f"verkaufer = '{verkaufer}' AND Preis <= {max_price}"

        insert_query = f"SELECT * FROM Produkt WHERE {query_conditions}"
        self.cursor.execute(insert_query)
        rows = self.cursor.fetchall()
        return rows

    def searchh(
            self, search_index, search_value, verkaufer, min_price="von", max_price="bis"
    ):
        if search_index == "Auf Lager":  # TODO change the attribut in DB Auf Lager
            search_index = "Anzahl"
        query_conditions = f"{search_index} = '{search_value}' "
        if min_price.isnumeric() and max_price.isnumeric():
            query_conditions += f" AND Preis >= {min_price} AND Preis <= {max_price}"
        if min_price.isnumeric() == False and max_price.isnumeric():
            query_conditions += f" AND Preis <= {max_price}"
        if min_price.isnumeric() and max_price.isnumeric() == False:
            query_conditions += f" AND Preis >= {min_price}"
        if (
                (search_index == "" or search_value == "")
                and min_price.isnumeric()
                and max_price.isnumeric()
        ):
            query_conditions = f" Preis >= {min_price} AND Preis <= {max_price}"
        if (
                (search_index == "" or search_value == "")
                and min_price.isnumeric()
                and max_price.isnumeric() == False
        ):
            query_conditions = f" Preis >= {min_price}"
        if (
                (search_index == "" or search_value == "")
                and min_price.isnumeric() == False
                and max_price.isnumeric()
        ):
            query_conditions = f" Preis <= {max_price}"

        insert_query = f"SELECT * FROM Produkt WHERE {query_conditions}"

        self.cursor.execute(insert_query)
        rows = self.cursor.fetchall()
        return rows

# tset = DB_data()
# tset.insert_card()
