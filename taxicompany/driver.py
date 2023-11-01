from trip import Trip

class Taxi:
    def __init__(self, taxi_id):
        self.taxi_id = taxi_id
        self.is_available = True
        self.trips = []

    def __str__(self):
        return f"Taxi ID: {self.taxi_id}"

    def start_trip(self, destination):
        self.is_available = False
        self.trips.append(Trip(str(self), destination))

    def end_trip(self):
        self.is_available = True
