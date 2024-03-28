x = 5   #Globale variable

def f():
    #mit global x -- können variable innerhalb einer funktion global werden
    x = 10  #Variable nur in der Funktion
    print(x)

f()
print(x)