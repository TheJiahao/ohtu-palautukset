from entities.kivi_paperi_sakset import KiviPaperiSakset
from typing import Callable
from entities.pelaajat.pelaaja import Pelaaja


class Logiikka:
    def __init__(self) -> None:
        self.__pelimuodot: dict[str, Callable] = {
            "kaksinpeli": KiviPaperiSakset.luo_kaksinpeli,
            "helppo": KiviPaperiSakset.luo_helppo_yksinpeli,
            "vaikea": KiviPaperiSakset.luo_vaikea_yksinpeli,
        }

        self.__peli: KiviPaperiSakset = self.__pelimuodot["kaksinpeli"]()

    def aseta_peli(self, pelimuoto: str) -> None:
        self.__peli = self.__pelimuodot[pelimuoto]()

    def pelaa(self) -> tuple[str, str]:
        return self.__peli.pelaa()

    def anna_pelaaja1(self) -> Pelaaja:
        return self.__peli.pelaaja1

    def anna_pelaaja2(self) -> Pelaaja:
        return self.__peli.pelaaja2

    def hae_pelitulos(self) -> str:
        return str(self.__peli.__tuomari)
