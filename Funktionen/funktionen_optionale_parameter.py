#Optionale Parameter immer an das Ende!

def addieren(a,b,c=0):
    return a+b+c

def meine_wurzel(basis,potenz=2):
    return basis**(1/potenz)

print(addieren(2,3,2))
print(meine_wurzel(9,3))
