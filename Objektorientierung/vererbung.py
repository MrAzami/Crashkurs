class Person:
    def __init__(self,vorname,nachname,gebdat):
        self.vorname = vorname
        self.nachname = nachname
        self.gebdat = gebdat

    def __str__(self):
        ret = self.vorname + " " + self.nachname
        ret += " ," + self.gebdat
        return ret

class Angestellter(Person):
    def __init__(self,vorname,nachname,gebdat,personalnummer):
        super().__init__(vorname,nachname,gebdat)       # Übergibt an die mutterclasse, braucht kein self
        # Person.__init__(self,vorname,nachname,gebdat)   # mögliche zweite schreibart, braucht self
        self.personalnummer = personalnummer

    def __str__(self):
        return super().__str__() + " " + self.personalnummer
        # return Person.__str__(self) + " " + self.personalnummer # mögliche zweite schreibart, braucht self

if __name__ == "__main__":

    p1 = Person("Eva", "Huber", "12.12.200")
    # print(p1)
    a1 = Angestellter("Hans","Berger","1.02.1999","4711")
    a2 = Angestellter("Anna","Gruber","1.02.1998","4712")
    li = [p1,a1,a2]     # liste mit den Daten erstellt
    for p in li:
        print(p)
    # print(a1)