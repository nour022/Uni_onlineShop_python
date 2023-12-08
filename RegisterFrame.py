import tkinter as tk
import customtkinter as ctk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import pandas, random, re
from db_func import DB_data

font_h1 = ("Helvetica", 25, "bold")
font_Label = ("Helvetica", 14)
font_color = "red"


class RegisterFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        parent.title("Register")
        self.parent = parent
        self.getData = DB_data()

        # Label Register
        label_login = ttk.Label(text="Register", font=font_h1)

        # Login Container
        self.div = ttk.LabelFrame(self, labelwidget=label_login, labelanchor="n")
        self.div.columnconfigure(0, weight=2)
        self.div.columnconfigure(1, weight=2)
        self.div.columnconfigure(2, weight=2)
        self.div.pack(fill="both", pady=40, padx=40)

        # img für user login
        img = Image.open("Images/HomeBilder/user.png").resize((150, 150))
        self.photo = ImageTk.PhotoImage(img)
        label_img = ttk.Label(self.div, image=self.photo, text="test")
        label_img.grid(row=0, column=1, sticky="n")

        # Full Name label
        self.fA = False
        full_name_label = ttk.Label(self.div, text="Full Name:", font=font_Label)
        full_name_label.grid(row=1, column=0, sticky="ne", pady=10)

        self.full_name_entry = ctk.CTkEntry(self.div, fg_color="#fff", placeholder_text="Max Muster", text_color="#000")
        self.full_name_entry.grid(row=1, column=1, sticky="we", pady=10)
        # one event FocusOut for FullName To check the size of the value
        self.full_name_entry.bind("<FocusOut>", command=self.check_name)

        # User Name Label & Entry
        username_label = ttk.Label(self.div, text="Username: ", font=font_Label)
        username_label.grid(row=3, column=0, sticky="ne", pady=10)

        self.username_entry = ctk.CTkEntry(self.div, fg_color="#fff", placeholder_text="Mrxx-_-00", text_color="#000")
        self.username_entry.grid(row=3, column=1, sticky="we", pady=10)
        # one event FocusOut for username To check if the value is valid
        self.username_entry.bind("<FocusOut>", command=self.check_username)
        self.fU = False

        # Password label
        password_label = ttk.Label(self.div, text="Password: ", font=font_Label)
        password_label.grid(row=5, column=0, sticky="ne", pady=10)
        self.password_entry = ctk.CTkEntry(self.div, fg_color="#fff", placeholder_text="Enter Your password",
                                           text_color="#000")
        self.password_entry.grid(row=5, column=1, sticky="we", pady=10)
        self.pass_generator_btn = ctk.CTkButton(self.div, text="Password Generator", command=self.generate_password,
                                                fg_color="#334257", text_color="#fff", hover_color="black")
        self.pass_generator_btn.grid(row=5, column=2, sticky="w", pady=10)

        # Enter the password again
        password_label_2 = ttk.Label(self.div, text="Password-Again: ", font=font_Label)
        password_label_2.grid(row=7, column=0, sticky="ne", pady=10)
        self.password_entry_2 = ctk.CTkEntry(self.div, fg_color="#fff", placeholder_text="Password", text_color="#000")
        self.password_entry_2.grid(row=7, column=1, sticky="we", pady=10)
        # one event FocusOut for Password To check if the value is valid
        self.password_entry_2.bind("<FocusOut>", command=self.check_password)
        self.fP = False

        # Save data button
        self.register_btn = ctk.CTkButton(self.div, text="Register", command=self.save_data, fg_color="#334257",
                                          text_color="#fff", hover_color="black")
        self.register_btn.grid(row=8, column=1, pady=20, sticky="n")

        label_Lgoin = ttk.Label(self.div, text="Sing in")
        label_Lgoin.grid(row=9, column=1, pady=10, sticky="n")
        label_Lgoin.bind("<Button>", parent.switch_to_login)

    def check_name(self, event):
        size = len(self.full_name_entry.get())
        str_commit = tk.StringVar()
        error_Label = tk.Label(self.div, textvariable=str_commit)
        if size < 6:
            # messagebox.showinfo(message=f"Your name must be at least 6 characters long. Current size: {size}")
            str_commit.set(f"Geben sie bitte vollstandig Name ({self.full_name_entry.get()})")
            error_Label.grid(row=2, column=1, sticky="we")
            error_Label.config(foreground="red")
            self.div.after(2000, error_Label.destroy)
        else:
            self.fA = True

    def check_username(self, e):
        username = self.username_entry.get()
        str_commit = tk.StringVar()
        error_Label = tk.Label(self.div, textvariable=str_commit)
        if len(username) > 4:
            try:
                # excel_file = pandas.read_excel('./Daten/LoginDaten.xlsx')
                # datas = excel_file.loc[excel_file["Username"] == username]
                datas = self.getData.getData_user(user=username)

                if len(datas) != 0:
                    # messagebox.showinfo(
                    #     message=f"This username '{username}' is already taken. Please choose another username.")
                    str_commit.set(f"This username '{username}' is already taken.\n Please choose another username.")
                    error_Label.grid(row=4, column=1, sticky="we")
                    error_Label.config(foreground="red")
                    self.div.after(2000, error_Label.destroy)
                else:
                    self.fU = True
            except:
                self.fU = True
        else:
            # messagebox.showinfo(
            #     message=f"The entered username '{username}' is too short. Please use a username with at least 5 characters.")
            str_commit.set(
                f"The entered username '{username}' is too short. Please use \na username with at least 5 characters.")
            error_Label.grid(row=4, column=1, sticky="we")
            error_Label.config(foreground="red")
            self.div.after(2000, error_Label.destroy)

    def check_password(self, e):
        pattern = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&\(\)])[A-Za-z\d@\(\)$!%*?&+**,&%#*!#@]{8,}$"
        password = self.password_entry.get()
        str_commit = tk.StringVar()
        error_Label = tk.Label(self.div, textvariable=str_commit)
        if re.match(pattern, password):
            if password == self.password_entry_2.get():
                self.fP = True
            else:
                # messagebox.showinfo(
                # message="The entered passwords do not match. Please check your input or use our Password Generator.")
                str_commit.set(
                    f"The entered passwords do not match. Please check \n your input or use our Password Generator.")
                error_Label.grid(row=6, column=1, sticky="we")
                error_Label.config(foreground="red")
                self.div.after(2000, error_Label.destroy)
        else:
            messagebox.showinfo(
                message="Password requirements:\n- Minimum length of 8 characters\n- At least one lowercase letter\n- At least one uppercase letter\n- At least one digit\n- At least one special character")

    def generate_password(self):
        self.password_entry.delete(0, tk.END)
        self.password_entry_2.delete(0, tk.END)
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u',
                   'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
                   'P',
                   'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '#', '@', '%', '&', '(', ')', '*', '+']
        nr_letters = random.randint(8, 10)
        nr_symbols = random.randint(2, 4)
        nr_numbers = random.randint(2, 4)

        password_list = []

        for _ in range(nr_letters):
            password_list.append(random.choice(letters))

        for _ in range(nr_symbols):
            password_list += random.choice(symbols)

        for _ in range(nr_numbers):
            password_list += random.choice(numbers)

        random.shuffle(password_list)

        password = "".join(password_list)
        self.password_entry.insert(0, password)
        self.password_entry_2.insert(0, password)
        self.check_password("")

    def save_data(self):
        if self.fU and self.fP and self.fA:
            username = self.username_entry.get()
            password = self.password_entry.get()
            full_name = self.full_name_entry.get()
            # data = {
            # 	'Full Name': [full_name], 'Username': [username], 'Password': [password], "roll": False,
            # 	"Budget": 100000
            # }
            # new_data = pandas.DataFrame(data)
            # try:
            # 	excel_file = pandas.read_excel('./Daten/LoginDaten.xlsx')
            # except FileNotFoundError:
            # 	# create new Excel file with new data
            # 	new_data.to_excel('./Daten/LoginDaten.xlsx', index=False)
            # 	# excel_file = pandas.read_excel('./Daten/LoginDaten.xlsx')
            # # append new data to existing Excel file
            # updated_data = pandas.concat([excel_file, new_data])
            # updated_data.to_excel('./Daten/LoginDaten.xlsx', index=False)
            self.getData.insert_user(username=username, password=password, full_name=full_name)

            self.clear_data()
            self.parent.switch_to_login()

        else:
            print(f"Username {self.fU} : Password {self.fP} : Fullname {self.fA}")
            messagebox.showerror(message="Hello, please check your input.")

    def clear_data(self):
        self.getData.close_db()
        messagebox.showinfo(message=f"Username: {self.username_entry.get()}\nPassword: {self.password_entry.get()}")
        self.password_entry.delete(0, tk.END)
        self.password_entry_2.delete(0, tk.END)
        self.username_entry.delete(0, tk.END)
        self.full_name_entry.delete(0, tk.END)
        self.fU = False
        self.fA = False
        self.fP = False
