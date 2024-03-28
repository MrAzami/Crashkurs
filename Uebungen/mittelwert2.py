def mittelwert():
    try:
      x1 = int(input("eine Zahl eingeben:"))
      x2 = int(input("eine Zahl eingeben:"))
      x3 = int(input("eine Zahl eingeben:"))
      x4 = int(input("eine Zahl eingeben:"))

    except:
      print("Nur int Werte erlaubt!")
    print(f"Der Mittelwert ist: {(x1+x2+x3+x4)/4}")

mittelwert()