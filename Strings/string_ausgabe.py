preis = 44.33
steuer = 0.19
brutto = preis *(1+steuer)

print("Preis: {0:<6.2f} steuer: {1:4.2f} brutto: {2:<6.2f}".format(preis,steuer,brutto))

s = "Python"

print(s.center(100))
print(s.ljust(12),":")
print(s.rjust(12,"0"))
print(s.zfill(100))

ausgabe = "Preis: {0:<6.2f} steuer: {1:4.2f} brutto: {2:<6.2f}".format(preis,steuer,brutto)
print(ausgabe)           
