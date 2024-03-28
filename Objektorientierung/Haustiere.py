class Pets:
    name = "Haustiere"
    @classmethod
    def ausgabe(cls):   #cls wegen der classmethod; (cls ist veränderbar, kann auch otto heisen)
        print("In dieser Klasse geht es um {} ".format(cls.name))

class Dogs(Pets):
    name = "Hunde"

class Cats(Pets):
    name = "Katzen"

p = Pets()
p.ausgabe()
d = Dogs()
d.ausgabe()
c = Cats()
c.ausgabe()
