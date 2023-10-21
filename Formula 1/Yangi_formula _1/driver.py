
class Driver:
    def __init__(self, name) -> None:
        self._name = name
        self.grand_pri_nomi = []
        self._points = 0

    @property
    def name(self):
        return self._name
    
    
    def get_raced(self):
        return self.grand_pri_nomi
    
    def get_points(self):
        return self.points
    
    def __str__(self) -> str:
        return self.name