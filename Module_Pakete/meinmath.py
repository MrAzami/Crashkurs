def mein_pi():
    return 3.14

def addieren(a,b,c=0):
    return a+b+c

def multi(a,b,c=1):
    return a*b*c
if __name__ == "__main__": #wird eingeführt damit die z.b. Testung nicht weitergegeben wird
    print('Aus "meinmath"',addieren(2,3,4))