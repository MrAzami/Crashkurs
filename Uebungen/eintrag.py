# mit cd in den Ordner Uebungen gehen, dann ausführen
def eintrag():
    quelle = open("personen.txt","r")
    ziel = open("personen2.txt","w")
    ausgabe = ""
    for zeile in quelle:
        if ausgabe:
            ausgabe += " " + zeile.rstrip()+"\n"
            ziel.write(ausgabe)
            ausgabe = ""
        else:
            ausgabe = zeile.rstrip()
    quelle.close()
    ziel.close()

eintrag()