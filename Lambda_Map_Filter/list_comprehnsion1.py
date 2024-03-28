quadrate = [i**2 for i in range(1,11)]
print(quadrate)

# q = []
# for i in range (1,11):
#     q.append(i**2)
# print(q) # alles markieren und dann strg + #

wert7 = [(x,y) for x in range(1,7) for y in range (1,7) if x+y ==7]
print(wert7) # [(1, 6), (2, 5), (3, 4), (4, 3), (5, 2), (6, 1)]
# wir haben zwei Wurfel x und y

Celsius = [39,36,37,20]
Fahrenheit = [((float(9)/5)*x +32) for x in Celsius]
print(Fahrenheit)

farben=["rot","grün","blau"]
tiere=["Hunde","Katzen"]
farben_tiere=[(x,y) for x in farben for y in tiere]
print(farben_tiere)

alle = [(x,y) for x in range(1,7) for y in range(1,7)]
summe7 = [x for x in alle if sum(x)==7] # sum ist eine eingebaute Funktion
anzahl_alle = len(alle)
anzahl7 = len(summe7)
ws = anzahl7/anzahl_alle
print("Die Wahrscheinlichkeit eine Summe zu bekommen ist: {}".format(ws))
print(sum([x**2 for x in range(1,11)]))
print(sum([x for x in range(1,101)]))



