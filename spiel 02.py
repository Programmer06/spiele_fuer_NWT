import time
import random

setzmethode = 0

reihe01 = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34]
reihe02 = [2,5,8,11,14,17,20,23,26,29,32,35]
reihe03 = [3,6,9,12,15,18,21,24,27,30,33,36,]
rot = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
schwarz = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]


def spiel():
    print("Auf was willst du setzen? (Bitte gib entweder Farbe, Reihe oder Nummer ein) ")
    eingabe_methode = input()

    if eingabe_methode == "Reihe" :
        print("Auf welche Reihe möchtest du setzen?(Bitte gib 1, 2, oder 3 ein)")
        eingabe_reihe = input()
        setzmethode = 1


    elif eingabe_methode == "Farbe" :
        print("Auf welche Farbe möchtest du setzen? (Bitte gibt entweder Rot oder Schwarz ein) ")
        eingabe_farbe = input()
        setzmethode = 2

    elif eingabe_methode == "Zahl":
        print("Auf welche Zahl möchtest du setzen?")
        eingabe_zahl = input()
        setzmethode = 3

    for x in range(50):
        time.sleep(0.1)
        x = random.randint(0,37)
        print(x)

    if setzmethode == 1:
        if eingabe_reihe == 1 and x in reihe01:
            print("Du hast gewonnen!", x, "ist in Reihe 1" )
        elif eingabe_reihe == 2 and x in reihe02:
            print("Du hast gewonnen!", x, "ist in Reihe 2" )
        elif eingabe_reihe == 3 and x in reihe03:
            print("Du hast gewonnen!", x, "ist in Reihe 3" )
        else:
            print("Du hast verloren", x, "ist nicht in deiner Reihe")

    elif setzmethode == 2:
        if eingabe_farbe == "Schwarz" and x in schwarz:
            print("Du hast gewonnen!", x, "ist schwarz)
        elif eingabe_farbe == "Rot" and x in rot:
            print("Du hast gewonnen", x, "ist rot)
        else:
            print("Du hast verloren", x, "ist nicht die Farbe, auf die du gesetzt hast")

    elif setzmethode == 3:
        if eingabe_zahl == x:
            print("Du hast gewonnen!!")
        else:
            print("Du hast verloren! Die Zahl war", x )

    print("Möchtest du nochmal spielen?")

    janein = input()

    if janein == "ja" or janein == "Ja":
        spiel()
    else:
        print("Dann nicht.")
        time.sleep(3)
        exit()


spiel()
