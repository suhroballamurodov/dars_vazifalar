from kitob import Kitob
from qavat import Qavat

class Kutubhona:
    def __init__(self) -> None:
        self.qavat_list: list[Qavat] = [Qavat(i) for i in range(1, 4)]

    def add(self, qavat, shkaf, javon, kitob: Kitob):
        qavat = self.qavat_list[qavat - 1]
        return qavat.add(shkaf, javon, kitob)

    def contain(self, qavat, shkaf, javon, kitob: Kitob):
        qavat = self.qavat_list[qavat - 1]
        return qavat.contain(shkaf, javon, kitob)