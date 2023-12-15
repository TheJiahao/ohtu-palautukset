from abc import ABC, abstractmethod


class Tekoaly(ABC):
    @abstractmethod
    def anna_siirto(self) -> str:
        pass

    @abstractmethod
    def aseta_siirto(self, siirto: str) -> None:
        pass
