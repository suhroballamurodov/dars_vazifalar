from driver import Driver
from grandprix import GrandPrix

class Chempionship:
    ''' Dastlab bo'sh list yaratib uning ichiga append yordamida driver va grandprix larni qo'shib ketadi'''
    def __init__(self):
        self.drivers = []
        self.grandPrixList = []


    def createDriver(self, name):
        ''' Yangi driverlarni yaratib ularni listga yozib ketadi'''
        driver = Driver(name)
        self.drivers.append(driver)
        return driver


    def getDrivers(self):
        '''Driverlarni ismini qaytarish uchun funksiya'''
        return self.drivers


    def getDriver(self, name):
        for driver in self.drivers:
            if driver.getName() == name:
                return driver
        return None


    def defineGrandPrix(self, name):
        grandPrix = GrandPrix(name)
        self.grandPrixList.append(grandPrix)
        return grandPrix

    def getGrandPrix(self, name):
        for grandPrix in self.grandPrixList:
            if grandPrix.getName() == name:
                return grandPrix
        return None

