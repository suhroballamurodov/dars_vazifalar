class VendingMachine:
    
    ''' Ichimlik sotuvchi mashina '''
    def __init__(self, nomi: str, sotish_narxi: int, soni: int):
        ''' Ichimlik xususiyatlari '''
        self.nomi = nomi
        self.sotish_narxi = sotish_narxi
        # self.soni = 0
        # self.ichimliklar = []

    def nomi(self):
        return self._nomi
    
    def sotish_narxi(self):
        return self._sotish_narxi

    def soni(self):
        return self.soni

    def set_soni(self, soni):
        self.soni = soni


    # def addBeverage(self):
    #     ''' Yangi ichimlik qo'shish '''
    #     self.soni += 1

    def get_info(self):
        return (f"{self.nomi} ichimligi {self.sotish_narxi} so'm turadi, Sotuv mashinada {self.soni} ta qolgan")
    
    def getPrise(self):
        return (f"{self.nomi} ichimligi {self.sotish_narxi} so'm turadi")

    


ichimlik = VendingMachine("Coca Cola", 3200, 1)
print(ichimlik.get_info())

ichimlik1 = VendingMachine("Suv", 1000, 5)
print(ichimlik1.get_info())

ichimlik2 = VendingMachine("Pepsi", 2500, 3)
print(ichimlik2.get_info())

