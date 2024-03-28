def f(*tuple_werte):        # mit * kann man mit beliebig vielen werten aufrufen
    print(tuple_werte)

def f2(**dict_werte):       # doppelte * wert wird als dictionary erwartet und ausgegeben
    print(dict_werte)

t = (1,2,3,4,5,6)
l = [1,2,3,4,5,6]
f(*l)       # * in einer liste, löst die daten als tuple auf
#f2({'a':'append', 'b':'block', 'y':'yes'})
f2(de="Germany", en="English",fr="French")
