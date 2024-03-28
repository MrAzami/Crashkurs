import random

# def lotto_generator():  #mit set
#     erster_wert = random.randint(1,49)
#     zahlen = {erster_wert}
#     print(type(zahlen))
#     for i in range(1,6):
#         zufallszahl = zahlen.add(random.randint(1,49))
#     print(zahlen)

# def lotto_generator2(): # mit Liste
#     zahlen = list(range(1,49))
#     random.shuffle(zahlen)
#     lotto_zahlen = zahlen[2:8]
#     print(lotto_zahlen)

def lotto_generator3():  # mit Liste
    zahlen = []
    while True:
        zufallszahl = random.randint(1, 49)
        if zufallszahl not in zahlen:
            zahlen.append(zufallszahl)
        if len(zahlen) == 6:
            break
    print(zahlen)

lotto_generator3()