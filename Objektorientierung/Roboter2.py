class Roboter:
    __zaehler = 0 # weil es kein self hat, ist es ein klassen attribute
    def __init__(self,name):
        self.__name = name
        # type(self).zaehler += 1       das geht auch
        Roboter.__zaehler += 1
    def get_zaehler():
        return Roboter.__zaehler    #kein self, da classen attribut
    
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,name):
        if name == "Egon":
            self.__name = "Marvin"
        else:
            self.__name = name


r1 = Roboter("Otto")
r2 = Roboter("Anna")
r3 = Roboter("Emil")
print("Anzahl Roboter: " + str(Roboter.get_zaehler()))
print(r1.name)
r1.name = "Eva"
print(r1.name)
