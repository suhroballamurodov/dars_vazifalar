from driver import Driver
from gp import GP
from timeform import TimeForm

class Time:
    def __init__(self, gp: GP, driver: Driver, tugash_vaqti: TimeForm) -> None:
        self._gp = gp
        self._driver = driver
        self._tugash_vaqti = tugash_vaqti
        self.position = None

        gp.results.append((driver, tugash_vaqti))    

    def __str__(self) -> str:
        a = self._tugash_vaqti
        return a.to_string()
    

    def get_position(self):
        return self.position