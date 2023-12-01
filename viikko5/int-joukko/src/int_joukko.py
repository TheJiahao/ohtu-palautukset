KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko) -> list[int]:
        return [0] * koko

    def __init__(
        self, kapasiteetti: int = KAPASITEETTI, kasvatuskoko: int = OLETUSKASVATUS
    ):
        if kapasiteetti < 0 or kasvatuskoko < 0:
            raise ValueError("Virheellinen kapasiteetti tai kasvatuskoko")

        self.__kapasiteetti: int = kapasiteetti
        self.__kasvatuskoko: int = kasvatuskoko
        self.__luvut = self._luo_lista(self.__kapasiteetti)
        self.__alkioiden_lkm = 0

    def kuuluu(self, luku) -> bool:
        return luku in self.__luvut[0 : self.__alkioiden_lkm]

    def lisaa(self, luku) -> None:
        if self.kuuluu(luku):
            return

        self.__luvut[self.__alkioiden_lkm] = luku
        self.__alkioiden_lkm += 1

        if self.__alkioiden_lkm == len(self.__luvut) - 1:
            uusi_lista = self._luo_lista(self.__alkioiden_lkm + self.__kasvatuskoko)
            self.kopioi_lista(self.__luvut, uusi_lista)
            self.__luvut = uusi_lista

    def poista(self, n):
        kohta = -1
        apu = 0

        for i in range(0, self.__alkioiden_lkm):
            if n == self.__luvut[i]:
                kohta = i  # siis luku löytyy tuosta kohdasta :D
                self.__luvut[kohta] = 0
                break

        if kohta != -1:
            for j in range(kohta, self.__alkioiden_lkm - 1):
                apu = self.__luvut[j]
                self.__luvut[j] = self.__luvut[j + 1]
                self.__luvut[j + 1] = apu

            self.__alkioiden_lkm = self.__alkioiden_lkm - 1
            return True

        return False

    def kopioi_lista(self, vanha, uusi):
        for i in range(0, len(vanha)):
            uusi[i] = vanha[i]

    def mahtavuus(self):
        return self.__alkioiden_lkm

    def to_int_list(self) -> list[int]:
        taulu = self._luo_lista(self.__alkioiden_lkm)

        for i in range(0, len(taulu)):
            taulu[i] = self.__luvut[i]

        return taulu

    @staticmethod
    def yhdiste(a: "IntJoukko", b: "IntJoukko"):
        tulos = IntJoukko()
        yhdiste = a.to_int_list()
        yhdiste.extend(b.to_int_list())

        for alkio in yhdiste:
            tulos.lisaa(alkio)

        return tulos

    @staticmethod
    def leikkaus(a, b):
        tulos = IntJoukko()
        a_taulu = a.to_int_list()
        b_joukko = set(b.to_int_list())

        for alkio in a_taulu:
            if alkio in b_joukko:
                tulos.lisaa(alkio)

        return tulos

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            z.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            z.poista(b_taulu[i])

        return z

    def __str__(self):
        if self.__alkioiden_lkm == 0:
            return "{}"
        elif self.__alkioiden_lkm == 1:
            return "{" + str(self.__luvut[0]) + "}"
        else:
            tuotos = "{"
            for i in range(0, self.__alkioiden_lkm - 1):
                tuotos = tuotos + str(self.__luvut[i])
                tuotos = tuotos + ", "
            tuotos = tuotos + str(self.__luvut[self.__alkioiden_lkm - 1])
            tuotos = tuotos + "}"
            return tuotos
