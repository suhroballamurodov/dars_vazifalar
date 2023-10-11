from kitob import Kitob



class Javon:
    def __init__(self, id: int)-> None:
        self.id = id
        kitoblar_list: list[Kitob] = []

    def contain(self, kitob: Kitob):
        for i in self.kitoblar_list:
            if in_kitob==kitob.muallifi and in_kitob==kitob.nomi
            return kitob
        return None
    
    def add(self, kitob: Kitob):
        if len(self.kitob_list) < 10:
            self.kitoblar_list.append(kitob)
            return "Kitob qo'shildi"
        else:
            return "Kitob qo'shilmadi"