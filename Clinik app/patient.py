from person import Person

class Patient(Person):
    def __init__(self, ismi, familiyasi, ssn):
        super().__init__(ismi, familiyasi,ssn)