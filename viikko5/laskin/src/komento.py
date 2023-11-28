from abc import ABC, abstractmethod
from typing import Callable

from sovelluslogiikka import Sovelluslogiikka


class Komento(ABC):
    def __init__(self, sovelluslogiikka: Sovelluslogiikka, lue_syote: Callable) -> None:
        self._logiikka: Sovelluslogiikka = sovelluslogiikka
        self._lue_syote: Callable = lue_syote

    @abstractmethod
    def suorita(self):
        pass


class Summa(Komento):
    def suorita(self) -> None:
        self._logiikka.arvo += self._lue_syote()


class Erotus(Komento):
    def suorita(self) -> None:
        self._logiikka.arvo -= self._lue_syote()


class Nollaus(Komento):
    def suorita(self) -> None:
        self._logiikka.arvo = 0
