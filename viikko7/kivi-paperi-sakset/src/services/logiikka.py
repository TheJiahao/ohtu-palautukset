from entities.kivi_paperi_sakset import KiviPaperiSakset
from typing import Callable


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

    def pelaa(self) -> None:
        self.__peli.pelaa()
