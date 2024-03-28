def schreiben():
    with open("test2.txt","w") as datei:
        for i in range(1,11):
            datei.write(f"Zeile {i}\n")

def lesen():
    with open("test2.txt","r") as datei:
        for zeile in datei:
            print(zeile.rstrip())

#schreiben()
lesen()
