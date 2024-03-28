def f():
    print('Funktion f()')

# verweis = f # es wird ein zeiger auf die funktion definiert
# verweis()
verweis = lambda x:x+2  # anonyme funktion, vor : übergabe wert, dahinter die rückgabe
print(verweis(2))