from konto import Konto
class Girokonto(Konto):
    def __init__(self, konto_nummer, konto_inhaber, konto_stand, kreditlimit):
        super().__init(konto_nummer, konto_inhaber, konto_stand)
        self.kreditlimit = kreditlimit

    def ausgabe(self):
        print("Girokonto: {0} KontoInhaber: {1} Kontostand: {2}").format(self._konto_nummer, self._konto_inhaber, self._konto_stand)
        self.ausgabe_in_datei()
    
    def buchen(self,betrag):
        if betrag + self.get_konto_stand() +self.kreditlimit < 0:
            print("Kreditlimit erreicht")
        else:
            self._konto_stand += betrag

    def ausgabe_in_datei(self):
            with open("girokonto.txt","+a") as datei:
                datei.write("Girokonto: {0} KontoInhaber: {1} Kontostand: {2}\n".format(self._konto_nummer, self._konto_inhaber, self._konto_stand))


if __name__ == "__main__":
    g1 = Girokonto(5000,"Otto Gruber", 1000, 1000)
    g1.ausgabe()
    g1.buchen(1000)
    g1.ausgabe()
    g1.buchen(-3001)
    g1.ausgabe()