def bsp1():
    x = 1
    if x == 1:
         print("x hat den wert 1")
    else:
        print("x ist nicht gleich 1")

bsp1()

note = (input("Bitte Note eingeben: "))
def get_note(note):
    if note == 1:
        return "sehr gut"
    elif note == 2:
        return "gut"
    elif note == 3:
        return "befriedigend"
    elif note == 4:
        return "ausreichend"
    elif note == 5:
        return "mangelhaft"
    elif note == 6:
        return "ungenügend"
    else:
        return "Nur Werte zwischen 1 und 6 zulässig"
    
print(get_note())
