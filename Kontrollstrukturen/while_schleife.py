def bsp1():
    i = 1
    while i <= 10:
        print (i)
        i += 1

def bsp2():
    li = [1,2,3,4,5,6,7,8,9,10]
    for wert in li:
        if wert % 2 == 0:
            print(wert,end=" ")

def bsp3():
    i=1
    while i <= 10:
        if i == 4:
            continue
        print(i,end=" ")
        i +=1

def bsp4():
    li = range(10)  #range ist eine liste
    for wert in li:
        print(wert,end=" ")

def bsp5():
    li = range(5)
    print(li[-1])   # bei minus zahlen zählt es von hinten

#bsp1()
#bsp2()
#bsp3()
#bsp4()
bsp5()