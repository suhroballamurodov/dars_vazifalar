class TimeForm:

    def __init__(self, hour, second, ms):
        self._hour = hour
        self._second = second
        self._ms = ms

        def __str__(self):
            return f'{self._hour} : {self._second} : {self._ms}'
        
        