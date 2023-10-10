from shkaf import Shkaf
from kitob import Kitob

class Qavat:

    def __init__(self, qavat) -> None:
        self._qavat = qavat
        self.shkaf_list: list[Shkaf] = [Shkaf("C1"+str(i)) for i in range(1, 31)]

    def qavat(self):
        return self._qavat

    def add(self, shkaf, javon, kitob: Kitob):
        for in_shkaf in self.shkaf_list:
            if in_shkaf.ind == shkaf:
                return in_shkaf.add(javon, kitob)
        return "bunday shkaf yo'q"

    def contain(self, shkaf, javon, kitob: Kitob):
        for in_shkaf in self.shkaf_list:
            if in_shkaf.ind == shkaf:
                return in_shkaf.contain(javon, kitob)
        return "bunday shkaf yo'q"