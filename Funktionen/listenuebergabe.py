def s(liste):
    liste += [47,11]
    print(liste)

l = [1,2,3,4]
s(l[:])     #Übergabe nicht als referenz, nur als kopie
print(l)