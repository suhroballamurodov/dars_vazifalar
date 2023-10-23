class Person:
    def __init__(self, ismi, familiyasi, ssn):
        self._ismi = ismi
        self._familiya = familiyasi
        self._ssn = ssn


    @property
    def ismi(self):
        return self._ismi
    
    @property
    def familiyasi(self):
        return self._familiyasi
    
    @property
    def ssn(self):
        return self._ssn
    
    def __str__(self):
        return f"Bemor haqida to'liq ma'lumot ismi: {self._ismi}, familiyasi: {self._familiya} SSN raqami: {self._ssn}, "