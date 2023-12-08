LoginFrame-Klasse

**init**(self, parent)
Initialisiert das LoginFrame-Objekt.
Erstellt und platziert alle erforderlichen Widgets, einschließlich Labels, Buttons und Eingabefelder.
Verbindet den "Log-in"-Button mit der Methode save_data.
Verbindet das "Sign Up"-Label mit der Methode switch_to_register des übergeordneten Fensters.
check_username(self, e)
Wird aufgerufen, wenn der Fokus aus dem Benutzernamen-Eingabefeld entfernt wird.
Überprüft, ob der eingegebene Benutzername in der Datenbank vorhanden ist.
Wenn der Benutzername nicht vorhanden ist, wird eine Fehlermeldung angezeigt.
save_data(self)
Wird aufgerufen, wenn der "Log-in"-Button geklickt oder die Eingabetaste gedrückt wird.
Überprüft das eingegebene Passwort mit dem Passwort in der Datenbank.
Wenn das Passwort korrekt ist, wird der Benutzer in die Anwendung eingeloggt und die Methode homePages des übergeordneten Fensters aufgerufen.
Wenn das Passwort falsch ist, wird eine Fehlermeldung angezeigt.
