from driver import Driver

class GP:
    def __init__(self, name) -> None:
        self._name = name
        self._gp_list: list[Driver] = []
        self.results = []

    def add_driver(self, driver: Driver):
        self._gp_list.append(driver)
        print('gp ga driver qo\'shildi')

    @property
    def name(self):
        return self._name
    
    def __str__(self) -> str:
        return self.name