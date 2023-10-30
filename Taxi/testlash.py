from driver import Taxi
from taxi import TaxiCompany
from place import Place

company = TaxiCompany()

company.add_taxi("T001")
company.add_taxi("T002")
company.add_taxi("T003")

available_taxis = company.get_available()
for taxi in available_taxis:
    print(taxi)


plase1 = Place('Toshkent', 'Chilonzor', 'Oqtosh') 

print(company.add_place(plase1))