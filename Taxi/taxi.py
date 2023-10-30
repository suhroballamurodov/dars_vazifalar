from driver import Taxi
from nosuch import InvalidTaxiName
from place import Place

from passanger import Passenger


class TaxiCompany:

    def __init__(self):
        self.bosh_driver_list = []
        self.available_taxis = []
        self.place_list = []

    def add_taxi(self, taxi_id):
        try:
            taxi = Taxi(taxi_id)
            self.available_taxis.append(taxi)
            print("Taxi qo'shildi")
        except InvalidTaxiName:
            print("Invalid taxi ID")
    
    def add_place(self, place:Place):
        self.place_list.append(place)
        return f" Sizning buyurtmangiz qabul qilindi tez orada haydovchimiz yetib boradi"
    
    def tostring_plase(self):
        return self.place_list

    def call_taxi(self, passenger):
        available_taxis = [taxi for taxi in self.available_taxis if taxi.is_available]
        if available_taxis:
            taxi = available_taxis[0]
            taxi.is_available = False
            return taxi
        else:
            return None


    def get_lost_trips(self):
        return self.lost_trips

    def getdriver(self):
        return self.driver_list
    
    def get_available(self):
        return self.available_taxis

