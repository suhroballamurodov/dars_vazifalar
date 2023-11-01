from taxi import TaxiCompany

class TaxiManager: 
    def __init__(self, taxi_company): 
        self.taxi_company = taxi_company 
        self.lost_trips = 0 
 
    def callTaxi(self, passenger): 
        available_taxis = self.taxi_company.getAvailable()
        if len(available_taxis) == 0: 
            print("Bosh taksi yo'qligi sabab buyurtma qabul qilinmadi. Noqulaylik uchun kechirasiz!") 
            self.lost_trips += 1 
            return None 
        else: 
            taxi = available_taxis[0]
            return taxi 
 
    def getLostTrips(self): 
        return self.lost_trips 