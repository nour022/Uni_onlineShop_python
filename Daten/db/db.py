import sqlite3

# Verbindung zur SQLite-Datenbank herstellen
conn = sqlite3.connect('database.db')

# Datenbankcursor erstellen
cursor = conn.cursor()

# Tabelle "Login" erstellen
cursor.execute('''CREATE TABLE IF NOT EXISTS Login (
                    Username TEXT PRIMARY KEY,
                    Fullname TEXT,
                    Password TEXT,
                    Roll TEXT,
                    Budget REAL
                )''')

# Tabelle "Produkt" erstellen
cursor.execute('''CREATE TABLE IF NOT EXISTS Produkt (
                    id INTEGER PRIMARY KEY,
                    Hersteller TEXT,
                     TEXT,
                    Ps INTEGER,
                    KMh INTEGER,
                    Preis REAL,
                    Baujahr INTEGER,
                    Anzahl INTEGER,
                    Photo TEXT,
                    verkaufer TEXT,
                    art TEXT,
                    FOREIGN KEY (verkaufer) REFERENCES Login(Username)
                )''')

# Tabelle "Bestellung" erstellen
cursor.execute('''CREATE TABLE IF NOT EXISTS Bestellung (
                    user TEXT,
                    P_id INTEGER,
                    Datum DATE,
                    verkaufer TEXT,
                    Anzahl INTEGER,
                    Preis REAL,
                    FOREIGN KEY (user) REFERENCES Login(Username),
                    FOREIGN KEY (P_id) REFERENCES Produkt(id),
                    FOREIGN KEY (verkaufer) REFERENCES Login(Username)
                )''')

# Tabelle "Einkaufswagen" erstellen
cursor.execute('''CREATE TABLE IF NOT EXISTS Einkaufswagen (
                    id INTEGER PRIMARY KEY,
                    user TEXT,
                    verkaufer TEXT,
                    productnumer INTEGER,
                    FOREIGN KEY (user) REFERENCES Login(Username),
                    FOREIGN KEY (verkaufer) REFERENCES Login(Username),
                    FOREIGN KEY (productnumer) REFERENCES Produkt(id)
                )''')

# Datenbankverbindung schließen
conn.close()
