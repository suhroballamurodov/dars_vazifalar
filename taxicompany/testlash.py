# from driver import Taxi
from taxi import TaxiCompany
from place import Place
from passanger import Passenger


company = TaxiCompany()


place1 = Place("Toshkent shahri, Amir Temur ko'chasi", "Mirobod tumani", "Olmazor mahallasi")
place2 = Place("Toshkent shahri, Mustaqillik ko'chasi", "Yunusobod tumani", "Chilonzor mahallasi")
place3 = Place("Toshkent shahri, Navoiy ko'chasi", "Mirzo Ulug'bek tumani", "Chilanzar mahallasi")


company = TaxiCompany()


company.add_taxi("T001")
company.add_taxi("T002")
company.add_taxi("T003")


available_taxis = company.get_available()
print(available_taxis)


passenger1 = Passenger(place1)
passenger2 = Passenger(place2)
passenger3 = Passenger(place3)


taxi1 = company.call_taxi(passenger1)
taxi2 = company.call_taxi(passenger2)
taxi3 = company.call_taxi(passenger3)

print(taxi1)
print(taxi2)
print(taxi3)


taxi1.start_trip("Toshkent shahri,Qotortol ko'chasi")
taxi2.start_trip("Toshkent shahri, Amir Temur ko'chasi")
taxi3.start_trip("Toshkent shahri, Mustaqillik ko'chasi")

print(taxi1.is_available)  
print(taxi2.is_available)  
print(taxi3.is_available)  


taxi1.end_trip()
taxi2.end_trip()
taxi3.end_trip()

print(taxi1.is_available)  
print(taxi2.is_available)  
print(taxi3.is_available)  


trips1 = company.get_trips("T001")
trips2 = company.get_trips("T002")
trips3 = company.get_trips("T003")

print(trips1) 
print(trips2) 
print(trips3) 