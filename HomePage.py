import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import customtkinter as ctk
from db_func import DB_data

font_h1 = ("Helvetica", 22, "bold")
font_p = ("Helvetica", 16, "")


class HomePage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        imgd = Image.open("Images/HomeBilder/information-button.png").resize((25, 25))
        self.info_img = ImageTk.PhotoImage(imgd)
        self.parent = parent
        self.getData = DB_data()
        parent.resizable(width=True, height=True)
        self.configure(bg="white")
        datas = self.getData.getUserDaten()
        self.getData.UserDatemDb(datas[1])
        # Create the menu frame
        menu = tk.Frame(self)
        menu.config(background="#334257", height=100)
        menu.pack(fill="x")

        # Create labels for the menu
        limg = Image.open("Images/HomeBilder/traktor.png").resize((50, 50))
        self.lphoto = ImageTk.PhotoImage(limg)
        label1 = ttk.Label(
            menu, image=self.lphoto, background="#334257", foreground="#fff"
        )
        label1.pack(side="left", pady=10, padx=10, expand=1)
        label1.bind("<Button 1>", func=self.parent.homePages)
        # Name Label
        page = tk.Label(
            menu,
            text=" H o m e P a g e ",
            background="#334257",
            fg="#fff",
            font=("Arial", 18, "bold"),
        )
        page.bind("<Button 1>", func=self.parent.homePages)
        page.pack(side="left", pady=10, expand=1)
        eimg = Image.open("Images/HomeBilder/einkaufswagen.png").resize((50, 50))
        self.ephoto = ImageTk.PhotoImage(eimg)
        label_wg = ttk.Label(
            menu, image=self.ephoto, background="#334257", foreground="#fff"
        )
        label_wg.pack(side="right", pady=10, padx=10, expand=1)
        label_wg.bind("<Button 1>", func=self.parent.einkaufsWagen)

        dataFram = tk.Frame(self, height=40)
        dataFram.pack(fill="x")
        # datas = self.getData.getUserDaten()
        fontStyle = ("Arial", 16, "bold italic")
        usernameM = datas[0]

        userLabelM = tk.Label(dataFram, text=f"Name: {usernameM}", font=fontStyle)
        userLabelM.pack(side="left", expand=1)

        budgetM = datas[3]
        budgetMlabel = tk.Label(dataFram, text=f"budget: {budgetM} €", font=fontStyle)
        budgetMlabel.pack(side="left", expand=1)
        # Create the main frame
        self.main = tk.Frame(self)
        self.main.pack(fill="both")
        # ---------search frame-----------#
        self.search_var_home = tk.StringVar()  # search_entry
        self.search_by_home = tk.StringVar()
        self.preis_var_home_bis = tk.StringVar()
        self.preis_var_home_von = tk.StringVar()
        self.search_frame_home = tk.Frame(self.main, width=250, bg="silver")
        self.search_frame_home.pack(side="left", fill="y", padx=20)
        such_lbl = tk.Label(
            self.search_frame_home,
            text="[ s u c h e n ]",
            bg="#283747",
            fg="white",
            font=("Perpetua Titling MT", 10, "bold"),
            relief="solid",
        )
        such_lbl.grid(column=0, row=0, columnspan=3, sticky="swne")

        search_lbl_home = tk.Label(
            self.search_frame_home, text="Filter nach :", bg="silver"
        )
        search_lbl_home.grid(column=0, row=1, padx=5)

        combo_search_home = ctk.CTkComboBox(
            self.search_frame_home,
            justify="left",
            variable=self.search_by_home,
            height=20,
            values=["Hersteller", "Typ", "Leistung (PS)", "KMh", "Preis", "Baujahr"],
            dropdown_fg_color="#85929E",
            fg_color="#85929E",
            border_color="#85929E",
            dropdown_hover_color="#283747",
        )
        combo_search_home.grid(column=1, row=1, padx=5, pady=3)

        search_entry_home = ctk.CTkEntry(
            self.search_frame_home,
            fg_color="#fff",
            text_color="#000",
            textvariable=self.search_var_home,
            height=20,
            width=120,
        )
        search_entry_home.grid(column=2, row=1)

        preis_lbl_home = tk.Label(self.search_frame_home, text="preis :", bg="silver")
        preis_lbl_home.grid(column=0, row=2, padx=5)
        entry_preis_von = ctk.CTkEntry(
            self.search_frame_home,
            fg_color="#fff",
            text_color="#000",
            textvariable=self.preis_var_home_von,
            height=20,
            width=120,
            justify="center",
        )
        entry_preis_von.insert(0, "von")
        entry_preis_von.bind(
            "<FocusIn>", lambda event,: entry_preis_von.delete(0, "end")
        )
        entry_preis_von.grid(column=1, row=2, padx=5)
        entry_preis_bis = ctk.CTkEntry(
            self.search_frame_home,
            fg_color="#fff",
            text_color="#000",
            textvariable=self.preis_var_home_bis,
            height=20,
            width=120,
            justify="center",
        )
        entry_preis_bis.insert(0, "bis")
        entry_preis_bis.bind(
            "<FocusIn>", lambda event,: entry_preis_bis.delete(0, "end")
        )
        entry_preis_bis.grid(column=2, row=2, padx=5)

        submit_home_btn = ctk.CTkButton(
            self.search_frame_home,
            text="Search",
            fg_color="#85929E",
            width=100,
            height=20,
            hover_color="#283747",
            command=self.search,
        )
        submit_home_btn.grid(column=0, row=3, padx=5, pady=5, columnspan=3, sticky="ew")
        # Create the card container frame
        self.card_container = ctk.CTkScrollableFrame(
            self.main, height=800, width=1000, fg_color="#fff"
        )
        self.card_container.pack(fill="y", side="left")

        # Load card data from Excel
        self.card_data = self.getData.getData_card("Fahrzeug")

        # Create cards
        self.photo_list = [
            0,
        ]  # List to store PhotoImage objects
        for card in self.card_data:
            img_path = f"./Images/{card[8]}"
            img = Image.open(img_path).resize((280, 220))
            photo = ImageTk.PhotoImage(img)
            self.photo_list.append(photo)  # Store PhotoImage object in the list
            self.create_card(card, self.card_container)

        # Create footer frame
        self.footer = tk.Frame(self, background="#334257", height=150)
        self.footer.pack(fill="x")

    def search(self):
        self.card_datass = self.getData.searchh(
            str(self.search_by_home.get()),
            str(self.search_var_home.get()),
            verkaufer=self.getData.getUserDaten()[1],
            min_price=str(self.preis_var_home_von.get()),
            max_price=str(self.preis_var_home_bis.get())
        )
        if len(self.card_datass) != 0:
            self.card_container.pack_forget()
            try:
                self.card_containers.pack_forget()
            except AttributeError:
                pass
            self.card_containers = ctk.CTkScrollableFrame(
                self.main, height=800, width=1000, fg_color="#fff"
            )
            self.card_containers.pack(fill="y", side="left")
            # self.photo_list = []

            self.photo_list = [
                0,
            ]  # List to store PhotoImage objects
            for card in self.card_datass:
                img_path = f"./Images/{card[8]}"
                img = Image.open(img_path).resize((250, 250))
                photo = ImageTk.PhotoImage(img)
                self.photo_list.append(photo)  # Store PhotoImage object in the list
                self.create_card(card, self.card_containers)
    def deletCart(self, arr):
        self.getData.delet_order(arr[0], self.getData.getUserDaten()[1])

    def create_card(self, data, div):
        if data[7] != 0:
            self.card = tk.Frame(div, height=250)
            # image Traktor

            cardImg = tk.Label(
                self.card, image=self.photo_list[len(self.photo_list) - 1]
            )
            cardImg.place(x=20, y=10)
            cardImg.bind("<Button>", lambda event, data=data: self.showPhoto(data))
            herLabel = tk.Label(
                self.card, text=f"Hersteller: {data[1]}", font=("Arial", 18, "bold")
            )
            herLabel.place(x=350, y=5)
            hr = ttk.Separator(self.card)
            hr.place(x=350, y=40, width=200, height=10)

            typLabel = tk.Label(
                self.card, text=f"Typ: {data[2]}", font=("Arial", 16, "")
            )
            typLabel.place(x=350, y=50)

            psLabel = tk.Label(self.card, text=f"Ps: {data[3]}", font=("Arial", 16, ""))
            psLabel.place(x=350, y=80)

            kmHLabel = tk.Label(
                self.card, text=f"Km/h: {data[4]} ", font=("Arial", 16, "")
            )
            kmHLabel.place(x=350, y=110)

            bjLabel = tk.Label(
                self.card, text=f"Baujahr: {data[6]}", font=("Arial", 16, "")
            )
            bjLabel.place(x=350, y=150)

            priceLabel = tk.Label(self.card, text=f"Preis: {data[5]}")
            priceLabel.place(x=600, y=60, width=150)
            delet_btn = tk.Label(self.card, image=self.info_img)
            delet_btn.bind("<Button>", lambda event, data=data: self.showPhoto(data))
            delet_btn.place(x=900, y=10, width=25)
            buyBtn = ctk.CTkButton(self.card, text="Add to Cart")
            buyBtn.bind(
                "<Button-1>", lambda event, data=data: self.button_clicked(data)
            )
            buyBtn.place(x=600, y=150)
            hr = ttk.Separator(self.card_container)
            hr.pack()
            self.card.pack(fill="x")

    def button_clicked(self, e):
        self.checkFrame()
        self.save_data(e)

    def save_data(self, id):
        with open("./Daten/login.csv", "r") as userData:
            user = userData.readline().split(" | ")[1]
        self.getData.insert_to_cart(user=user, vk=id[9], pid=id[0])

    def checkFrame(self):
        frameSecseful = tk.Frame(self)
        frameSecseful.place(y=80, x=950, width=300, height=40)

        img = Image.open("Images/HomeBilder/checked.png").resize((20, 20))
        self.photoS = ImageTk.PhotoImage(img)
        pfile = tk.Label(frameSecseful, image=self.photoS)
        pfile.pack(side="left", expand=1, padx=5)

        added = tk.Label(frameSecseful, text="Deine produkt schon in einkaufsWagen!")
        added.pack(side="left", expand=1)
        self.parent.after(2000, frameSecseful.destroy)

    def showPhoto(self, card):
        self.main.pack_forget()
        self.footer.pack_forget()
        card_show = ctk.CTkScrollableFrame(self, fg_color="#fff")
        card_show.pack(fill="both", ipadx=20, ipady=20, expand=1)

        imgFrame = tk.Frame(
            card_show,
        )
        imgFrame.pack(fill="x")

        img = Image.open(f"Images/{card[8]}").resize((650, 500))
        self.photox = ImageTk.PhotoImage(img)
        imgLabel = ttk.Label(imgFrame, image=self.photox)
        imgLabel.pack(side="left")

        textFrame = tk.Frame(imgFrame)
        textFrame.pack(fill="both", expand=1)

        uberschreift = tk.Label(textFrame, text=f"Hersteller: {card[1]} ")
        uberschreift.pack(pady=30)

        textInner = tk.Frame(textFrame)
        textInner.pack(fill="both", expand=1)

        typLabel = tk.Label(
            textInner,
            text=f"{card[2]} {card[3]} ist ein leistungsstarker Traktor mit einer Leistung\n",
        )
        typLabel.place(x=100, y=0)

        psLabel = tk.Label(
            textInner,
            text=f"von {card[4]} PS. Mit einer Höchstgeschwindigkeit von {card[6]} km/h ist er ein\n",
        )
        psLabel.place(x=100, y=30)

        psLabel = tk.Label(
            textInner,
            text=f"zuverlässiges und effizientes Arbeitsgerät für landwirtschaftliche Aufgaben.\n\n",
        )
        psLabel.place(x=100, y=60)

        psLabel = tk.Label(
            textInner,
            text=f"Der Traktor wurde von {card[2]}, einem renommierten Hersteller von Landmaschinen,\n",
        )
        psLabel.place(x=100, y=90)

        psLabel = tk.Label(
            textInner,
            text="entwickelt. Mit seiner robusten Konstruktion und hochwertigen Komponenten bietet\n",
        )
        psLabel.place(x=100, y=120)

        psLabel = tk.Label(
            textInner,
            text=f"der {card[3]} eine hohe Leistungsfähigkeit und Langlebigkeit. Er eignet sich\n",
        )
        psLabel.place(x=100, y=150)

        psLabel = tk.Label(
            textInner,
            text="ideal für verschiedene landwirtschaftliche Anwendungen wie das Ziehen schwerer\n",
        )
        psLabel.place(x=100, y=180)

        psLabel = tk.Label(textInner, text="Lasten oder das Pflügen von Feldern.\n\n")
        psLabel.place(x=100, y=210)

        psLabel = tk.Label(
            textInner,
            text=f"Der {card[2]} {card[3]} verfügt über moderne Funktionen und Technologien, die die\n",
        )
        psLabel.place(x=100, y=240)

        psLabel = tk.Label(
            textInner,
            text="Bedienung erleichtern und die Produktivität steigern. Mit seiner komfortablen Kabine\n",
        )
        psLabel.place(x=100, y=270)

        psLabel = tk.Label(
            textInner,
            text="und ergonomischen Ausstattung sorgt er für eine angenehme Arbeitsumgebung \n",
        )
        psLabel.place(x=100, y=300)

        psLabel = tk.Label(
            textInner,
            text="für den Fahrer.Insgesamt ist der Claas 95E ein leistungsstarker und zuverlässiger Traktor,\n",
        )
        psLabel.place(x=100, y=330)

        psLabel = tk.Label(
            textInner,
            text=" der dieAnforderungen anspruchsvoller landwirtschaftlicher Arbeiten erfüllt.",
        )
        psLabel.place(x=60, y=360)

        priseFrame = tk.Frame(textFrame)
        priseFrame.pack(fill="x", padx=10, pady=20)

        priseLabel = tk.Label(priseFrame, text=f"Prise:  {card[5]}")
        priseLabel.pack(side="left", padx=(100, 0))

        priseBtn = ctk.CTkButton(priseFrame, text="Add to Cart")

        priseBtn.bind("<Button-1>", lambda event, card=card: self.button_clicked(card))
        priseBtn.pack(side="right", padx=(0, 100))

        fahrzugeTeile = tk.Frame(
            card_show,
        )
        fahrzugeTeile.pack(fill="x")
        card_data = self.getData.getData_card("Ersatzteil")

        # Create cards
        self.photo_list = [
            0,
        ]  # List to store PhotoImage objects
        for cards in card_data:
            if cards[2].find(card[1]) != -1:                                                #wurde später hinzugefügt
                img_path = f"./Images/{cards[8]}"
                img = Image.open(img_path).resize((250, 250))
                photo = ImageTk.PhotoImage(img)
                self.photo_list.append(photo)  # Store PhotoImage object in the list
                self.create_card_ZB(cards, fahrzugeTeile)

        self.footer.pack(fill="x")

    def create_card_ZB(self, data, div):
        if data[7] != 0:
            card = tk.Frame(div, height=300, width=800)
            # image Traktor

            cardImg = tk.Label(card, image=self.photo_list[len(self.photo_list) - 1])
            cardImg.place(x=20, y=10)
            # cardImg.bind("<Button>",
            #              lambda event, data=data: self.showPhoto(data))
            herLabel = tk.Label(
                card, text=f"Gerät: {data[1]}", font=("Arial", 18, "bold")
            )
            herLabel.place(x=350, y=5)
            hr = ttk.Separator(card)
            hr.place(x=350, y=40, width=200, height=10)

            typLabel = tk.Label(
                card, text=f"Kompatibel mit: {data[2]}", font=("Arial", 16, "")
            )
            typLabel.place(x=350, y=50)

            # psLabel = tk.Label(card, text=f"Ps: {data[3]}", font=("Arial", 16, ""))
            # psLabel.place(x=350, y=80)
            #
            # kmHLabel = tk.Label(card, text=f"Km/h: {data[4]} ", font=("Arial", 16, ""))
            # kmHLabel.place(x=350, y=110)
            #
            bjLabel = tk.Label(
                card, text=f"auf Lager: {data[7]}", font=("Arial", 16, "")
            )

            bjLabel.place(x=350, y=150)

            priceLabel = tk.Label(card, text=f"Preis: {data[5]}")
            priceLabel.place(x=600, y=90, width=150)

            buyBtn = ctk.CTkButton(card, text="Add to Cart")
            buyBtn.bind(
                "<Button-1>", lambda event, data=data: self.button_clicked(data)
            )
            buyBtn.place(x=600, y=150)
            hr = ttk.Separator(self.card_container)
            hr.pack()
            card.pack(fill="x")
