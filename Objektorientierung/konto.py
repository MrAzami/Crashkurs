from abc import ABC, abstractmethod

class Konto(ABC):
    def __init__(self, konto_nummer, konto_inhaber, konto_stand):
        self._konto_nummer = konto_nummer
        self._konto_inhaber = konto_inhaber
        self._konto_stand = konto_stand

    @abstractmethod
    def buchen(self,betrag):
        pass
    @abstractmethod
    def ausgabe(self):
        pass
    @abstractmethod
    def ausgabe_in_datei(self):
        pass
    @abstractmethod
    def get_konto_stand(self):
        return self._konto_stand