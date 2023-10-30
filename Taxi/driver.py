
class Taxi:
    def __init__(self, taxi_id):
        self.taxi_id = taxi_id

    
    @property
    def id(self):
        return self.taxi_id
    
    def __str__(self):
        return f"Taxi ID: {self.taxi_id}"
