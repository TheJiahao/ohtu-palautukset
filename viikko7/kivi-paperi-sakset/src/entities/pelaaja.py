from abc import ABC, abstractmethod


class Pelaaja(ABC):
    @abstractmethod
    def pelaa(self) -> str:
        pass
