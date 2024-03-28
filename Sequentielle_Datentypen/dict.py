en_de = {"red":"rot", "blue":"blau", "yellow":"gelb", "green":"grün"}
#en_de2.copy()   #dictionary kopieren
# en_de.clear()
# print(en_de)

for k in en_de:
    print(k,en_de[k])

for wert in en_de.keys():
    print(wert,en_de[wert])

for k in en_de.keys():
    print(k,)
for v in en_de.values():
    print(v)
for k,v in en_de.items():
    print(k,v)