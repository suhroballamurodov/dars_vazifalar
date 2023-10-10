from javon import Javon
from kitob import Kitob

class Shkaf:

    def __init__(self, ind: str) -> None:
        self._ind = ind
        self.javon_list: list[Javon] = [Javon(i) for i in range(1, 7)]

    @property
    def ind(self):
        return self._ind

    def add(self, javon, kitob: Kitob):
        in_javon = self.javon_list[javon - 1]
        return in_javon.add(kitob)

    def contain(self, javon, kitob: Kitob):
        in_javon = self.javon_list[javon - 1]
        return in_javon.contain(kitob)

    # def __eq__(self, __o: object) -> bool:
    #     return self.

    

    # res = []
    # for i in range(1, 7):
    #     res.append(Javon(i))