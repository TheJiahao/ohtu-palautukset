KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko) -> list[int]:
        return [0] * koko

    def __siirra_vasemmalle(self, indeksi: int) -> None:
        for j in range(indeksi, self.__alkioiden_lkm - 1):
            self.__luvut[j] = self.__luvut[j + 1]

        self.__alkioiden_lkm = self.__alkioiden_lkm - 1

    def __kasvata_listaa(self) -> None:
        uusi_lista = self._luo_lista(self.__alkioiden_lkm + self.__kasvatuskoko)
        self.kopioi_lista(self.__luvut, uusi_lista)
        self.__luvut = uusi_lista

    def __init__(
        self, kapasiteetti: int = KAPASITEETTI, kasvatuskoko: int = OLETUSKASVATUS
    ) -> None:
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
            self.__kasvata_listaa()

    def poista(self, poistettava) -> None:
        if not self.kuuluu(poistettava):
            return

        indeksi = self.__luvut[0 : self.__alkioiden_lkm].index(poistettava)
        self.__siirra_vasemmalle(indeksi)

    def kopioi_lista(self, vanha, uusi) -> None:
        for i in range(0, len(vanha)):
            uusi[i] = vanha[i]

    def mahtavuus(self):
        return self.__alkioiden_lkm

    def to_int_list(self) -> list[int]:
        return self.__luvut[0 : self.__alkioiden_lkm]

    @staticmethod
    def muunna_int_joukoksi(joukko: set[int]) -> "IntJoukko":
        tulos = IntJoukko()

        for alkio in joukko:
            tulos.lisaa(alkio)

        return tulos

    @staticmethod
    def yhdiste(a: "IntJoukko", b: "IntJoukko") -> "IntJoukko":
        yhdiste = set.union(set(a.to_int_list()), set(b.to_int_list()))
        return IntJoukko.muunna_int_joukoksi(yhdiste)

    @staticmethod
    def leikkaus(a: "IntJoukko", b: "IntJoukko") -> "IntJoukko":
        leikkaus = set.intersection(set(a.to_int_list()), set(b.to_int_list()))
        return IntJoukko.muunna_int_joukoksi(leikkaus)

    @staticmethod
    def erotus(a: "IntJoukko", b: "IntJoukko") -> "IntJoukko":
        erotus = set(a.to_int_list()).difference(set(b.to_int_list()))
        return IntJoukko.muunna_int_joukoksi(erotus)

    def __str__(self) -> str:
        if self.__alkioiden_lkm == 0:
            return "{}"

        return str(set(self.__luvut[0 : self.__alkioiden_lkm]))
