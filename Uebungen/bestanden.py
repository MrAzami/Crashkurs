#note = (input("Bitte Note eingeben: "))
def get_note(note):
    if note == 6 or note == 5:
        return "nicht bestanden"
    elif note <= 4 or note >= 1:
        return "bestanden"

    elif note > 6:
        return "Nur Werte zwischen 1 und 6 zulaessig"
    
print(get_note())
