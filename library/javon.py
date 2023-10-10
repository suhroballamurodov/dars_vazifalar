from kitob import Kitob

class Javon:

    def __init__(self, number) -> None:
        self._number = number
        self.kitob_list: list[Kitob] = []

    @property
    def number(self):
        return self._number

    def add(self, kitob: Kitob):
        if len(self.kitob_list) < 10:
            self.kitob_list.append(kitob)
            return "kitob qo'shildi"
        return "javonda kitoblar yetarli"

    def contain(self, kitob: Kitob):
        for in_kitob in self.kitob_list:
            if in_kitob == kitob:
                return "qoyil ushbu kitob mavjud ekan"
        return "kechirasis bu kitob yo'q ekan"