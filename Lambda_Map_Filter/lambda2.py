def f42(x):
    return x+42

def anwenden(f,list):
    ergebnis = []
    for element in list:
        ergebnis.append(f(element))
        """mit f wird f42 aufgerufen und als erstes die 0 übergeben,
        ergebnis wird in die liste übernommen"""
    return ergebnis

print(anwenden(f42,range(10)))  # an f wird die funktion f42 übergeben
print(anwenden(lambda x:x+42,range(10)))