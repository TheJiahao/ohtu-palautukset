from entities.pelaajat.pelaaja import Pelaaja
from entities.tuomari import Tuomari
from entities.pelaajat.ihminen_pelaaja import IhminenPelaaja

class KiviPaperiSakset:
    def __init__(self, pelaaja1: Pelaaja, pelaaja2: Pelaaja) -> None:
        self._pelaaja1: Pelaaja = pelaaja1
        self._pelaaja2: Pelaaja = pelaaja2
        self._tuomari: Tuomari = Tuomari()

    def pelaa(self) -> str:
        siirto1 = self._pelaaja1.anna_siirto()
        siirto2 = self._pelaaja2.anna_siirto()

        while self._tarkista_siirto(siirto1) and self._tarkista_siirto(siirto2):
            self._tuomari.kirjaa_siirto(siirto1, siirto2)

            self._pelaaja1.aseta_siirto(siirto2)
            self._pelaaja2.aseta_siirto(siirto1)

        return str(self._tuomari)

    def _tarkista_siirto(self, siirto: str) -> bool:
        return siirto in {"k", "p", "s"}

    @staticmethod
    def luo_kaksinpeli() -> "KiviPaperiSakset":
        return KiviPaperiSakset(IhminenPelaaja("Pelaaja1"), IhminenPelaaja("Pelaaja2"))
