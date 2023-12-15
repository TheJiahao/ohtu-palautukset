from abc import ABC, abstractmethod


class Pelaaja(ABC):
    def __init__(self, nimi: str) -> str:
        self.nimi: str = nimi

    @abstractmethod
    def anna_siirto(self) -> str:
        pass
