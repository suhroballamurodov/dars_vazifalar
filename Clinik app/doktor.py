from person import Person

class Doktor(Person):
    def __init__(self, ismi, familiyasi, ssn, mutaxassisligi, id:int):
        super().__init__(ismi, familiyasi,ssn)
        self._mutaxassisligi = mutaxassisligi
        self._id = id
        self._patient_list: list[Person] = []

    @property
    def get_mutaxassisligi(self):
        return self._mutaxassisligi
    
    @property
    def id(self):
        return self._id
    
    def __str__(self):
        return f"Doktor haqida to'liq ma'lumot ismi: {self._ismi}, familiyasi: {self._familiya}, SSN raqami: {self._ssn}, idsi: {self._id}, mutaxasssisligi: {self._mutaxassisligi} "
    
    def add_patient(self, patient):
        self._patient_list.append(patient)
        print(f' {self._id} id doctorga patient biriktirildi')
