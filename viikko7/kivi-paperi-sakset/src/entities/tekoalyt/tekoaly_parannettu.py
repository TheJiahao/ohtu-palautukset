from entities.tekoalyt.tekoaly import Tekoaly
from collections import deque


# "Muistava tekoäly"
class TekoalyParannettu(Tekoaly):
    def __init__(self, muistin_koko: int) -> None:
        self._muisti = deque(maxlen=muistin_koko)
        self.__haviavat_siirrot: dict[str, str] = {"k": "p", "p": "s", "s": "k"}

    def aseta_siirto(self, siirto: str) -> None:
        self._muisti.append(siirto)

    def anna_siirto(self) -> str:
        if len(self._muisti) <= 2:
            return "k"

        yleisin_siirto = self.__hae_yleisin_siirto(self._muisti[-1])

        return self.__haviavat_siirrot[yleisin_siirto]

    def __hae_yleisin_siirto(self, viimeisin_siirto: str) -> str:
        frekvenssit = {"k": 0, "p": 0, "s": 0}
        edellinen = self._muisti[0]

        for i, siirto in enumerate(self._muisti):
            if i == 0:
                continue

            if edellinen == viimeisin_siirto:
                frekvenssit[siirto] += 1

            edellinen = siirto

        return max(frekvenssit.keys(), key=lambda x: frekvenssit[x])
