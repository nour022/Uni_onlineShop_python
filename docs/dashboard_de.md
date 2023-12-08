Dashboard-Klasse
Die Dashboard-Klasse ist ein tkinter Frame, das das Dashboard des Online-Shops darstellt. Es enthält verschiedene Widgets wie Labels, Buttons, Entry-Felder und eine Tabelle. Hier ist eine Übersicht über die wichtigsten Methoden und Funktionen:

**init**(self, parent)
Initialisiert das Dashboard-Objekt.
Erstellt und platziert alle erforderlichen Widgets, einschließlich Labels, Buttons, Entry-Felder und der Tabelle.
Verbindet die Widgets mit den entsprechenden Methoden.
add_pruduk(self)
Überprüft die Eingabe der Produktinformationen und fügt das Produkt zur Datenbank hinzu.
Ruft die insert_card-Methode des DB_data-Objekts auf, um das Produkt in die Datenbank einzufügen.
Zeigt eine Meldung an, ob das Hinzufügen erfolgreich war oder nicht.
visualisieren(self)
Ruft alle Produkte aus der Datenbank ab und zeigt sie in der Tabelle an.
delete_produk(self)
Löscht das ausgewählte Produkt aus der Datenbank.
Ruft die delet_card-Methode des DB_data-Objekts auf, um das Produkt zu löschen.
Aktualisiert die Tabelle und zeigt eine Meldung über den erfolgreichen Löschvorgang an.
clear(self)
Leert alle Eingabefelder des Dashboards.
select_row(self, event)
Wird aufgerufen, wenn eine Zeile in der Tabelle ausgewählt wird.
Füllt die Eingabefelder mit den Daten der ausgewählten Zeile.
upd_prod(self)
Überprüft die Eingabe der Produktinformationen und aktualisiert das ausgewählte Produkt in der Datenbank.
Ruft die update_card-Methode des DB_data-Objekts auf, um das Produkt zu aktualisieren.
Löscht das alte Produktbild und speichert das neue Produktbild.
Aktualisiert die Tabelle und leert die Eingabefelder.
search(self)
Ruft Produkte aus der Datenbank basierend auf der angegebenen Suchanfrage ab.
Ruft die search-Methode des DB_data-Objekts auf, um die Suche durchzuführen.
Aktualisiert die Tabelle mit den Suchergebnissen.
reset(self)
Zeigt alle Produkte in der Datenbank in der Tabelle an.
da die gescuchte daten erchienden und der Nutzer den Ursrüngliche tabelle angezeigt haben will.
about_us(self)
Zeigt eine Informationsmeldung über die Entwickler des Online-Shops an.
upd_auflager(self)
Aktualisiert den Lagerbestand anhand der zahl im SpinBox widget "pruduk_bestellen" eines ausgewählten Produkts basierend auf der Anzahl der Bestellungen.

Ruft die update_card_auf_lager-Methode des DB_data-Objekts auf, um den Lagerbestand zu aktualisieren.
Aktualisiert das Startbudget des Benutzers basierend auf dem Gesamtpreis der Bestellung.
Aktualisiert die Tabelle und leert die Eingabefelder.
uploadProduct(self)
Öffnet einen Dateidialog, um ein Produktbild auszuwählen.
Speichert den ausgewählten Dateipfad im file_path-Attribut.
Zeigt den Dateinamen im photo_var-Attribut an.
save_img(self, file_path)
Speichert das ausgewählte Produktbild im images-Verzeichnis.
Verwendet die Pillow-Bibliothek, um das Bild zu öffnen, zu kopieren und unter einem neuen Dateinamen zu speichern.
delet_img(self, imgName)
Löscht das angegebene Produktbild aus dem images-Verzeichnis.
Getter-Methoden

