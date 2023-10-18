class Card:
    def __init__(self, id: int, credit: int):
        self._id = id
        self._credit = credit


    def add_credit(self,value):
        self._credit += value
    

    @property
    def credit(self):
        return self._credit 
    
    