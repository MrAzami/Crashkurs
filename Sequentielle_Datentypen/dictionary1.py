farbe = input("welche farbe? ")

en_de = {"red":"rot", "blue":"blau", "yellow":"gelb", "green":"grün"}

print(en_de.get("blue"))
print(en_de["yellow"])
print(en_de[farbe])
print (en_de)
print(type(en_de))