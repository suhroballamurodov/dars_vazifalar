from nosuch import InvalidTaxiName
from driver import Taxi
class TaxiCompany: 
    def init(self): 
        self.taxis = [] 
 
    def addTaxi(self, taxi): 
        for existing_taxi in self.taxis: 
            if existing_taxi.id == taxi.id: 
                raise InvalidTaxiName("Taxi ID already exists") 
        self.taxis.append(taxi) 
 
    def getAvailable(self): 
        return [taxi for taxi in self.taxis if self.isTaxiAvailable(taxi)] 
 
    def isTaxiAvailable(self, taxi):
        pass 



class TaxiCompany:
    def __init__(self):
        self.taxis = []
        self.lost_trips = 0

    def add_taxi(self, taxi_id):
        if self._is_taxi_id_exists(taxi_id):
            raise InvalidTaxiName("Taxi ID already exists.")
        self.taxis.append(Taxi(taxi_id))

    def get_available(self):
        return [taxi for taxi in self.taxis if taxi.is_available]

    def call_taxi(self, passenger):
        available_taxis = self.get_available()
        if not available_taxis:
            return None
        taxi = available_taxis[0]
        taxi.start_trip(passenger.get_place())
        return taxi

    def get_lost_trips(self):
        return self.lost_trips

    def get_trips(self, taxi_id):
        taxi = self._get_taxi_by_id(taxi_id)
        if not taxi:
            raise InvalidTaxiName("Invalid Taxi ID.")
        return taxi.trips

    def _is_taxi_id_exists(self, taxi_id):
        return any(taxi.taxi_id == taxi_id for taxi in self.taxis)

    def _get_taxi_by_id(self, taxi_id):
        for taxi in self.taxis:
            if taxi.taxi_id == taxi_id:
                return taxi
        return None