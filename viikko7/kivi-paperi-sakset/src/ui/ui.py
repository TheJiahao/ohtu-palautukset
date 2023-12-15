from services.logiikka import Logiikka


class UI:
    def __init__(self, logiikka: Logiikka | None = None) -> None:
        self.__logiikka: Logiikka = logiikka or Logiikka()

    def kaynnista() -> None:
        while True:
            print(
                "Valitse pelataanko"
                "\n (a) Ihmistä vastaan"
                "\n (b) Tekoälyä vastaan"
                "\n (c) Parannettua tekoälyä vastaan"
                "\nMuilla valinnoilla lopetetaan"
            )

            vastaus = input()

            if vastaus.endswith("a"):
                print(
                    "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
                )

                kaksinpeli = KPSPelaajaVsPelaaja()
                kaksinpeli.pelaa()
            elif vastaus.endswith("b"):
                print(
                    "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
                )

                yksinpeli = KPSTekoaly()
                yksinpeli.pelaa()
            elif vastaus.endswith("c"):
                print(
                    "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
                )

                haastava_yksinpeli = KPSParempiTekoaly()
                haastava_yksinpeli.pelaa()
            else:
                break
