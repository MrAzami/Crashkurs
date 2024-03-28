# print(list(map(lambda x:x+42,range(10))))

#Fahrenheit in Celsius

def cels(T):
    return (float(5)/9)*(T-32)
def fahr(T):
    return ((float(9)/5)*T + 32)
temp = (10, 20, 30, 40, 50)
F = map(fahr, temp)
C = map(cels, F)

temp_in_Fahr = list(map(fahr, temp))
temp_in_Cels = list(map(cels, temp_in_Fahr))

print(temp_in_Cels)
print(temp_in_Fahr)

#mit map
#C = (9.0/5)*F+32
temp = (5, 25, 35, 40, 50)
x=list(map(lambda F:(9.0/5)*F+32,temp))
print(x)

li = range(1,11)
ergebnis = list(map(lambda x:x*x,li))
print(ergebnis)

a = [1,2,3,4]
b = [5,6,7,8]
c = [10,20,30,40]
print(list(map(lambda x,y,z:2.5*x+2*y-z,a,b,c)))


