from konto import Konto
class Sparkonto(Konto):
    def __init__(self,konto_nummer,konto_inhaber,konto_stand):
        super().__init__(konto_nummer, konto_inhaber, konto_stand)

    def ausgabe(self):
        print("Sparbuch: {0} KontoInhaber: {1} Kontostand: {2}".format(self._konto_nummer, self._konto_inhaber, self._konto_stand))
        self.ausgabe_in_datei()
    
    def buchen(self, betrag):
        if betrag + self.get_konto_stand() < 0:
            print("Sparkonto darf nicht überzogen werden!")
        else:
            self._konto_stand += betrag
        
    def ausgabe_in_datei(self):
        with open("sparkonto.txt","+a")as datei:
            datei.write("Sparbuch: {0} KontoInhaber: {1} Kontostand: {2}\n".format(self._konto_nummer, self._konto_inhaber, self._konto_stand))

if __name__ == "__main__":
    s1 = Sparkonto(1000,"Eva Maier", 500)


    # s1.ausgabe()
    # s1.buchen(-200)
    # s1.ausgabe()
    # s1.buchen(-400)
    # s1.ausgabe()