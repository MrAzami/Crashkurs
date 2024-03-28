f = lambda x:x*10   # übergabewert:rückgabewert*10
print(f(2))
print((lambda x:x*2)(4))    #lambda funktion direkt aufgerufen, erst funktion dann übergabewert

for i in range(10):
    print((lambda x:x+42)(i))
