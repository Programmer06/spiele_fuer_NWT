from tkinter import *
import random
from tkinter import messagebox

gewinner_zahlen = []
geclickt = 0

def play():
    gewinner_zahlen = []
    x = 0
    y = 0
    main = Tk()
    main.title("Glücksklicker")
    main.geometry("600x600")
    for _ in range(10):
        for _ in range(10):
            Teil = Button(main, text="Drücken", command=click)
            Teil.place(x=x, y=y, width=60, height=60)
            x += 60
        y += 60
        x = 0
    main.mainloop()

def nochmal():
    question = messagebox.askquestion("Nochmal?", "Willst es nochmal versuchen?")
    if question == "yes":
        main.destroy()
        play()
    else:
        exit()


def click():
    gewinner_zahlen = []
    janein = random.randint(1, 36)
    for _ in range(6):
        gewinne = random.randint(1,36)
        while gewinne in gewinner_zahlen:
            gewinne = random.randint(1, 36)

        gewinner_zahlen.append(gewinne)
    if janein in gewinner_zahlen:
        messagebox.showinfo("Win", "Du hast gewonnen")
        nochmal()
    else:
        messagebox.showerror("Verloren", "Du hast leider verloren")
        nochmal()



play()
