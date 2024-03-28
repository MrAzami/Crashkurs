#Abstracte Klasse, muss min eine abstracte methode enthalten
#Abstract methode = eine nicht programmierte methode
#Kind Klasse wird gezwungen dies zu tun
from abc import ABC, abstractmethod
class Konto(ABC):
    @abstractmethod
    def buchen(self,betrag):
        pass
    def ausgabe(self):
        print("Ausgabe aus Konto")
class Sparkonto(Konto):
    def buchen(self,betrag):
        print("Es wird gebucht ",betrag)

s = Sparkonto()
s.buchen(500)