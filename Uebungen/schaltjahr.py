# def schaltjahr(x):
#     if x % 4 == 0 and x % 100 != 0:
#         print ("Das Jahr ", x," ist ein schaltjahr")
#     elif x % 400 == 0:
#         print ("Das Jahr ", x," ist ein schaltjahr")
#     else:
#         print ("Das Jahr ", x," ist kein schaltjahr")

# schaltjahr(input("gib das jahr ein: "))

while True:
    jahr = eval(input("Geben Sie das Jahr ein : "))
    if jahr == 0:
        break
    if (jahr % 4 == 0) and (jahr % 100 != 0) or (jahr % 400 == 0):
        print(jahr," ** ist ein Schaltjahr **")
    else:
        print(jahr," ist KEIN Schaltjahr")


## Nicht FERTIG