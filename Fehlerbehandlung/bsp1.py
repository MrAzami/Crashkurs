try:
    eingabe = input("Zahl eingeben: ")
    print(int(eingabe))

except:# tritt beim Fehler ein
    print("Das ist keine Zahl!")
# except ValueError as e:
#     print("ERROR Message ", e)

# except:
#     print("Allgemeiner Fehler")

finally:# wird immer ausgeführt
    print("wird immer ausgeführt")
