from driver import Driver 
from grandprix import GrandPrix
from timeform import TimeForm



class Time:

    def __init__(self, gp:GrandPrix, driver: Driver, tugash_vaqti:TimeForm) -> None:
            self._gp = gp
            self._driver = driver
            self._tugash_vaqti = tugash_vaqti