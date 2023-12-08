import tkinter as tk
from PIL import ImageTk, Image
from tkinter import END, ttk, messagebox, filedialog
from db_func import DB_data
import math
import os
import customtkinter as ctk
import time


class Dashboard(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.getData = DB_data()
        self.root = self

        ctk.set_appearance_mode("Dark")
        # self.parent.title("Online Shop")
        # self.parent.configure(background="silver")
        # self.parent.resizable(False, False)
        title = ctk.CTkLabel(
            self.root,
            text="[  H o m e   P a g e  ]",
            fg_color="#283747",
            font=("Perpetua Titling MT", 14, "bold"),
            corner_radius=6,
        )
        title.bind("<Button-1>", lambda event,: self.parent.homePages(None))
        title.pack(fill="x", padx=30, pady=5)

        # --------variable----------#
        self.search_var = tk.StringVar()  # search_entry
        self.search_by = tk.StringVar()  # search combobox
        self.id_var = tk.StringVar()
        self.hersteller_var = tk.StringVar()
        self.typ_var = tk.StringVar()
        self.leistung_var = tk.StringVar()
        self.km_h_var = tk.StringVar()
        self.preis_var = tk.StringVar()
        self.baujahr_var = tk.StringVar()
        self.auflager_var = tk.StringVar()
        self.delete_produk_var = tk.StringVar()
        self.photo_var = tk.StringVar()
        self.bestell_var = tk.StringVar()
        self.art_var = tk.StringVar()

        # ------------frame für den angemeldete person-----------#
        infos_frame = tk.Frame(self.root, bg="white")
        infos_frame.place(x=1053, y=40, width=265, height=90)

        # ---user name label---#
        label_id = tk.Label(
            infos_frame,
            text="[ A D M I N ]",
            bg="white",
            font=("Perpetua Titling MT", 10, "bold"),
        )
        label_id.place(x=15, y=2)

        self.getusername = tk.StringVar()
        userDaten = self.getData.getUserDaten()
        self.getusername.set(userDaten[1])  # To_Do der eingelogte Nutzer name
        entry_id = tk.Label(
            infos_frame,
            textvariable=self.getusername,
            width=13,
            font=("Arial", 10, "bold"),
            relief="solid",
        )
        entry_id.place(x=150, y=2)

        # ----start budgeet label----#
        label_startbudget = tk.Label(
            infos_frame,
            text="[ B u d g e t ]",
            bg="white",
            font=("Perpetua Titling MT", 10, "bold"),
        )
        label_startbudget.place(x=10, y=30)

        self.getStartbudget = tk.IntVar()
        self.getStartbudget.set(
            userDaten[3]
        )  # To_Do der eingelogte Nutzer start budget
        entry_startbudget = tk.Label(
            infos_frame,
            textvariable=self.getStartbudget,
            width=13,
            font=("Arial", 10, "bold"),
            relief="solid",
        )
        entry_startbudget.place(x=150, y=30)

        # ---------logout/login-----------#

        btn_logout = ctk.CTkButton(
            infos_frame,
            text="[ L o g o u t ]",
            fg_color="#F56D6D",
            font=("Arial", 13),
            text_color=("black", "white"),
            width=140,
            corner_radius=10,
            hover_color="#283747",
        )

        btn_logout.place(x=80, y=60)
        btn_logout.bind("<Button -1>", self.logout)

        # -----------Verkäufer frame------------#
        control_Frame = tk.Frame(self.root, bg="white")
        control_Frame.place(x=1053, y=535, width=265, height=250)
        contro_panel = tk.Label(
            control_Frame,
            text="[ V e r k ä u f e r ]",
            bg="#283747",
            fg="white",
            font=("Perpetua Titling MT", 10, "bold"),
            relief="solid",
        )
        contro_panel.pack(fill="x", ipady=1)

        add_broduk = ctk.CTkButton(
            control_Frame,
            text="Add produckt",
            command=self.add_pruduk,
            width=200,
            height=30,
            fg_color="#85929E",
            hover_color="#283747",
        )
        add_broduk.place(x=33, y=30)

        dele_broduk = ctk.CTkButton(
            control_Frame,
            text="Delete produckt",
            command=self.delete_produk,
            width=200,
            height=30,
            fg_color="#85929E",
            hover_color="#283747",
        )
        dele_broduk.place(x=33, y=65)

        update_broduk = ctk.CTkButton(
            control_Frame,
            text="Update produckt",
            command=self.upd_prod,
            width=200,
            height=30,
            fg_color="#85929E",
            hover_color="#283747",
        )
        update_broduk.place(x=33, y=100)

        clear_broduk = ctk.CTkButton(
            control_Frame,
            text="Clear table",
            command=self.clear,
            width=200,
            height=30,
            fg_color="#85929E",
            hover_color="#283747",
        )
        clear_broduk.place(x=33, y=135)

        about_broduk = ctk.CTkButton(
            control_Frame,
            text="About us",
            command=self.about_us,
            width=200,
            height=30,
            fg_color="#85929E",
            hover_color="#283747",
        )
        about_broduk.place(x=33, y=170)

        exit_broduk = ctk.CTkButton(
            control_Frame,
            text="Exit",
            command=self.root.quit,
            width=200,
            height=30,
            fg_color="#85929E",
            hover_color="#283747",
        )
        exit_broduk.place(x=33, y=205)

        # ------informationen hinzufügen----------#

        produckt_details = tk.Frame(self.root, bg="white")
        produckt_details.place(x=1053, y=135, width=265, height=395)
        details_panel = tk.Label(
            produckt_details,
            text="[ I n f o s ]",
            bg="#283747",
            fg="white",
            font=("Perpetua Titling MT", 10, "bold"),
            relief="solid",
            width=26,
        )
        details_panel.grid(column=0, row=0, columnspan=2, sticky="ewns", ipady=2)

        id_lbl = tk.Label(produckt_details, text="I D :", bg="white")
        id_lbl.grid(column=0, row=1, pady=5)
        id_entry = ctk.CTkEntry(
            produckt_details,
            fg_color="#fff",
            text_color="#000",
            textvariable=self.id_var,
            width=140,
            height=20,
            justify="center",
        )
        id_entry.grid(column=1, row=1)

        hersteller_lbl = tk.Label(
            produckt_details, text="H e r s t e l l e r :", bg="white"
        )
        hersteller_lbl.grid(column=0, row=2, pady=5)
        hersteller_entry = ctk.CTkEntry(
            produckt_details,
            fg_color="#fff",
            text_color="#000",
            textvariable=self.hersteller_var,
            width=140,
            height=20,
            justify="center",
        )
        hersteller_entry.grid(column=1, row=2)

        typ_lbl = tk.Label(produckt_details, text="T y p :", bg="white")
        typ_lbl.grid(column=0, row=3, pady=5)
        typ_entry = ctk.CTkEntry(
            produckt_details,
            fg_color="#fff",
            text_color="#000",
            textvariable=self.typ_var,
            width=140,
            height=20,
            justify="center",
        )
        typ_entry.grid(column=1, row=3)

        leistung_lbl = tk.Label(
            produckt_details, text="L e i s t u n g (PS):", bg="white"
        )
        leistung_lbl.grid(column=0, row=4, pady=5)
        leistung_entry = ctk.CTkEntry(
            produckt_details,
            fg_color="#fff",
            text_color="#000",
            textvariable=self.leistung_var,
            width=140,
            height=20,
            justify="center",
        )
        leistung_entry.grid(column=1, row=4)

        km_h_lbl = tk.Label(produckt_details, text="K m / h :", bg="white")
        km_h_lbl.grid(column=0, row=5, pady=5)
        km_h_entry = ctk.CTkEntry(
            produckt_details,
            fg_color="#fff",
            text_color="#000",
            textvariable=self.km_h_var,
            width=140,
            height=20,
            justify="center",
        )
        km_h_entry.grid(column=1, row=5)

        preis_lbl = tk.Label(produckt_details, text="P r e i s :", bg="white")
        preis_lbl.grid(column=0, row=6, pady=5)
        preis_entry = ctk.CTkEntry(
            produckt_details,
            fg_color="#fff",
            text_color="#000",
            textvariable=self.preis_var,
            width=140,
            height=20,
            justify="center",
        )
        preis_entry.grid(column=1, row=6)

        baujahr_lbl = tk.Label(produckt_details, text="B a u j a h r :", bg="white")
        baujahr_lbl.grid(column=0, row=7, pady=5)
        baujahr_entry = ctk.CTkEntry(
            produckt_details,
            fg_color="#fff",
            text_color="#000",
            textvariable=self.baujahr_var,
            width=140,
            height=20,
            justify="center",
        )
        baujahr_entry.grid(column=1, row=7)

        auflager_lbl = tk.Label(produckt_details, text="A u f  L a g e r :", bg="white")
        auflager_lbl.grid(column=0, row=8, pady=5)
        auflager_entry = ctk.CTkEntry(
            produckt_details,
            fg_color="#fff",
            text_color="#000",
            textvariable=self.auflager_var,
            width=140,
            height=20,
            justify="center",
        )
        auflager_entry.grid(column=1, row=8)

        art_lbl = tk.Label(produckt_details, text="A R T :", bg="white")
        art_lbl.grid(column=0, row=9, pady=5)
        combo_art = ctk.CTkComboBox(
            produckt_details,
            variable=self.art_var,
            height=20,
            values=["Fahrzeug", "Ersatzteil"],
            dropdown_fg_color="#85929E",
            fg_color="white",
            border_color="#85929E",
            dropdown_hover_color="#283747",
            text_color="black",
        )
        combo_art.grid(column=1, row=9, pady=5)

        del_prod_lbl = tk.Label(
            produckt_details,
            text="del prod bei ID:",
            bg="white",
            font=("Arial", 8),
            fg="red",
        )
        del_prod_lbl.grid(column=0, row=10, pady=5)
        del_prod_entry = ctk.CTkEntry(
            produckt_details,
            fg_color="#fff",
            text_color="#000",
            textvariable=self.delete_produk_var,
            width=140,
            height=20,
            justify="center",
        )
        del_prod_entry.grid(column=1, row=10)

        img_label = tk.Label(produckt_details, text="I M A G E :", bg="white")
        img_label.grid(column=0, row=11, pady=5)
        img_btn = ctk.CTkButton(
            produckt_details,
            textvariable=self.photo_var,
            width=155,
            fg_color="#85929E",
            command=self.uploadProduct,
            hover_color="#283747",
            height=22,
        )
        img_btn.grid(column=1, row=11, pady=5)

        self.pb = ttk.Progressbar(
            produckt_details, orient="horizontal", length=250, style=""
        )

        # -------------search Frame-------------#
        search_frame = tk.Frame(self.root, bg="white")
        search_frame.place(x=30, y=40, width=1017, height=40)

        search_lbl = tk.Label(search_frame, text="Suche nach Farhrzeug :", bg="white")
        search_lbl.place(x=4, y=10)

        combo_search = ctk.CTkComboBox(
            search_frame,
            justify="left",
            variable=self.search_by,
            height=20,
            values=[
                "ID",
                "Hersteller",
                "Typ",
                "Leistung (PS)",
                "Km/h",
                "Preis",
                "Baujahr",
                "Auf Lager",
            ],
            dropdown_fg_color="#85929E",
            fg_color="#85929E",
            border_color="#85929E",
            dropdown_hover_color="#283747",
        )
        # combo_search["value"] = ("ID", "Hersteller", "Typ", "Leistung (PS)", "Km/h", "Preis", "Baujahr", "Auf Lager")
        combo_search.place(x=140, y=10)

        search_entry = ctk.CTkEntry(
            search_frame,
            fg_color="#fff",
            text_color="#000",
            textvariable=self.search_var,
            height=20,
            width=120,
        )
        search_entry.place(x=290, y=10)

        search_button = ctk.CTkButton(
            search_frame,
            text="Search",
            fg_color="#85929E",
            command=self.search,
            width=100,
            height=20,
            hover_color="#283747",
        )
        search_button.place(x=420, y=10)

        reset_button = ctk.CTkButton(
            search_frame,
            text="Reset",
            fg_color="#85929E",
            command=self.reset,
            width=100,
            height=20,
            hover_color="#283747",
        )
        reset_button.place(x=525, y=10)

        pruduk_bestellen_lbl = ctk.CTkLabel(
            search_frame,
            text="Produckt bestellen :",
            font=("Arial", 11, "bold"),
            text_color="black",
        )
        pruduk_bestellen_lbl.place(x=635, y=6)
        pruduk_bestellen = ttk.Spinbox(
            search_frame,
            from_=1,
            to=20,
            wrap=True,
            width=10,
            justify="center",
            state="readonly",
            textvariable=self.bestell_var,
        )
        pruduk_bestellen.place(x=750, y=10)
        reset_button = ctk.CTkButton(
            search_frame,
            text="Bestellen",
            fg_color="#85929E",
            command=self.upd_auflager,
            width=100,
            height=20,
            hover_color="#283747",
        )
        reset_button.place(x=840, y=10)
        # ---------hauptFrame----------#
        hp_frame = tk.Frame(self.root, bg="white")
        hp_frame.place(x=30, y=85, width=1017, height=700)

        # -------------scroll zum frame hinzufügen-----------#
        scroll_y = tk.Scrollbar(hp_frame, orient="vertical")
        scroll_x = tk.Scrollbar(hp_frame, orient="horizontal")
        scroll_x.pack(side="bottom", fill="x")
        scroll_y.pack(side="right", fill="y")

        # ------tabelle-------#
        style = ttk.Style()
        style.configure(
            "Treeview",
            background="silver",
            foreground="black",
            rowheight=25,
            fieldbackground="silver",
        )
        style.map("Treeview", background=[("selected", "#283747")])
        self.produckt_table = ttk.Treeview(
            hp_frame,
            columns=(
                "ID",
                "Hersteller",
                "Typ",
                "Leistung (PS)",
                "Km/h",
                "Preis",
                "Baujahr",
                "Auf Lager",
                "Photo",
                "verkäufer",
                "Art",
            ),
            yscrollcommand=scroll_y.set,
            xscrollcommand=scroll_x.set,
        )
        self.produckt_table.place(x=1, y=1, width=1001, height=680)
        self.produckt_table["show"] = "headings"
        self.produckt_table.heading("ID", text="ID")
        self.produckt_table.heading("Hersteller", text="Hersteller")
        self.produckt_table.heading("Typ", text="Typ")
        self.produckt_table.heading("Leistung (PS)", text="Leistung (PS)")
        self.produckt_table.heading("Km/h", text="Km/h")
        self.produckt_table.heading("Preis", text="Preis")
        self.produckt_table.heading("Baujahr", text="Baujahr")
        self.produckt_table.heading("Auf Lager", text="Auf Lager")
        self.produckt_table.heading("Art", text="Art")
        self.produckt_table.heading("verkäufer", text="verkäufer")
        self.produckt_table.heading("Photo", text="Photo")
        self.produckt_table.column("ID", width=10, anchor="center")
        self.produckt_table.column("Hersteller", width=50, anchor="center")
        self.produckt_table.column("Typ", width=60, anchor="center")
        self.produckt_table.column("Leistung (PS)", width=50, anchor="center")
        self.produckt_table.column("Km/h", width=30, anchor="center")
        self.produckt_table.column("Preis", width=50, anchor="center")
        self.produckt_table.column("Baujahr", width=30, anchor="center")
        self.produckt_table.column("Auf Lager", width=30, anchor="center")
        self.produckt_table.column("Art", width=30, anchor="center")
        self.produckt_table.column("verkäufer", width=30, anchor="center")
        self.produckt_table.column("Photo", width=100, anchor="center")
        self.produckt_table.bind("<ButtonRelease-1>", self.select_row)

        # ---------sql-add produckt---------#
        self.visualisieren()  # auf die tabelle zeigen

    def add_pruduk(self):
        if (
            len(self.hersteller_var.get()) != 0
            and len(self.typ_var.get()) != 0
            and len(self.leistung_var.get()) != 0
            and self.photo_var.get() != "Upload Photo"
            and len(self.km_h_var.get()) != 0
            and len(self.preis_var.get()) != 0
            and len(self.baujahr_var.get()) != 0
            and len(self.auflager_var.get()) != 0
        ):
            self.getData.insert_card(
                self.hersteller_var.get(),
                self.typ_var.get(),
                self.leistung_var.get(),
                self.km_h_var.get(),
                self.preis_var.get(),
                self.baujahr_var.get(),
                self.auflager_var.get(),
                self.photo_var.get(),
                self.getData.getUserDaten()[1],
                self.art_var.get(),
            )
            self.visualisieren()
            self.save_img(self.file_path)
            self.clear()  # alle tabellen leereen
            messagebox.showinfo(
                "info!!", "alles hat geklappt produckt wurde hinzugefügt"
            )
        else:
            messagebox.showerror(message="Achtung deine angaben ist nicht voll ständig")

    # ---------auf die tabelle zeigen(alle hinzugefügten produkte zeigen)------------#
    def visualisieren(self):
        rows = self.getData.getData_card_k(verkaufer=self.getData.getUserDaten()[1])
        if len(rows) != 0:
            self.produckt_table.delete(*self.produckt_table.get_children())
            for item in rows:
                self.produckt_table.insert("", END, values=item)
        self.clear()

    # ---------delete produckt---------#
    def delete_produk(self):
        confirm = messagebox.askyesno(
            "Bestätigen", "Möchten Sie wirklich alle Daten löschen?"
        )
        if confirm:
            self.getData.delet_card(self.delete_produk_var.get())
            self.delet_img(f"{self.photo_var.get()}")
            self.visualisieren()

    # --------alle entry felder leeren---------#
    def clear(self):
        self.id_var.set("")
        self.auflager_var.set("")
        self.baujahr_var.set("")
        self.leistung_var.set("")
        self.hersteller_var.set("")
        self.km_h_var.set("")
        self.delete_produk_var.set("")
        self.typ_var.set("")
        self.preis_var.set("")
        self.photo_var.set("Upload Photo")
        self.bestell_var.set(0)
        self.art_var.set("")

    # ---------ein row in der Tabelle auswählen---------#
    def select_row(self, event):
        selectRow = self.produckt_table.focus()
        row = self.produckt_table.item(selectRow)
        items = row["values"]
        try:
            self.id_var.set(items[0])
            self.hersteller_var.set(items[1])
            self.typ_var.set(items[2])
            self.leistung_var.set(items[3])
            self.km_h_var.set(items[4])
            self.preis_var.set(items[5])
            self.baujahr_var.set(items[6])
            self.auflager_var.set(items[7])
            self.art_var.set(items[10])
            self.delete_produk_var.set(items[0])
            self.photo_var.set(items[8])
        except IndexError:
            pass

    # ---------Update Funktion um produkte zu bearbeiten--------
    def upd_prod(self):
        confirm = messagebox.askyesno(
            "Bestätigen", "Möchten Sie wirklich alle Daten Updaten?"
        )
        if confirm:
            self.getData.update_card(
                self.hersteller_var.get(),
                self.typ_var.get(),
                self.leistung_var.get(),
                self.km_h_var.get(),
                self.preis_var.get(),
                self.baujahr_var.get(),
                self.auflager_var.get(),
                self.photo_var.get(),
                self.id_var.get(),
                self.art_var.get(),
            )
            self.visualisieren()
            self.save_img(self.file_path)
            self.delet_img(f"{self.img_extra}")
            self.clear()

    def search(self):
        rows = self.getData.search(
            str(self.search_by.get()),
            str(self.search_var.get()),
            verkaufer=self.getData.getUserDaten()[1],
        )
        if len(rows) != 0:
            self.produckt_table.delete(*self.produckt_table.get_children())
            for item in rows:
                self.produckt_table.insert("", END, values=item)

    def reset(self):
        self.visualisieren()

    def about_us(self):
        messagebox.showinfo(
            "devolpers Amer, nour, theodore",
            "this is a software for selling vehicles and their Equipments",
        )

    def upd_auflager(self):
        try:
            b2 = int(self.auflager_var.get()) + int(self.bestell_var.get())

            self.auflager_var.set(b2)
            strtbud = int(self.getStartbudget.get()) - (
                ((float(self.preis_var.get())/100)*65) * int(self.bestell_var.get())
            )
            self.getStartbudget.set(strtbud)
            self.getData.update_card_auf_lager(
                self.auflager_var.get(), self.id_var.get()
            )
            self.visualisieren()
            self.clear()
            user = self.getData.getUserDaten()[1]
            self.getData.update_budget(str(strtbud), user)
            self.getData.UserDatemDb(user)
        except ValueError:
            messagebox.showerror(
                "Achtung", "Du musst ein Produckt aus der tabelle auswählen"
            )

    def uploadProduct(self):
        self.img_extra = self.photo_var.get()
        types = [("images", "*.png"), ("images", "*.jpg")]
        self.file_path = filedialog.askopenfilename(filetypes=types)
        original_filename = self.file_path.split("/")[-1]
        self.photo_var.set(original_filename)
        try:
            self.pb.grid(column=0, columnspan=2, row=12)
            for task in range(10):
                self.pb["value"] += 10
                self.update()
                time.sleep(0.2)
            self.pb["value"] = 0
            self.parent.after(1000, self.pb.grid_forget)
        except:
            pass

    def save_img(self, file_path):
        if file_path:
            # Öffne das ausgewählte Bild mit Pillow
            image = Image.open(file_path)

            # Erzeuge eine Kopie des Bildes
            image_copy = image.copy()
            # image.r
            # Speicherort für die Kopie
            save_directory = "images"

            # Generiere einen Dateiname für die Kopie
            original_filename = file_path.split("/")[-1]
            filename, extension = original_filename.split(".")
            save_path = f"{save_directory}/{filename}.{extension}"

            # Speichere die Kopie in einer neuen Datei
            image_copy.save(save_path)

            # Schließe das Bild
            image.close()

    def delet_img(self, imgName):
        path = "images"
        imge_path = f"./{path}/{imgName}"
        try:
            os.remove(imge_path)
        except FileNotFoundError:
            pass

    def logout(self, e):
        file_path = "./Daten/login.csv"
        os.remove(file_path)
        self.parent.updateLogin(e)
