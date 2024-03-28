def mittelwert(*l):
  summe = 0
  anzahl = len(l)

  for wert in l:
    summe+= wert
    return summe/anzahl

def mittelwert2(*l):
#   summe = sum(l)
#   anzahl = len(l)

    return sum(l)/anzahl(l)

def mittelwert3(erster_wert,*l):
   return((erster_wert + sum(l))/(1+len(l)))
   
print(mittelwert3(1,2,3,4,5))