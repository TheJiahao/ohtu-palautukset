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
            "kaksinpeli": KiviPaperiSakset.luo_kaksinpeli,
            "helppo": KiviPaperiSakset.luo_helppo_yksinpeli,
            "vaikea": KiviPaperiSakset.luo_vaikea_yksinpeli,
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
        try:
            peli = self.__pelit[vaikeus]()
        except KeyError as exc:
            raise ValueError from exc

        try:
            while True:
                ekan_siirto = input("Ensimmäisen pelaajan siirto: ")
                peli.pelaaja1.aseta_siirto(ekan_siirto)

                if vaikeus == "kaksinpeli":
                    tokan_siirto = input("Toisen pelaajan siirto: ")
                    peli.pelaaja2.aseta_siirto(tokan_siirto)

                siirrot = peli.pelaa()

                if vaikeus != "kaksinpeli":
                    print(f"Tietokone pelasi: {siirrot[1]}")

        except ValueError:
            print(peli.hae_pelitulos())
