Hauptfenster-Klasse
**init**(self)
Initialisiert das Hauptfenster-Objekt.
Erstellt und platziert die Anfangs-Frames (LoginFrame, RegisterFrame oder HomePage) basierend auf dem Zustand der Login-Datei (login.csv).
Verbindet verschiedene Events wie das Wechseln zum Login-Fenster, zum Registrierungs-Fenster oder zur Startseite mit den entsprechenden Methoden.
switch_to_login(self, e)
Wird aufgerufen, wenn das "Sign Up"-Label im Registrierungs-Fenster geklickt wird.
Wechselt zum Login-Fenster und zeigt es an.
switch_to_register(self, e)
Wird aufgerufen, wenn das "Sign Up"-Label im Login-Fenster geklickt wird.
Wechselt zum Registrierungs-Fenster und zeigt es an.
homePages(self, e)
Wird aufgerufen, wenn der Benutzer erfolgreich eingeloggt ist.
Wechselt zur Startseite und zeigt sie an.
einkaufsWagen(self, e)
Wird aufgerufen, wenn der Benutzer auf den Einkaufswagen-Button klickt.
Wechselt zur Seite des Einkaufswagens und zeigt sie an.
dashBoard(self,e)
Wird aufgerufen, wenn der Benutzer auf den Dashboard-Button klickt.
Wechselt zur Dashboard-Seite und zeigt sie an.
updateLogin(self,e)
Wird aufgerufen, wenn das updateLogin-Event ausgelöst wird (z. B. beim Starten der Anwendung).
Überprüft den aktuellen Zustand der Login-Datei (login.csv) und entscheidet, welcher Frame angezeigt werden soll (Login, Registrierung oder Startseite).
mainloop()
Startet die Hauptloop des Hauptfensters, die die GUI-Ereignisse verarbeitet und das Programm am Laufen hält.
