class Punkt:
    def __init__(self,x,y):
        self.__x = x
        self.__y = y

    def __get_x(self):
        return self.__x   
    def __get_y(self):
        return self.__y
    
    def __set_x(self,x):
        if x < 0:
            print("x muss grösser 0 sein")
        else:
            self.__x = x
    def __set_y(self,y):
        if y < 0:
            print("y muss grösser 0 sein")
        else:
            self.__y = y

    def __str__(self):
        return f"Wert von x: {self.__x} Wert von y: {self.__y}"
    x = property(__get_x,__set_x)
    y = property(__get_y,__set_y)
    
p1 = Punkt(2,3)
# p1.__set_x(-1)
# p1.__set_y(-1)
print(p1)
p1.x = 33
print(p1.x)
