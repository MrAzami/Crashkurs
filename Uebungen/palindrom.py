def ist_palindrom(wort):
    wort = wort.lower()
    return wort == wort [::-1]

def ist_palindrom2(wort):
    wort = wort.lower()
    for i in range(len(wort)//2):
        if wort[i] != wort[-(i+1)]:
            return False
    return True

eingabe = input("bitte ein wort eingeben: ")

if ist_palindrom(eingabe):
    print(f"{eingabe} ist ein Palindrom")
else:
    print(f"{eingabe} ist kein Palindrom")
