import os
import random
import tkinter as tk
from tkinter import ttk, END, messagebox

import customtkinter as ctk
from PIL import Image, ImageTk

from db_func import DB_data


class EinkaufsWagen(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.getData = DB_data()
        self.username, self.Budget = self.getData.getUserDaten()[1], self.getData.getUserDaten()[3]
        # Create the menu frame
        menu = tk.Frame(self)
        menu.config(background="#334257", height=100)
        menu.pack(fill="x")

        # Create labels for the menu
        limg = Image.open("Images/HomeBilder/traktor.png").resize((50, 50))
        self.lphoto = ImageTk.PhotoImage(limg)
        label1 = ttk.Label(menu, image=self.lphoto, background="#334257", foreground="#fff")
        label1.pack(side="left", pady=10, padx=30, expand=1)
        label1.bind("<Button 1>", func=self.parent.homePages)
        # Name Label
        page = tk.Label(menu, text="[ E i n K a u f s W a g e n ]", background="#334257", fg="#fff",
                        font=("Arial", 18, "bold"))
        page.pack(side="left", pady=10, expand=1)
        # EinkaufsWagen
        eimg = Image.open("Images/HomeBilder/einkaufswagen.png").resize((50, 50))
        self.ephoto = ImageTk.PhotoImage(eimg)
        label_wg = ttk.Label(menu, image=self.ephoto, background="#334257", foreground="#fff")
        label_wg.pack(side="right", pady=10, padx=30, expand=1)
        label_wg.bind("<Button 1>", func=self.parent.einkaufsWagen)
        dataFram = tk.Frame(self, height=40)
        # user Daten
        datas = self.getData.getUserDaten()
        dataFram.pack(fill="x")

        fontStyle = ("Arial", 16, "bold italic")
        usernameM = datas[0]

        userLabelM = tk.Label(dataFram, text=f"Name: {usernameM}", font=fontStyle)
        userLabelM.pack(side="left", expand=1)

        budgetM = datas[3]
        budgetMlabel = tk.Label(dataFram, text=f"budget: {budgetM} €", font=fontStyle)
        budgetMlabel.pack(side="left", expand=1)
        # body freme
        bFrame = tk.Frame(self)
        bFrame.pack(fill="both", expand=1)

        # sidebar Frame
        sidebar = tk.Frame(bFrame, background="#cfc5c5", height=800, )
        sidebar.pack(fill="y", side="left")

        # btnProfile = ctk.CTkButton(sidebar, text="Profile", width=230)
        # btnProfile.pack(pady=2)

        btnHome = ctk.CTkButton(sidebar, text="Home", width=230)
        btnHome.bind("<Button 1>", command=parent.homePages)
        btnHome.pack(pady=2)

        btnDashboard = ctk.CTkButton(sidebar, text="VerkauferDashboard", width=230)
        self.UserData = self.getData.getUserDaten()
        roll = self.UserData[2]
        # print(roll)
        if roll != "Verkaufer":
            btnDashboard.configure(state='disabled', text="um Verkufer zu werden\n Kontaktieren sie uns \n info@uni-online-shop.de",width=200)
            btnDashboard.pack(side="top", expand=2)
        else:
            btnDashboard.bind("<Button 1>", command=parent.dashBoard)
            btnDashboard.pack(pady=2)

        logout = ctk.CTkButton(sidebar, text="logout", width=230)
        logout.bind("<Button 1>", command=self.logout)
        logout.pack(side="top", expand=2)

        # Cards Frame for all photo
        self.cards = ctk.CTkScrollableFrame(bFrame, height=700, width=700, fg_color="#fff")
        self.cards.pack(fill="y", side="left")

        imgd = Image.open("Images/HomeBilder/delete.png").resize((25, 25))
        self.delet_img = ImageTk.PhotoImage(imgd)

        self.card_data = self.getData.getData_einkaufsWagen(self.UserData[1])

        # Create cards
        self.photo_list = [0, ]  # List to store PhotoImage objects
        for item in self.card_data:
            card = item
            img_path = f"./Images/{card[7]}"
            img = Image.open(img_path).resize((250, 250))
            photo = ImageTk.PhotoImage(img)
            self.photo_list.append(photo)  # Store PhotoImage object in the list
            self.creat_cart_w(card)

        # -------------Quittung------#
        self.qutittungNum_var = tk.StringVar()
        self.username_var = tk.StringVar()
        self.username_var.set(str(self.getData.getUserDaten()[1]))
        # print(self.getData.getUserDaten()[1])
        x = random.randint(1000, 9999)
        self.qutittungNum_var.set(str(x))
        self.f1 = tk.Frame(bFrame, bd=2, width=400, height=80, bg="#283747")
        self.f1.pack(side="top", fill="x")
        quittung_nummer = tk.Label(self.f1, text="Quittung Nummer  :", bg="#283747", fg="orange",
                                   font=("Perpetua Titling MT", 12, "bold")).place(x=3, y=40)
        quittung_entry = tk.Entry(self.f1, bd=2, width=27, textvariable=self.qutittungNum_var, justify="center").place(
            x=210, y=40)
        username = tk.Label(self.f1, text=" Username\t   :", bg="#283747", font=("Perpetua Titling MT", 12, "bold"),
                            fg="orange").place(x=3, y=0)
        username_entry = tk.Entry(self.f1, textvariable=self.username_var, bd=2, width=27, justify="center").place(
            x=210, y=3)

        # --------scroll funktion ---------#
        self.f2 = tk.Frame(bFrame, bd=2, width=350, height=400, bg="black")
        self.f2.pack(side="top", fill="x")
        scroll_y = tk.Scrollbar(self.f2, orient="vertical")
        self.textarea = tk.Text(self.f2, yscrollcommand=scroll_y.set, width=50)
        scroll_y.pack(side="right", fill="y")
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill="x", expand=1)

        buyall = tk.Frame(bFrame)
        buyall.pack(side="top", fill="x", pady=10)
        z = 0
        self.gp_var = tk.IntVar()
        for item in self.card_data:
            z += (item[4] * item[9])
        self.gp_var.set(z)
        labelGasamt = tk.Label(buyall, text=f"{self.gp_var.get()} €")
        labelGasamt.pack(side="left", expand=1, padx=15)
        btnBuyAll = ctk.CTkButton(buyall, text="Add All")
        btnBuyAll.bind("<Button-1>", lambda event, data=self.card_data: self.we_all(data))
        btnBuyAll.pack(side="left", expand=1, padx=15)
        btnReset = ctk.CTkButton(buyall, text="Reset All")

        btnReset.bind("<Button-1>", lambda event, data=self.card_data: self.textarea.delete("1.0", END))
        btnReset.pack(side="left", expand=1, padx=0)

        buyall1 = tk.Frame(bFrame)
        self.btnBuyAll1 = ctk.CTkButton(buyall1, text="Buy", fg_color="red", text_color="#fff")

        self.btnBuyAll1.pack(side="left", expand=1, padx=15)
        buyall1.pack(side="top", fill="x", pady=10)

    def creat_cart_w(self, data):
        if data[-1] != "Ersatzteil":
            card = tk.Frame(self.cards, width=700, height=250)
            # image Traktor

            cardImg = tk.Label(card, image=self.photo_list[len(self.photo_list) - 1])
            cardImg.place(x=20, y=10)

            herLabel = tk.Label(card, text=f"Hersteller: {data[1]}", font=("Arial", 18, "bold"))
            herLabel.place(x=280, y=5)
            hr = ttk.Separator(card)
            hr.place(x=280, y=40, width=200, height=10)

            typLabel = tk.Label(card, text=f"Typ: {data[10]}", font=("Arial", 16, ""))
            typLabel.place(x=285, y=50)

            psLabel = tk.Label(card, text=f"Ps: {data[2]}", font=("Arial", 16, ""))
            psLabel.place(x=285, y=80)

            kmHLabel = tk.Label(card, text=f"Km/h: {data[3]} ", font=("Arial", 16, ""))
            kmHLabel.place(x=285, y=110)

            bjLabel = tk.Label(card, text=f"Baujahr: {data[5]}", font=("Arial", 16, ""))
            bjLabel.place(x=285, y=150)

            priceLabel = tk.Label(card, text=f"Preis: {data[4]} €")
            priceLabel.place(x=500, y=40, width=150)

            delet_btn = tk.Label(card, image=self.delet_img)
            delet_btn.bind("<Button>", lambda event, data=data: self.deletCart(data))
            delet_btn.place(x=665, y=10, width=25)

            anzahlBox = ttk.Spinbox(card, from_=1, to=20)
            print(data)
            anzahlBox.set(data[9])
            # anzahlBox.bind("<ButtonRelease>",lambda event, data=data:self.update_value(event,data))
            anzahlBox.bind("<<Increment>>", lambda event, data=data: self.update_value(data))
            anzahlBox.bind("<<Decrement>>", lambda event, data=data: self.deletCartValue(data))
            anzahlBox.place(x=500, y=80, width=150)

            buyBtn = ctk.CTkButton(card, text="Buy this new")
            buyBtn.bind("<Button-1>", lambda event, data=data: self.button_clicked(data))

            buyBtn.place(x=500, y=150)
            hr = ttk.Separator(self.cards)
            hr.pack()
            card.pack()
        else:
            self.create_card_ZB(data,self.cards)

    def update_value(self, data):
        user = self.UserData[1]
        verkaufer = data[8]
        productNum = data[0]
        self.getData.insert_to_cart(user=user, vk=verkaufer, pid=productNum)
        self.parent.einkaufsWagen(None)

    def button_clicked(self, e):
        self.we(e)

    def we(self, data):
        self.textarea.delete("1.0", END)
        self.textarea.insert(END, "    wilkommen zu unserem Online Shop  ")
        self.textarea.insert(END, "\n=======================================")
        self.textarea.insert(END, f"\nBestelloung Nummer :\t{self.qutittungNum_var.get()}")
        self.textarea.insert(END, f"\nName               :\t{self.username_var.get()}")
        self.textarea.insert(END, "\n=======================================\n")

        self.textarea.insert(END, f"\n{data[1]}_{data[-1]} {data[5]}  {data[4]}x {data[9]}")

        self.textarea.insert(END, "\n\n=======================================\n")
        prise = (data[4] * data[9])
        self.textarea.insert(END,
                             f"\nBestelungen: {data[1]}_{data[-2]} Anzahl: {data[9]} Preis: {prise} €")
        self.textarea.insert(END, "\n\n=======================================")
        self.btnBuyAll1.bind("<Button-1>",
                             lambda event, data=data: self.buyProduct(data, prise))

    def we_all(self, datas):
        self.textarea.delete("1.0", END)
        self.textarea.insert(END, "    wilkommen zu unserem Online Shop  ")
        self.textarea.insert(END, "\n\n=======================================\n")
        self.textarea.insert(END, f"\nBestelloung Nummer :\t{self.qutittungNum_var.get()}")
        self.textarea.insert(END, f"\nName               :\t{self.username_var.get()}")
        self.textarea.insert(END, "\n\n=======================================\n")
        anzahl = 0
        prise = 0
        for data in datas:
            self.textarea.insert(END, f"\n{data[1]}_{data[-2]} {data[5]}  {data[4]}x {data[9]}")
            prise += (data[4] * data[9])
            # print(data)
            anzahl += data[9]
        self.textarea.insert(END, "\n\n=======================================\n")
        self.textarea.insert(END,
                             f"\nBestelungen: {self.qutittungNum_var.get()} Anzahl: {anzahl} Preis: {int(prise)} €")
        self.textarea.insert(END, "\n\n=======================================\n")
        self.btnBuyAll1.bind("<Button-1>",
                             lambda event, data=datas: self.buyProduct_all(datas, prise))

    def buyProduct(self, date, gPreise):

        kunde = self.UserData[1]
        verkaufer = date[8]
        if kunde != verkaufer:
            kundeBudget = float(self.UserData[3])
            if kundeBudget < gPreise:
                messagebox.showerror(
                    message=f"deine budget ist: {kundeBudget} € und deine bestelung Prise ist: {gPreise} € \n budget reichen nicht aus")
            else:
                verkauferBudget = self.getData.getData_user(verkaufer)[0][-1]
                # print(verkauferBudget)
                self.getData.update_budget(str((kundeBudget - (date[4] * date[9]))), kunde)
                self.getData.update_budget(str((verkauferBudget + (date[4] * date[9]))), verkaufer)
                # Todo mache minus vonlager
                self.getData.update_card_auf_lager((date[6] - 1), date[0])
                self.deletCart(date)
                self.save()
                self.getData.UserDatemDb(kunde)
                messagebox.showinfo(message="es hat sich erledigt")
                self.parent.einkaufsWagen()
        else:
            self.deletCart(date)
            self.getData.UserDatemDb(kunde)
            self.parent.einkaufsWagen()
            self.save()
            messagebox.showinfo(message="es hat sich erledigt")

    def buyProduct_all(self, s, g_Precise):
        kunde = self.UserData[1]
        for date in s:

            verkaufer = date[8]
            kundeBudget = float(self.UserData[3])
            if kundeBudget < g_Precise:
                messagebox.showerror(
                    message=f"deine budget ist: {kundeBudget} € und deine bestelung Prise ist: {g_Precise} € \n budget reichen nicht aus")
            else:
                verkaufer = date[8]
                if kunde != verkaufer:
                    verkauferBudget = self.getData.getData_user(verkaufer)[0][-1]
                    self.getData.update_budget(str((kundeBudget - (date[4] * date[9]))), kunde)
                    self.getData.update_budget(str((verkauferBudget + (date[4] * date[9]))), verkaufer)
                    # Todo mache minus vonlager
                    self.getData.update_card_auf_lager((date[6] - 1), date[0])
                    self.deletCart(date)
                else:
                    self.deletCart(date)
        self.save()
        self.getData.UserDatemDb(kunde)
        # messagebox.showinfo(message="es hat sich erledigt")
        self.parent.einkaufsWagen()

    def logout(self, e):
        file_path = "./Daten/login.csv"
        os.remove(file_path)
        self.parent.updateLogin(e)

    def deletCart(self, arr):
        self.getData.delet_order(arr[0], self.getData.getUserDaten()[1])
        self.parent.einkaufsWagen(None)

    def deletCartValue(self, arr):
        self.getData.delet_order_value(arr[-1], self.getData.getUserDaten()[1])
        self.parent.einkaufsWagen(None)

    def save(self):
        op = messagebox.askyesno("save", "möchtest du die Quittung speichern?!")
        if op > 0:
            self.bb = self.textarea.get("1.0", END)
            f1 = open('./Daten/quittung/' + str(self.qutittungNum_var.get()) + ".txt", "a",
                      encoding="utf-8")
            f1.write(self.bb)
            f1.close()

        else:
            return
    def create_card_ZB(self, data, div):
        if data[7] != 0:

            card = tk.Frame(div, height=300, width=800)
            # image Traktor
            delet_btn = tk.Label(card, image=self.delet_img)
            delet_btn.bind("<Button>", lambda event, data=data: self.deletCart(data))
            delet_btn.place(x=665, y=10, width=25)

            anzahlBox = ttk.Spinbox(card, from_=1, to=20)

            anzahlBox.set(data[9])
            # anzahlBox.bind("<ButtonRelease>",lambda event, data=data:self.update_value(event,data))
            anzahlBox.bind("<<Increment>>", lambda event, data=data: self.update_value(data))
            anzahlBox.bind("<<Decrement>>", lambda event, data=data: self.deletCartValue(data))
            anzahlBox.place(x=500, y=100, width=150)

            buyBtn = ctk.CTkButton(card, text="Buy this new")
            buyBtn.bind("<Button-1>", lambda event, data=data: self.button_clicked(data))
            buyBtn.place(x=500, y=150)
            cardImg = tk.Label(card, image=self.photo_list[len(self.photo_list) - 1])
            cardImg.place(x=20, y=10)
            # cardImg.bind("<Button>",
            #              lambda event, data=data: self.showPhoto(data))
            herLabel = tk.Label(
                card, text=f"Gerät: {data[1]}", font=("Arial", 18, "bold")
            )
            herLabel.place(x=280, y=5)
            hr = ttk.Separator(card)
            hr.place(x=280, y=40, width=200, height=10)
            test = data[10].split(",")
            newArr = ""
            for i in range(len(test)):
                newArr += test[i]
                if i % 2 == 0:
                    newArr += "\n"

            typLabel = tk.Label(
                card, text=f"Kompatibel mit: \n {newArr}", font=("Arial", 10, "")
            )
            typLabel.place(x=285, y=50)

            bjLabel = tk.Label(
                card, text=f"auf Lager: {data[6]}", font=("Arial", 16, "")
            )
            bjLabel.place(x=285, y=150)

            priceLabel = tk.Label(card, text=f"Preis: {data[4]}")
            priceLabel.place(x=500, y=60, width=150)


            hr = ttk.Separator(self.cards)
            hr.pack()
            card.pack(fill="x")
