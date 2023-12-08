import tkinter as tk
from datetime import date
from LoginFrame import LoginFrame
from RegisterFrame import RegisterFrame
from HomePage import HomePage
from dashboard import Dashboard
from WagenKorbe import EinkaufsWagen


class Hauptfenster(tk.Tk):
    def __init__(self):
        super().__init__()
        self.dashBoards = None

        self.win_width = 1350
        self.win_height = 800
        self.monitor_center_x = self.winfo_screenwidth() / 2 - (self.win_width / 2)
        self.monitor_center_y = self.winfo_screenheight() / 2 - (self.win_height / 2)
        self.geometry("%dx%d+%d+%d" % (self.win_width, self.win_height, self.monitor_center_x, self.monitor_center_y))

        # self.resizable(width=False, height=False)
        self.login_frame = LoginFrame(self)
        self.register_frame = RegisterFrame(self)

        try:
            with open("./Daten/login.csv", "r") as file:
                check = file.readline()
                data_str = check.split(" | ")
                da = date.today()
                if data_str[4] == str(da):
                    # self.state('zoomed')
                    self.homePage = HomePage(self)
                    self.geometry("%dx%d+%d+%d" % (self.win_width, self.win_height, self.monitor_center_x, self.monitor_center_y))
                    self.current_frame = self.homePage
                    self.current_frame.pack(fill="both", pady=0, padx=0, expand=1)

                else:
                    self.current_frame = self.login_frame
                    self.current_frame.pack(fill="both", pady=75, padx=60)
        except FileNotFoundError:
            self.current_frame = self.login_frame
            self.current_frame.pack(fill="both", pady=75, padx=60)

    # Funktion zum Wechseln zum Login-Fenster
    def switch_to_login(self, e):
        # style
        win_width = 700
        win_height = 650
        monitor_center_x = self.winfo_screenwidth() / 2 - (win_width / 2)
        monitor_center_y = self.winfo_screenheight() / 2 - (win_height / 2)
        self.geometry("%dx%d+%d+%d" % (win_width, win_height, monitor_center_x, monitor_center_y))
        self.resizable(width=False, height=False)
        self.config(bg="#334257")
        self.title("Login")
        self.current_frame.pack_forget()
        self.current_frame = self.login_frame
        self.current_frame.pack(fill="both", pady=75, padx=60)

    # Funktion zum Wechseln zum Registrierungs-Fenster
    def switch_to_register(self, e):
        win_width = 700
        win_height = 650
        monitor_center_x = self.winfo_screenwidth() / 2 - (win_width / 2)
        monitor_center_y = self.winfo_screenheight() / 2 - (win_height / 2)
        self.title("Register")
        self.geometry("%dx%d+%d+%d" % (win_width, win_height, monitor_center_x, monitor_center_y))
        self.resizable(width=False, height=False)
        self.config(bg="#334257")
        self.current_frame.pack_forget()
        self.current_frame = self.register_frame
        self.current_frame.pack(fill="both", pady=40, padx=40)

    # Funktion zum Wechseln zur Startseite
    def homePages(self, e):
        homePages = HomePage(self)
        self.geometry("%dx%d+%d+%d" % (self.win_width, self.win_height, self.monitor_center_x, self.monitor_center_y))
        self.title("Home Page")
        self.configure(background="silver")
        # self.resizable(False, False)
        self.current_frame.pack_forget()
        self.current_frame = homePages
        self.current_frame.pack(fill="both", pady=0, padx=0, expand=1)

    def einkaufsWagen(self, e=None):
        self.einkaufswagen = EinkaufsWagen(self)
        self.geometry("%dx%d+%d+%d" % (self.win_width, self.win_height, self.monitor_center_x, self.monitor_center_y))
        self.title("Einkaufs Wagen")
        self.configure(background="silver")
        # self.resizable(False, False)
        self.current_frame.pack_forget()
        self.current_frame =self.einkaufswagen
        self.current_frame.pack(fill="both", pady=0, padx=0, expand=1)

    def dashBoard(self,e):
        self.dashBoards = Dashboard(self)

        self.geometry("%dx%d+%d+%d" % (self.win_width, self.win_height, self.monitor_center_x, self.monitor_center_y))
        self.title("Verkaufer Dashboard")
        self.configure(background="silver")
        self.resizable(False, False)
        self.current_frame.pack_forget()
        self.current_frame = self.dashBoards
        self.current_frame.pack(fill="both", expand=1)
    def updateLogin(self,e):
        self.current_frame.pack_forget()
        try:
            with open("./Daten/login.csv", "r") as file:
                check = file.readline()
                data_str = check.split(" | ")
                da = date.today()
                if data_str[4] == str(da):
                    self.homePages(None)
                else:
                    self.switch_to_login(None)
        except FileNotFoundError:
            self.switch_to_login(None)

# Erstelle eine Instanz der Hauptklasse
hauptfenster = Hauptfenster()

# Starte die Hauptloop des Hauptfensters
hauptfenster.mainloop()
