class A(object):
    __slots__ = ['vorname']     # Slots verhindern das nachhinein attribute eingeführt werden
    def __init__(self, vorname):
        self.vorname = vorname
x = A('Otto')
print(x.vorname)
x.nachname = "Meier"    # wird von Slot verhindert
print(x.nachname)