brett = {("a",1):("Turm","Weiss"),
         ("d",1):("Dame","Weiss"),
         ("e",1):("König","Weiss"),
         ("f",1):("Läufer","Weiss"),
         ("h",8):("Turm","Schwarz"),}

print(brett)
print(brett[("e",1)])
print(brett.get(("f",1)))