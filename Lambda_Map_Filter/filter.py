li = range(1,11)
gerade = list(filter(lambda x: x%2==0,li)) # um nur gerade Zahlen von eine Liste zu zeigen4
ungerade = list(filter(lambda x: x%2==1,li)) # oder x%2!=0
print(gerade)
print(ungerade)

jahre = range(1900,2100)
schaltjahr = list(filter(lambda x: x%4==0 and (x%100!=0 or x%400==0),jahre))
print(schaltjahr)

