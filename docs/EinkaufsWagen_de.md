EinkaufsWagen-Klasse
**init**(self, parent)
Initialisiert das EinkaufsWagen-Objekt.
Erstellt das Menü und die Sidebar des Einkaufswagen-Fensters.
Erstellt den Bereich für die Karten (Artikel) im Einkaufswagen.
Lädt die Daten der Artikel aus der Datenbank und erstellt die entsprechenden Karten.
Erstellt das Quittungsfeld und den Scrollbereich für die Artikelübersicht.
we(self, data)
Aktualisiert das Quittungsfeld mit den Benutzerinformationen und der Bestellungsnummer.
Ruft diese Methode auf, um das Quittungsfeld mit den aktuellen Daten zu aktualisieren.
creat_cart_w(self, data)
Erstellt eine Karte für einen Artikel im Einkaufswagen.
Enthält Informationen wie Hersteller, Typ, PS, Preis usw.
Enthält Buttons zum Löschen des Artikels und zum Kauf des Artikels.
Wird für jeden Artikel im Einkaufswagen aufgerufen.
button_clicked(self, e)
Wird aufgerufen, wenn der Benutzer auf den Löschen-Button oder den Kauf-Button klickt.
Ruft die entsprechende Methode (deletCart oder buyCart) auf, um den Artikel zu entfernen oder zu kaufen.
logout(self, e)
Wird aufgerufen, wenn der Benutzer auf den Logout-Button klickt.
Entfernt die Login-Datei (login.csv) und ruft die updateLogin-Methode des Hauptfensters auf, um zum Login-Fenster zu wechseln.
deletCart(self, arr)
Wird aufgerufen, wenn der Benutzer den Löschen-Button für einen Artikel im Einkaufswagen klickt.
Entfernt den Artikel aus dem Einkaufswagen in der Datenbank und aktualisiert die Anzeige des Einkaufswagens.
