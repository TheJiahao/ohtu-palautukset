# Luokka pitää kirjaa ensimmäisen ja toisen pelaajan pisteistä sekä tasapelien määrästä.
class Tuomari:
    def __init__(self) -> None:
        self.__ekan_pisteet = 0
        self.__tokan_pisteet = 0
        self.__tasapelit = 0

        self.__voittavat_siirrot: dict[str, str] = {"k": "p", "p": "s", "s": "k"}

    def kirjaa_siirto(self, ekan_siirto: str, tokan_siirto: str) -> None:
        if self._tasapeli(ekan_siirto, tokan_siirto):
            self.__tasapelit = self.__tasapelit + 1
        elif self._eka_voittaa(ekan_siirto, tokan_siirto):
            self.__ekan_pisteet += 1
        else:
            self.__tokan_pisteet += 1

    def __str__(self) -> str:
        return "\n".join(
            [
                f"Pelitilanne: {self.__ekan_pisteet} - {self.__tokan_pisteet}",
                f"Tasapelit: {self.__tasapelit}",
            ]
        )

    # sisäinen metodi, jolla tarkastetaan tuliko tasapeli
    def _tasapeli(self, eka, toka):
        return eka == toka

    # sisäinen metodi joka tarkastaa voittaako eka pelaaja tokan
    def _eka_voittaa(self, eka: str, toka: str) -> bool:
        return self.__voittavat_siirrot[eka] == toka
