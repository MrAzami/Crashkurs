import locale
locale.setlocale(locale.LC_ALL,'de_DE')
preis = input("Einen Preis eingeben! ")
preis = locale.atof(preis)
print(preis)

