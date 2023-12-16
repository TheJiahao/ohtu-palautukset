from entities.tekoalyt.tekoaly import Tekoaly
from collections import deque


# "Muistava tekoäly"
class TekoalyParannettu(Tekoaly):
    def __init__(self, muistin_koko: int) -> None:
        self._muisti = deque(maxlen=muistin_koko)
        self.__muistin_koko: int = muistin_koko
        self._vapaa_muisti_indeksi = 0
        self.__frekvenssit: dict[str, int] = {"k": 0, "p": 0, "s": 0}
        self.__voittavat_siirrot: dict[str, str] = {"k": "p", "p": "s", "s": "k"}

    def aseta_siirto(self, siirto: str) -> None:
        if len(self._muisti) >= self.__muistin_koko:
            poistettava = self._muisti[-1]
            self.__frekvenssit[poistettava] -= 1

        poistettava = self._muisti[-1]

        self.__frekvenssit[siirto] += 1
        self.__frekvenssit[poistettava] -= 1

        self._muisti.append(siirto)

    def anna_siirto(self):
        if self._vapaa_muisti_indeksi == 0 or self._vapaa_muisti_indeksi == 1:
            return "k"

        viimeisin_siirto = self._muisti[self._vapaa_muisti_indeksi - 1]

        k = 0
        p = 0
        s = 0

        for i in range(0, self._vapaa_muisti_indeksi - 1):
            if viimeisin_siirto == self._muisti[i]:
                seuraava = self._muisti[i + 1]

                if seuraava == "k":
                    k = k + 1
                elif seuraava == "p":
                    p = p + 1
                else:
                    s = s + 1

        # Tehdään siirron valinta esimerkiksi seuraavasti;
        # - jos kiviä eniten, annetaan aina paperi
        # - jos papereita eniten, annetaan aina sakset
        # muulloin annetaan aina kivi
        if k > p or k > s:
            return "p"
        elif p > k or p > s:
            return "s"
        else:
            return "k"

        # Tehokkaampiakin tapoja löytyy, mutta niistä lisää
        # Johdatus Tekoälyyn kurssilla!
