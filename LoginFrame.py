import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from tkinter import messagebox
from PIL import Image, ImageTk
from datetime import date
from db_func import DB_data

font_h1 = ("Helvetica", 25, "bold")
font_Label = ("Helvetica", 14)
font_color = "red"
class LoginFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.getData = DB_data()
        # style 
        win_width = 700
        win_height = 650
        monitor_center_x = parent.winfo_screenwidth() / 2 - (win_width / 2)
        monitor_center_y = parent.winfo_screenheight() / 2 - (win_height / 2)
        parent.geometry("%dx%d+%d+%d" % (win_width, win_height, monitor_center_x, monitor_center_y))
        parent.resizable(width=False, height=False)
        parent.config(bg="#334257")
        parent.title("Login")
        # Label Login
        labelLogin = ttk.Label(self, text="Login", font=font_h1)
        labelLogin.pack()
        # Login Container
        self.div = ttk.LabelFrame(self, labelwidget=labelLogin, labelanchor="n")
        self.div.pack(fill="both", pady=50, padx=50)
        self.div.columnconfigure(0, weight=2)
        self.div.columnconfigure(1, weight=2)
        self.div.columnconfigure(2, weight=2)

        # img für user login
        img = Image.open("Images/HomeBilder/user.png").resize((150, 150))
        self.photo = ImageTk.PhotoImage(img)
        label_img = ttk.Label(self.div, image=self.photo, text="test")
        label_img.grid(row=0, column=1, sticky="n")
        # Username label
        username_L = ttk.Label(self.div, text="Username: ", font=font_Label)
        username_L.grid(row=1, column=0, sticky="ne", pady=10)
        #Button
        self.username_eny = ctk.CTkEntry(self.div,fg_color="#fff", placeholder_text="Enter your Username",text_color="#000")
        self.username_eny.grid(row=1,column=1, sticky="we", pady=10)
        self.username_eny.bind("<FocusOut>", command=self.check_username)

        # Password label
        password_L = ttk.Label(self.div, text="Password: ", font=font_Label)
        password_L.grid(row=3, column=0, sticky="ne", pady=10)
        
        self.password_eny = ctk.CTkEntry(self.div, show="*",fg_color="#fff" ,placeholder_text="Enter your Password",text_color="#000")
        self.password_eny.grid(row=3, column=1, sticky="we", pady=10)
        ttk.Label(self.div, text=".      .      .      .",foreground="#fff").grid(row=3, column=2)
        # Button login
        login_btn = ctk.CTkButton(self.div, text="Log-in", command=self.save_data,fg_color="#334257",text_color="#fff",hover_color="black")
        login_btn.grid(row=5, column=1, pady=10, sticky="n")
        login_btn.bind("<Key-Return>",command=self.save_data)
        label_register = ttk.Label(self.div, text="Sing Up")
        label_register.grid(row=6, column=1, pady=10, sticky="n")
        label_register.bind("<Button>",parent.switch_to_register)
        

        

    def check_username(self, e):
        username = self.username_eny.get()

        if len(username) >= 0:
            try:
                # excel_file = pandas.read_excel('./Daten/LoginDaten.xlsx')
                # datas = excel_file.loc[excel_file["Username"] == username]
                str_commit = tk.StringVar()
                datas = self.getData.getData_user(user=username)
                error_Label = tk.Label(self.div, textvariable=str_commit)
                
                if len(datas) != 0:
                    self.checkPasswd = datas[0][2]
                else:
                    # messagebox.showwarning(message="Hallo deine eingabe")
                    str_commit.set("Deine Username ist Falsch")
                    error_Label.grid(row=2, column=1, sticky="we")
                    error_Label.config(foreground="red")
                    self.after(2000, error_Label.destroy)


            except FileNotFoundError:
                pass
    def save_data(self):
        username = self.username_eny.get()
        datas = self.getData.getData_user(user=username)
        datum = date.today()
        usernames = datas[0][0]
        roll = datas[0][3]
        Budget = datas[0][4]
        FullName = datas[0][1]
        try:
            if self.password_eny.get() == datas[0][2]:

                with open("./Daten/login.csv", "w") as file:
                    file.write(f"{FullName} | {usernames} | {roll} | {Budget} | {datum}")
            else:
                messagebox.showwarning(message="Passwort ist falsch")
        except FileNotFoundError:
            with open("./Daten/login.csv", "a") as file:
                file.write(f"{FullName} | {usernames} | {roll} | {Budget} | {datum}")
        # self.root.pack_forget()
        # self.parent.state('zoomed')
        self.parent.homePages(None)

       