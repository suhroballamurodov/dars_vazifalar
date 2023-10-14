class Beverage:
    
    ''' Ichimlik sotuvchi mashina '''
    def __init__(self, nomi: str, sotish_narxi: int, soni: int):
        ''' Ichimlik xususiyatlari '''
        self._nomi = nomi
        self._sotish_narxi = sotish_narxi
        # self.soni = 0
        # self.ichimliklar = []
    @property
    def nomi(self):
       return self._nomi
    
    @nomi.setter
    def name(self,value):
        self._name = value


    def sotish_narxi(self):
        return self._sotish_narxi

    @name.setter
    def sotish_narxi(self,value):
        self._sotish_narxi = value




#     def soni(self):
#         return self.soni

#     def set_soni(self, soni):
#         self.soni = soni



class VendingMachine:
    def __init__(self) -> None:
        self.qator_list = []

    def add_Beverage(qator,beverage: Beverage):
        ''' Yangi ichimlik qo'shish '''
        self.soni += 1

#     def get_info(self):
#         return (f"{self.nomi} ichimligi {self.sotish_narxi} so'm turadi, Sotuv mashinada {self.soni} ta qolgan")
    
#     def getPrise(self):
#         return (f"{self.nomi} ichimligi {self.sotish_narxi} so'm turadi")

    


# ichimlik = VendingMachine("Coca Cola", 3200, 1)
# print(ichimlik.get_info())

# ichimlik1 = VendingMachine("Suv", 1000, 5)
# print(ichimlik1.get_info())

# ichimlik2 = VendingMachine("Pepsi", 2500, 3)
# print(ichimlik2.get_info())









#tolov kartalar 
class Tolov_kartalar:

    def __init__(self, card_id: int, credit: int):
        self.card_id = card_id
        self.credit = credit
        self.card = 0
        self.card = []

    def card_id(self):
        return self.card_id
    
    def getCredit(self):
        return self.credit
    
    def rechargeCard(self, credit):
        if self.car_id == card_id:
            return 
        self.credit += credit 

        
    # def getCredit(self):
    #     return 
    

card1 = Tolov_kartalar(12, 12000)
card2 = Tolov_kartalar(21,5600)
card3 = Tolov_kartalar(99,15800)
        
print(card1.getCard())









