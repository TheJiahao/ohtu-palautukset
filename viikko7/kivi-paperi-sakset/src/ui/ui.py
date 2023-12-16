from services.kivi_paperi_sakset import KiviPaperiSakset
from typing import Callable


class UI:
    def __init__(self) -> None:
        self.__ohje: str = "\n".join(
            [
                "Valitse pelataanko",
                f"{'kaksinpeli:':15} Ihmistä vastaan",
                f"{'helppo:':15} Tekoälyä vastaan",
                f"{'vaikea:':15} Parannettua tekoälyä vastaan",
                "Muilla valinnoilla lopetetaan",
            ]
        )

        self.__pelit: dict[str, Callable] = {
            "kaksinpeli": self.kaynnista_kaksinpeli,
            "helppo": self.kaynnista_yksinpeli,
            "vaikea": self.kaynnista_yksinpeli,
        }

    def kaynnista(self) -> None:
        while True:
            self.tulosta_ohje()

            vastaus = input()

            try:
                self.__pelit[vastaus]()
            except KeyError:
                break

    def tulosta_ohje(self) -> None:
        print(self.__ohje)

    def kaynnista_kaksinpeli(self) -> None:
        peli = KiviPaperiSakset.luo_kaksinpeli()

        try:
            while True:
                ekan_siirto = input("Ensimmäisen pelaajan siirto: ")
                tokan_siirto = input("Toisen pelaajan siirto: ")

                peli.pelaaja1.aseta_siirto(ekan_siirto)
                peli.pelaaja2.aseta_siirto(tokan_siirto)

                peli.pelaa()

        except ValueError:
            print(peli.hae_pelitulos())

    def kaynnista_yksinpeli(self, vaikeus: str) -> None:
        peli = KiviPaperiSakset.luo_helppo_yksinpeli()

        if vaikeus == "vaikea":
            peli = KiviPaperiSakset.luo_vaikea_yksinpeli()

        try:
            while True:
                ekan_siirto = input("Ensimmäisen pelaajan siirto: ")
                tokan_siirto = input("Toisen pelaajan siirto: ")

                peli.pelaaja1.aseta_siirto(ekan_siirto)
                peli.pelaaja2.aseta_siirto(tokan_siirto)

                peli.pelaa()

        except ValueError:
            print(peli.hae_pelitulos())
