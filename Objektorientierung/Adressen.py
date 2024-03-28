class Adressen:
    # vorname = "Anton"
    # nachname = "Maier"
    # alter = 33
    def __init__(self,vorname,nachname,alter):
        self.__vorname = vorname    # mit doppelter unterstrich wird es private
        self.__nachname = nachname
        self.__alter = alter

    # def ausgabe(self):
    #     print(self.vorname,self.nachname,self.alter)
    def __str__(self):
        return f"Vorname: {self.__vorname} Nachname: {self.__nachname} alter: {self.__alter}"
    
    def get_vorname(self):
        return self.__vorname
    def set_vorname(self, vorname):
        self.__vorname = vorname

adr1 = Adressen("Hans","Huber",33)
adr2 = Adressen("Eva","Müller",22)
# adr1.ausgabe()
# adr2.ausgabe()
# print(adr1.__dict__)
print(adr1)
print(adr2)
adr1.set_vorname("Gabi")       #wert wird geändert
print(adr1.get_vorname())