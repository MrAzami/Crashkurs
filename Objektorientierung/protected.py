class A():
    def __init__(self,vorname):
        self._vorname = vorname
    def __str__(self):
        return "Der Vorname ist: " + self._vorname
    
class B(A):
    pass

b = B("Hans")
print(b)
a = A("Otto")
print(a._vorname)