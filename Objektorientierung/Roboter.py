class Roboter:
    def __init__(self,name):
        self.__name = name
    
    def __get_name(self):
        return self.__name
    def __set_name(self,name):
        self.__name = name

    name = property(__get_name,__set_name)

r1 = Roboter("OttO")
print(r1.name)
r1.name = "Eva"
print(r1.name)