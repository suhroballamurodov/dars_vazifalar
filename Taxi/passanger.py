from place import Place


class Passenger:
    def __init__(self, place):
        self._current_place = place

    def get_place(self):
        return self.current_place