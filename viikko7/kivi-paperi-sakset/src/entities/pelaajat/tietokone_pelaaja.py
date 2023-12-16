from entities.pelaajat.pelaaja import Pelaaja
from entities.tekoalyt.tekoaly import Tekoaly


class TietokonePelaaja(Pelaaja):
    def __init__(self, tekoaly: Tekoaly) -> None:
        self.__tekoaly: Tekoaly = tekoaly

    def anna_siirto(self) -> str:
        return self.__tekoaly.anna_siirto()

    def aseta_siirto(self, siirto: str) -> None:
        self.__tekoaly.aseta_siirto(siirto)
