def tannenbaum(hoehe):
    for i in range(1,hoehe+1):
        x = 2 * i -1
        y = len(range(1,hoehe+1))-i
        print(y * " " + x * "*")
h = int(input("hoehe eingeben: "))
tannenbaum(h)