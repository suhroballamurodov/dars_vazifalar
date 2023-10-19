from chempionship import Chempionship

chempionship = Chempionship()


driver1 = chempionship.createDriver("Shumacher Andrech")
driver2 = chempionship.createDriver("Enzo Ferrari")
driver3 = chempionship.createDriver("Daniel Guber")


allDrivers = chempionship.getDrivers()
for driver in allDrivers:
    print(driver.getName())


driver = chempionship.getDriver("Enzo Ferrari")
if driver:
    print(driver.getName())
else:
    print("Driver not found")


grandPrix = chempionship.defineGrandPrix("London Grand Prix")
print(grandPrix.getName())


grandPrix = chempionship.getGrandPrix("London Grand Prix")
if grandPrix:
    print(grandPrix.getName())
else:
    print("Grand Prix not found")