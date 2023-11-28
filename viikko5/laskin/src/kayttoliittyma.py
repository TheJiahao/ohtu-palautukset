from enum import Enum
from tkinter import StringVar, constants, ttk

from komento import Erotus, Nollaus, Summa
from komento import Komento as Komento_luokka
from sovelluslogiikka import Sovelluslogiikka


class Komento(Enum):
    SUMMA = 1
    EROTUS = 2
    NOLLAUS = 3
    KUMOA = 4


class Kayttoliittyma:
    def __init__(self, sovellus: Sovelluslogiikka, root):
        self._logiikka: Sovelluslogiikka = sovellus
        self._root = root

        self._komennot: dict[Komento, Komento_luokka] = {
            Komento.SUMMA: Summa(self._logiikka, self._lue_syote),
            Komento.EROTUS: Erotus(self._logiikka, self._lue_syote),
            Komento.NOLLAUS: Nollaus(self._logiikka, self._lue_syote),
        }

        self._alusta()

    def _alusta(self):
        self._arvo_var = StringVar()
        self._arvo_var.set(str(self._logiikka.arvo))
        self._syote_kentta = ttk.Entry(master=self._root)

        tulos_teksti = ttk.Label(textvariable=self._arvo_var)

        summa_painike = ttk.Button(
            master=self._root,
            text="Summa",
            command=lambda: self._suorita_komento(Komento.SUMMA),
        )

        erotus_painike = ttk.Button(
            master=self._root,
            text="Erotus",
            command=lambda: self._suorita_komento(Komento.EROTUS),
        )

        self._nollaus_painike = ttk.Button(
            master=self._root,
            text="Nollaus",
            state=constants.DISABLED,
            command=lambda: self._suorita_komento(Komento.NOLLAUS),
        )

        self._kumoa_painike = ttk.Button(
            master=self._root,
            text="Kumoa",
            state=constants.DISABLED,
            command=lambda: self._suorita_komento(Komento.KUMOA),
        )

        tulos_teksti.grid(columnspan=4)
        self._syote_kentta.grid(columnspan=4, sticky=(constants.E, constants.W))
        summa_painike.grid(row=2, column=0)
        erotus_painike.grid(row=2, column=1)
        self._nollaus_painike.grid(row=2, column=2)
        self._kumoa_painike.grid(row=2, column=3)

    def kaynnista(self):
        self._kumoa_painike["state"] = constants.NORMAL

        if self._logiikka.arvo == 0:
            self._nollaus_painike["state"] = constants.DISABLED
        else:
            self._nollaus_painike["state"] = constants.NORMAL

        self._syote_kentta.delete(0, constants.END)
        self._arvo_var.set(str(self._logiikka.arvo))

    def _suorita_komento(self, komento):
        komento_olio = self._komennot[komento]

        if komento == Komento.KUMOA:
            komento_olio.kumoa()
        else:
            komento_olio.suorita()

            self._komennot[Komento.KUMOA] = komento_olio
            self._kumoa_painike["state"] = constants.NORMAL

        if self._logiikka.arvo == 0:
            self._nollaus_painike["state"] = constants.DISABLED
        else:
            self._nollaus_painike["state"] = constants.NORMAL

        self._syote_kentta.delete(0, constants.END)
        self._arvo_var.set(str(self._logiikka.arvo))

    def _lue_syote(self) -> int:
        return int(self._syote_kentta.get())
