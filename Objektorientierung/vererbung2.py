class A:
    def __init__(self):
        self.contentA= "42"
        print("__init__ der Klasse A wird ausgeführt")

    def m(self):
        print("m der Klasse A wird ausgeführt")

class B(A):
    def __init__(self):
        A.__init__(self)
        self.contentB= "44"
        print("__init__ der Klasse B wird ausgeführt")
    def m(self):
        print("m der Klasse B wird ausgeführt")
              
if __name__ == "__main__":
    x = A()
    x.m()
    y = B()
    y.m()
    print("self.contentB von y: " + y.contentB)
    print("self.contentA von y: " + y.contentA)