HomePage-Klasse

**init**(self, parent)
Initialisiert das HomePage-Objekt.
Erstellt und platziert alle erforderlichen Widgets, einschließlich Labels, Buttons und einer Scrollable Frame.
Lädt die Daten für die Karten aus einer Excel-Datei.
Erstellt und platziert die Karten basierend auf den Daten.
create_card(self, data)
Erstellt eine Karte für ein Produkt basierend auf den bereitgestellten Daten.
Erstellt Labels und Buttons für die Produktinformationen und platziert sie in der Karte.
Verbindet den "Add to Cart"-Button mit der Methode button_clicked.
button_clicked(self, e)
Wird aufgerufen, wenn der "Add to Cart"-Button einer Karte geklickt wird.
Ruft die Methode save_data auf und übergibt die ID des ausgewählten Produkts.
save_data(self, id)
Liest den Benutzernamen aus der Datei "login.csv".
Ruft die Methode insert_to_cart des DB_data-Objekts auf, um das Produkt zur Einkaufsliste des Benutzers hinzuzufügen.
showPhoto(self, card, img)
Wird aufgerufen, wenn auf das Bild einer Karte geklickt wird.
Erstellt ein neues Frame, um das vergrößerte Bild und weitere Informationen anzuzeigen.
Zeigt das vergrößerte Bild, den Hersteller und die Leistung des Produkts sowie eine Beschreibung an.
Zeigt den Preis des Produkts und einen "Add to Cart"-Button an.
