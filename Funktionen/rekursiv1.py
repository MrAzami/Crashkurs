# nicht rekursiv
# def fakul1(zahl):
#     ret_wert = 1
#     for i in range(1,zahl+1):
#         ret_wert = ret_wert * i
#     return ret_wert


# 4! = 4*3!
# 3! = 3*2!
# 2! = 2*1

#rekursive funktion,
# funktion ruft sich selber auf und braucht einen ausgang!
# verbraucht sehr viel speicherkapazitäten
# def fakul2(n):
#     if n==1:
#         return 1
#     else:
#         return n*fakul2(n-1)

def rekursion3(k):
    if (k>0):
        result = k + rekursion3(k-1)
        print(result)
    else:
        result = 0
    return result
print("Rekursion-Beispiel: ")
rekursion3(3)