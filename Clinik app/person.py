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
    
    def setdoktor(self, doctor):
        self._doktor = doctor

    def __str__(self):
        return f" SSN raqami: {self._ssn} "