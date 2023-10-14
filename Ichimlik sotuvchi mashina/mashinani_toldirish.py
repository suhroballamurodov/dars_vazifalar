
class Mashinani_toldirish:

    def __init__(self, ustun_raqami: int, ichimlik_nomi: str, soni: int):
        self.ustun_raqami = ustun_raqami
        # for i in self.ustun_raqami(1,5,1):
        #     return i
        self.ichimlik_nomi = ichimlik_nomi
        self.soni = soni
    

    
    # def ustunni_oshirish(self, ustun_raqami):
    #     self.ustun_raqami = ustun_raqami

    # def update_ustunni_oshirish(self):
    #     self.ustun_raqami +=1
    #     return self.ustun_raqami
        ''' Bu kod xatolik berdi !'''



    def avialableCans(self):
        return (f"Siz ichishni xohlagan {self.ichimlik_nomi} ichimligi {self.ustun_raqami}-ustunda joylashgan va mashinamizda {self.soni} ta qolgan")



ichimlik1 = Mashinani_toldirish(1,'Coca Cola', 1)
ichimlik2 = Mashinani_toldirish(2,'Suv', 10)
ichimlik3 = Mashinani_toldirish(3,'Pepsi', 15)
ichimlik4 = Mashinani_toldirish(4, 'Suv', 20)


print(ichimlik1.avialableCans())
print(ichimlik2.avialableCans())
print(ichimlik3.avialableCans())
print(ichimlik4.avialableCans())



# print(ichimlik1.update_ustunni_oshirish())