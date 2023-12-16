from entities.pelaajat.pelaaja import Pelaaja


class IhminenPelaaja(Pelaaja):
    def __init__(self) -> None:
        self.__siirto: str = "k"

    def anna_siirto(self) -> str:
        return self.__siirto

    def aseta_siirto(self, siirto: str) -> None:
        self.__siirto = siirto
