from My_Beverage import Beverage
from My_Qator import Qator
from My_Card import Card


class VendingMachine:
    def __init(self):
        self.card_list:list[Card] = []
        self.qator_list = [Qator(i) for i in range(1, 5)]

    def add_beverage(self, qator, beverage: Beverage, number_beverage):
        qator = self.qator_list[qator-1]
        return qator.add_beverage(beverage, number_beverage)
    
    def info(self, qator):
        qator = self.qator_list[qator-1]
        return qator.get_info()
    
    def get_price(self, name):
        for qator in self.qator_list:
            check = qator.get_price(name)
            if check != None:
                return check
        return -1.0
    

    def recharge_card(self, id, debit):
        for card in self.card_list:
            if card._id == id:
                card.add_credit(debit)
                print(f"{id} id li kartaga {debit} so'm qo'shildi. Va hozirgi summa {card.credit} ga teng")
        card = Card(id, debit)
        self.card_list.append(card)
        print(f"Karta qo'shildi !")


    def getCredit(self, id):
        for card in self.card_list:
            nomalum = card.getCredit(id)
            if nomalum != id:
                return nomalum
        return -1.0
            # print("Kechirasiz bunaqa karta mavjud emas")