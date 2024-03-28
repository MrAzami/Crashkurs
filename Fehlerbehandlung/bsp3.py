import sys
try:
    f = open("daten.txt")
    s = f.readline()
    i = int(s.strip())

except IOError as err:
    (errno,strerror) = err.args
    print("I/O error ({0}) : {1}".format(errno,strerror))

except ValueError:
    print("Kein Integer")

except:
    print("Unerwarteter Fehler")