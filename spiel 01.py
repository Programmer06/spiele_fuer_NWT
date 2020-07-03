from tkinter import *
import random
from tkinter import messagebox


liste_Karten = [2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,11,11,11,11]
wert_Karten = []
dealer_gesamt = []
Highscores = []
wins = 0

def stop():
    exit()

def endeja():
    Neustart.place(x=180, y=100)
    Name = name.get()






def endenein():
    Neustart.place(x=180, y=100)


def push():
    Dasistdername = name.get()
    print(Dasistdername)


def anfang():
    Neustart.place_forget()
    gewinn.set("")
    nein.set("")
    wert_Karten.clear()
    dealer_gesamt.clear()


    liste_Karten = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10,
                    10, 10, 10, 11, 11, 11, 11]

    for _ in range(2):
        dealerzahl = random.choice(liste_Karten)
        dealer_gesamt.append(dealerzahl)
        liste_Karten.remove(dealerzahl)
        wert = "Der Dealer hat", sum(dealer_gesamt)
        dealerkarten.set(wert)
        seinekarten.set(dealer_gesamt)

    for _ in range(2):
        zahl1 = random.choice(liste_Karten)
        wert_Karten.append(zahl1)
        liste_Karten.remove(zahl1)
    soviele = "Du hast", sum(wert_Karten)
    wieviele.set(soviele)
    meinekarten.set(wert_Karten)
    if sum(wert_Karten) > 21:
        item = 11
        if item in wert_Karten:
            wert_Karten.remove(item)
            wert_Karten.append(1)
    elif sum(wert_Karten) == 21:
        messagebox.showinfo("GEWONNEN", "21! Du hast gewonnen!")
        endeja()

def nehmen():
    if sum(wert_Karten) < 21:
        Karte = random.choice(liste_Karten)
        liste_Karten.remove(Karte)
        wert_Karten.append(Karte)
        if sum(wert_Karten) > 21 and Karte == 11:
            wert_Karten.remove(11)
            wert_Karten.append(1)
            soviele = "Du hast", sum(wert_Karten)
            wieviele.set(soviele)
            meinekarten.set(wert_Karten)
        elif sum(wert_Karten) > 21:
            item = 11
            if item in wert_Karten:
                wert_Karten.remove(item)
                wert_Karten.append(1)
                soviele = "Du hast", sum(wert_Karten)
                wieviele.set(soviele)
                meinekarten.set(wert_Karten)

            else:
                verloren = 1
                zuviele = sum(wert_Karten) - 21
                soviele = "Du hast", sum(wert_Karten), "Dealer gewinnt"
                messagebox.showinfo("Verloren", soviele)
                endenein()

        elif sum(wert_Karten) == 21:
            soviele = "21! Du hast gewonnen!"
            messagebox.showinfo("Gewonnen", soviele)
            endeja()

        soviele = "Du hast", sum(wert_Karten)
        wieviele.set(soviele)
        meinekarten.set(wert_Karten)


    else:
        soviele = "Du kannst keine weiteren Karten ziehen"
        messagebox.showwarning("Fehler", soviele)

def bleiben():
    while sum(dealer_gesamt) < 18:
        dealerzahl = random.choice(liste_Karten)
        liste_Karten.remove(dealerzahl)
        dealer_gesamt.append(dealerzahl)
        wert = "Dealer hat", sum(dealer_gesamt)
        dealerkarten.set(wert)
        seinekarten.set(dealer_gesamt)
    if sum(dealer_gesamt) > 21:
        dealer_bust = sum(dealer_gesamt) - 21
        soviele = "Du gewinnst mit", sum(wert_Karten)
        messagebox.showinfo("Gewonnen!", soviele)
        endeja()

    elif sum(dealer_gesamt) > sum(wert_Karten):
        soviele = "Dealer gewinnt mit", sum(dealer_gesamt)
        messagebox.showinfo("Verloren", soviele)
        endenein()

    elif sum(dealer_gesamt) == sum(wert_Karten):
        soviele = "Unentschieden"
        messagebox.showerror("Unentschieden", "Der Dealer und du haben das gleiche Ergebnis")
        endenein()

    else:
        soviele = "Du gewinnst mit", sum(wert_Karten)
        messagebox.showinfo("Gewonnen!", soviele)
        endeja()


main = Tk()
main.title("Blackjack")
main.geometry("540x400")
dealerkarten = StringVar()
meinekarten = StringVar()
meinekarten.set(wert_Karten)
nein = StringVar()
seinekarten = StringVar()
Dealer = Label(main, textvariable=dealerkarten)
Neustart = Button(main, text="Neustart", command=anfang)
Neustart.config(font=("Courier", 50))
Meinekarten = Label(main, textvariable=meinekarten)
Karte_nehmen = Button(main, text="Karte ziehen", command=nehmen)
Dealerkarten = Label(main, textvariable=seinekarten)
Bleiben = Button(main, text="Bleiben", command=bleiben)
Beenden = Button(main, text="Beenden", command=stop)
wieviele= StringVar()
gewinn = StringVar()
name = StringVar()
Karten = Label(main, textvariable=wieviele)
Gewinner = Label(main, textvariable=gewinn, font=("Courier", 30))
keinekartenmehr = Label(main, textvariable=nein, font=("Courier", 20))
Namehier = Label(main, text="Bitte Namen eingeben")
Nameeingabe = Entry(main, textvariable=name)
Nameabgabe = Button(main, text="festlegen", command=push)
Karte_nehmen.place(x=250, y=200)
Meinekarten.place(x=80, y=70)
keinekartenmehr.place(x=50, y=200)
Dealerkarten.place(x=80, y=120)
Bleiben.place(x=170, y=200)
Karten.place(x=30, y=50)
Dealer.place(x=40, y=100)
Gewinner.place(x=0, y=150)
Namehier.place(x=175, y=350)
Nameabgabe.place(x=350, y=315)
Neustart.place(x=180, y=90)
Beenden.place(x=470, y=370)
Nameeingabe.place(x=150, y=300, width=200, height=50)
anfang()
main.mainloop()
