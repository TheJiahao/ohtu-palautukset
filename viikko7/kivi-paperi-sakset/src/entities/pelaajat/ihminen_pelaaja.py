from entities.pelaajat.pelaaja import Pelaaja

class IhminenPelaaja(Pelaaja):
    def anna_siirto(self) -> str:
        return input(f"Syötä pelaajan {self.nimi} siirto: ")
