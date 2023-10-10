class Kitob:

    def __init__(self, muallifi: str, nomi: str) -> None:
        self._muallifi = muallifi
        self._nomi = nomi

    @property
    def muallifi(self):
        return self._muallifi

    @property
    def nomi(self):
        return self._nomi

    def to_string(self):
        return self._muallifi + ", " + self._nomi

    def __eq__(self, __o: object) -> bool:
        return self.nomi == __o.nomi and self.muallifi == __o.muallifi