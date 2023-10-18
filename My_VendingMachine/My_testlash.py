from My_Vendingmachine import VendingMachine
from My_Beverage import Beverage


my_machine = VendingMachine()

cola = Beverage('Cola', 3200)
suv = Beverage('Suv', 1000)
pepsi = Beverage('Pepsi', 2500)

print(my_machine.add_beverage(1, cola, 1))


print(my_machine.info(3))
print(my_machine.get_price('fanta'))


my_machine.recharge_card(12, 12000)
my_machine.recharge_card(21, 5600)
my_machine.recharge_card(99, 15800)

# my_machine.getCredit(6, 19900)
