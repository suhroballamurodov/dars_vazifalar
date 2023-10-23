from person import Person
from doktor import Doktor
from patient import Patient


class Clinic:
    def __init__(self):
        self.patient_list:list[Patient] = []
        self.doktor_list:list[Doktor] = []

    def add_patient(self, patient:Patient):
        self.patient_list.append(patient)
        return f'Bemor bazaga kiritildi'


    def add_doktor(self, doktor:Doktor):
        self.doktor_list.append(doktor)
        return f'Doktor bazaga kiritildi'

    def get_patient(self,patient:Patient, ssn:str):
        for patient in self.patient_list:
            if patient.ssn != ssn:
                return f" No Such Patient "
            else:
                return patient
        return None

    def get_doktor(self,doktor_id):
        for doktor in self.doktor_list:
            if doktor.id != doktor_id:
                return f" No Such Doktor "
            else:
                return doktor
        return None
