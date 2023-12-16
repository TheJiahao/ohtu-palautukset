from abc import ABC, abstractmethod


class Pelaaja(ABC):
    @abstractmethod
    def anna_siirto(self) -> str:
        pass

    def aseta_siirto(self, siirto: str) -> None:
        pass
