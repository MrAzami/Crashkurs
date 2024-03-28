def tannenbaum(hoehe):
    for i in range(1,hoehe+1):
        x = 2 * i -1
        y = len(range(1,hoehe+1))-i
        print(y * " "+ x * "*")
h = int(input("hoehe eingeben: "))
tannenbaum(h)

def tannenbaum2(hoehe):
    leer = " "
    stern = "* "
    zeilen = range(1,hoehe+1)
    anzahl = len(zeilen)
    for i in zeilen:
        print(leer * (anzahl-i)+ stern*i)
        
h = int(input("hoehe eingeben: "))
tannenbaum(h)

# def tannenbaum2(hoehe):
#     i=1
#     while i < hoehe:
#         x = 2 * i -1
#         y = len(range(1,hoehe+1))-i
#         print(y * " " + x * "*")
#         i+= 1
# h = int(input("hoehe eingeben: "))
# tannenbaum2(h)
