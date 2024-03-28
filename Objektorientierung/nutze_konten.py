from girokonto import Girokonto
from sparkonto import Sparkonto
g1 = Girokonto(5000,"Anna Maier",2000,1000)
s1 = Sparkonto(1000,"Otto Walkes",500)
g1.ausgabe()
s1.ausgabe()