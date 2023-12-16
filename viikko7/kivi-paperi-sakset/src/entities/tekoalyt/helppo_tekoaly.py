from entities.tekoalyt.tekoaly import Tekoaly


class HelppoTekoaly(Tekoaly):
    def __init__(self) -> None:
        self.__seuraava_siirto: int = 0
        self.__siirrot: list[str] = ["k", "p", "s"]

    def anna_siirto(self):
        self.__seuraava_siirto = (self.__seuraava_siirto + 1) % 3
        return self.__siirrot[self.__seuraava_siirto]

    def aseta_siirto(self, siirto: str) -> None:
        pass
