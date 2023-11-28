from abc import ABC, abstractmethod
from typing import Callable

from sovelluslogiikka import Sovelluslogiikka


class Komento(ABC):
    def __init__(self, sovelluslogiikka: Sovelluslogiikka, lue_syote: Callable) -> None:
        self._logiikka: Sovelluslogiikka = sovelluslogiikka
        self._lue_syote: Callable = lue_syote
        self._edellinen_arvo: int = sovelluslogiikka.arvo

    @abstractmethod
    def suorita(self) -> None:
        self._edellinen_arvo = self._logiikka.arvo

    def kumoa(self) -> None:
        self._logiikka.arvo = self._edellinen_arvo


class Summa(Komento):
    def suorita(self) -> None:
        super().suorita()
        self._logiikka.arvo += self._lue_syote()


class Erotus(Komento):
    def suorita(self) -> None:
        super().suorita()
        self._logiikka.arvo -= self._lue_syote()


class Nollaus(Komento):
    def suorita(self) -> None:
        super().suorita()
        self._logiikka.arvo = 0
