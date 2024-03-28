# import random
# zufallszahl = random.randint(1,49)
# print(zufallszahl)


import random
def zahlenraten():
    durchgang = 0
    aktiv = True
    rzahl = random.randint(1,10)

    while aktiv:
        durchgang = durchgang + 1
        print()
        print(f"{durchgang}. versuch! Du hast nur 3 versuche")
        print()
        eingabe = int(input("Bitte Zahl eingeben: "))

        if eingabe == rzahl:
            print()
            print("*** Gewonnen ***")
            print()
            aktiv = False
            break
        elif eingabe > rzahl:
            print()
            print("deine zahl ist ZU GROß")
        else:
            print()
            print("deine zahl ist ZU KLEIN")

        if (durchgang == 3):
            print()
            print("!!! VERLOREN !!!")
            print()
            print(">>> Es war die Zahl " + str(rzahl) + " <<<")
            aktiv = False
        print()
        print("<<< GAME OVER >>>")
zahlenraten()
