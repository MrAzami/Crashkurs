def aufsum(wert):
    summe = 0
    i = 1
    while i <=wert:
        summe = summe + i
        i += 1
    return summe
print(aufsum(3))