#tolov kartalar 
class Tolov_kartalar:

    def __init__(self, card_id: int, credit: int):
        self.card_id = card_id
        self.credit = credit
        self.card = 0
        self.card = []

    def card_id(self):
        return self.card_id
    
    def credit(self):
        return self.credit

    def getCredit(self):
        if self.card_id == 0:
            return -1
        else:
            return (f"Idsi {self.card_id} ga teng bo'lgan kartada {self.credit} dollor pul bor")
    
    def rechargeCard(self, credit):
        if self.car_id == card_id:
            self.credit += credit

    

card1 = Tolov_kartalar(12, 12000)
card2 = Tolov_kartalar(21,5600)
card3 = Tolov_kartalar(99,15800)
card4 = Tolov_kartalar(0,10000)
        
print(card1.getCredit())
print(card2.getCredit())
print(card3.getCredit())
print(card4.getCredit()) #bunda -1 chiqishi kerak shart bo'yicha