from abc import ABC, abstractmethod

from entities.pelaaja import Pelaaja
from entities.tuomari import Tuomari


class KiviPaperiSakset(ABC):
    def __init__(self, pelaaja1: Pelaaja, pelaaja2: Pelaaja) -> None:
        self._pelaaja1: Pelaaja = pelaaja1
        self._pelaaja2: Pelaaja = pelaaja2
        self._tuomari: Tuomari = Tuomari()

    @abstractmethod
    def pelaa(self) -> str:
        pass

    def _tarkista_siirto(self, siirto: str) -> bool:
        return siirto in {"k", "p", "s"}
