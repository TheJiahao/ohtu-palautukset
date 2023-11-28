class Sovelluslogiikka:
    def __init__(self, arvo: int = 0):
        self._arvo: int = arvo

    @property
    def arvo(self):
        return self._arvo

    @arvo.setter
    def arvo(self, arvo):
        self._arvo = arvo
