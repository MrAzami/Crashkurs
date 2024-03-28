def schreiben():
    datei = open("test.txt","w")
    for i in range(1,11):
        datei.write(f"Zeile {i}\n")
    datei.close()
def lesen():
    datei = open("test.txt","r")
    for zeile in datei:
        print(zeile.rstrip())   # zeilenumbruch von datei entfernt
    datei.close()

def lesen2():
    inhalt = open("test.txt").readlines()
    print(inhalt)

def lesen3():
    inhalt = open("test.txt").read()
    print(inhalt)

# schreiben()
# lesen()
# lesen2()
lesen3()