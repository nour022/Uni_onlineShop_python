Klasse: DB_data
Methode: **init**(self)
Initialisiert das DB_data-Objekt.
Stellt eine Verbindung zur SQLite-Datenbankdatei unter 'Daten/db/database.db' her.
Erstellt ein Cursor-Objekt zum Ausführen von SQL-Anweisungen.
Methode: getData_user(self, user) \n
Ruft Benutzerdaten aus der Datenbank basierend auf dem übergebenen Parameter user ab.
Führt eine SELECT-Abfrage aus, um alle Zeilen aus der Tabelle Login abzurufen, in denen der Username dem angegebenen user entspricht.
Gibt die abgerufenen Zeilen zurück.
Methode: getData_card(self)
Ruft Daten für alle Produkte aus der Tabelle Produkt ab.
Führt eine SELECT-Abfrage aus, um alle Zeilen aus der Tabelle Produkt abzurufen.
Gibt die abgerufenen Zeilen zurück.
Methode: getData_card_wk(self, typ)
Ruft Daten für ein bestimmtes Produkt basierend auf dem übergebenen Parameter typ ab.
Führt eine SELECT-Abfrage aus, um alle Zeilen aus der Tabelle Produkt abzurufen, in denen die ID dem angegebenen typ entspricht.
Gibt die abgerufenen Zeilen zurück.
Methode: getData_einkaufsWagen(self)
Ruft Daten für Produkte im Einkaufswagen sowie die Anzahl jedes Produkts ab.
Führt eine SELECT-Abfrage aus, um Daten aus den Tabellen Einkaufswagen und Produkt mithilfe einer JOIN-Operation abzurufen.
Gruppiert das Ergebnis nach Produkt.id.
Gibt die abgerufenen Zeilen zurück.
Methode: insert_user(self, username, password, full_name)
Fügt einen neuen Benutzerdatensatz in die Tabelle Login ein.
Führt eine INSERT-Abfrage aus, um eine neue Zeile mit den angegebenen username, password, full_name, 'User' (Standard-Rolle) und 100000.0 (Standardbudget) hinzuzufügen.
Speichert die Änderungen in der Datenbank.
Methode: insert_card(self, Hersteller, Typ, ps, kmh, preis, baujahr, an, img, vk)
Fügt einen neuen Produkt-Datensatz in die Tabelle Produkt ein.
Führt eine INSERT-Abfrage aus, um eine neue Zeile mit den angegebenen Produktdetails hinzuzufügen: Hersteller, Typ, ps, kmh, preis, baujahr, an, img und vk.
Speichert die Änderungen in der Datenbank.
Methode: insert_to_cart(self, user, vk, pid)
Fügt einen neuen Datensatz in die Tabelle Einkaufswagen ein, um ein zum Warenkorb hinzugefügtes Produkt darzustellen.
Führt eine INSERT-Abfrage aus, um eine neue Zeile mit den angegebenen user, vk und pid (Produktnummer) hinzuzufügen.
Speichert die Änderungen in der Datenbank.
Methode: insert_order(self)
Platzhaltermethode ohne Implementierung zum Einfügen einer Bestellung in die Datenbank.
Methode: close_db(self)
Schließt die Datenbankverbindung.
Methode: UserDatemDb(self, username)
Ruft Benutzerdaten aus der Datenbank basierend auf dem angegebenen username ab.
Extrahiert relevante Informationen aus den abgerufenen Daten, wie FullName, usernames, roll, Budget und das aktuelle Datum.
Schreibt die extrahierten Informationen in eine CSV-Datei mit dem Namen './Daten/login.csv' in einem bestimmten Format.
Wenn die CSV-Datei nicht existiert, wird eine neue Datei erstellt und die Informationen werden geschrieben. Andernfalls werden die Informationen an die vorhandene Datei angehängt.
Methode: getUserDaten(self)
Liest den Inhalt der Datei './Daten/login.csv'.
Gibt den Inhalt als Liste zurück, wobei jedes Element eine Zeile in der Datei darstellt, aufgeteilt durch den Trennzeichen ' | '.
Methode: delet_card(self, id)
Löscht einen Produkt-Datensatz aus der Tabelle Produkt basierend auf dem angegebenen Parameter id.
Führt eine DELETE-Abfrage aus, um die Zeile zu entfernen, bei der die id der angegebenen id entspricht.
Speichert die Änderungen in der Datenbank.
Methode: delet_order(self, id)
Löscht einen Datensatz aus der Tabelle Einkaufswagen basierend auf dem angegebenen Parameter id.
Führt eine DELETE-Abfrage aus, um die Zeile zu entfernen, bei der productnumer der angegebenen id entspricht.
Speichert die Änderungen in der Datenbank.
Methode: update_card(self, Hersteller, Typ, ps, kmh, preis, baujahr, an, img, id)
Aktualisiert einen vorhandenen Produkt-Datensatz in der Tabelle Produkt basierend auf dem angegebenen Parameter id.
Führt eine UPDATE-Abfrage aus, um die Zeile zu ändern, bei der die id der angegebenen id entspricht.
Aktualisiert die Spalten Hersteller, Typ, ps, kmh, preis, baujahr, an und img mit den angegebenen Werten.
Speichert die Änderungen in der Datenbank.
Methode: update_card_auf_lager(self, an, id)
Aktualisiert die Spalte Anzahl (Menge) eines Produkt-Datensatzes in der Tabelle Produkt basierend auf dem angegebenen Parameter id.
Führt eine UPDATE-Abfrage aus
