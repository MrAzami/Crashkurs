li = [1,2,3,4,[5,["Eva","Anton"],6,7],20,"otto"] # Liste in einer Liste
# li2 = li
# li2[0] = 100
# print(id(li),id(li2))

# li2 = li.copy()
# print(id(li),id(li2))
# print(li)

def listenausgabe(a_list):
    for daten in a_list:
        if isinstance(daten,list):
            listenausgabe(daten)
            print(daten)
        else:
            print(daten)

listenausgabe(li)