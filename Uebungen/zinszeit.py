def zinszeit():
    barwert = 1000
    zielwert = 2000
    zins = 0.02
    jahre = 0

    while barwert <= zielwert:
        barwert = barwert + barwert * zins
        jahre += 1

    print(f"Es muss {jahre} jahre angelegt werden")  #f damit ich die variable in den text schreiben kann
    print (f"Barwert beträgt : {barwert}")

zinszeit()