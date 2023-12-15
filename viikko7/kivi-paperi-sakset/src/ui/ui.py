from services.logiikka import Logiikka
from typing import Callable


class UI:
    def __init__(self, logiikka: Logiikka | None = None) -> None:
        self.__logiikka: Logiikka = logiikka or Logiikka()

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

            if vastaus in self.__pelit:
                print(
                    "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
                )

                self.__logiikka.aseta_peli(vastaus)
                self.__pelit[vastaus]()

            break

    def tulosta_ohje(self) -> None:
        print(self.__ohje)

    def kaynnista_kaksinpeli(self) -> None:
        try:
            while True:
                ekan_siirto = input("Ensimmäisen pelaajan siirto: ")
                tokan_siirto = input("Toisen pelaajan siirto: ")

                self.__logiikka.anna_pelaaja1().aseta_siirto(ekan_siirto)
                self.__logiikka.anna_pelaaja2().aseta_siirto(tokan_siirto)

                self.__logiikka.pelaa()

        except ValueError:
            print(self.__logiikka.hae_pelitulos())

    def kaynnista_yksinpeli(self) -> None:
        try:
            while True:
                pelaaja1 = self.__logiikka.anna_pelaaja1()
                tietokone = self.__logiikka.anna_pelaaja2()

                siirto = input(f"Pelaajan {pelaaja1.nimi} siirto: ")
                pelaaja1.aseta_siirto(siirto)

                siirrot = self.__logiikka.pelaa()

                print(f"Pelaajan {tietokone.nimi} siirto: {siirrot[1]}")

        except ValueError:
            print(self.__logiikka.hae_pelitulos())
