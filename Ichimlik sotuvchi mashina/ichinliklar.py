from uyga_vazifa import VendingMachine


class Ichimliklar:

    def __init__(self, nomi) -> None:
        self.nomi = nomi 
        self.ichimliklar_soni = 0
        self.ichimliklar = []

    def addBeverage(self, ichimlik):
        self.ichimliklar.append(ichimlik)
        self.ichimliklar_soni += 1







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