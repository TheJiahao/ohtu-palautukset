from services.kivi_paperi_sakset import KiviPaperiSakset
from typing import Callable


class UI:
    def __init__(self) -> None:
        self.__ohje: str = "\n".join(
            [
                "Valitse pelataanko",
                "(a) Ihmistä vastaan",
                "(b) Tekoälyä vastaan",
                "(c) Parannettua tekoälyä vastaan",
                "Muilla valinnoilla lopetetaan",
            ]
        )

        self.__pelit: dict[str, Callable] = {
            "a": KiviPaperiSakset.luo_kaksinpeli,
            "b": KiviPaperiSakset.luo_helppo_yksinpeli,
            "c": KiviPaperiSakset.luo_vaikea_yksinpeli,
        }

    def kaynnista(self) -> None:
        while True:
            self.__tulosta_ohje()

            vaikeus = input()

            try:
                self.__kaynnista_peli(vaikeus)
            except KeyError:
                return

    def __tulosta_ohje(self) -> None:
        print(self.__ohje)

    def __kaynnista_peli(self, vaikeus: str) -> None:
        peli = self.__pelit[vaikeus]()

        try:
            while True:
                ekan_siirto = input("Ensimmäisen pelaajan siirto: ")
                peli.pelaaja1.aseta_siirto(ekan_siirto)

                if vaikeus == "a":
                    tokan_siirto = input("Toisen pelaajan siirto: ")
                    peli.pelaaja2.aseta_siirto(tokan_siirto)

                siirrot = peli.pelaa()

                if vaikeus != "a":
                    print(f"Tietokone pelasi: {siirrot[1]}")

        except ValueError:
            print(peli.hae_pelitulos())
