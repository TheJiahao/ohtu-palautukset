from abc import ABC, abstractmethod


class Pelaaja(ABC):
    def __init__(self, nimi: str) -> None:
        self.nimi: str = nimi

    @abstractmethod
    def anna_siirto(self) -> str:
        pass

    def aseta_siirto(self, siirto: str) -> None:
        pass
