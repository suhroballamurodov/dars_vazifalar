from person import Person
from doktor import Doktor
from patient import Patient
from nosuch import NoSuchDoctor, NoSuchPatient
  
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

    def get_patient(self, ssn):
        for patient in self.patient_list:
            if patient.ssn == ssn:
                return patient
        raise NoSuchPatient(ssn)


    def get_doktor(self, doctor_id):
        for doctor in self.doktor_list:
            if doctor.id == doctor_id:
                return doctor
        raise NoSuchDoctor(doctor_id)
    
    
    def assignpatient_to_doktor(self, patient_ssn, doktor_id):
        try:
            doctor = self.get_doktor(doktor_id)
        except:
            raise NoSuchDoctor(doktor_id)
        try:
            patient = self.get_patient(patient_ssn)
        except:
            raise NoSuchPatient(patient_ssn)
        doctor.add_patient(patient_ssn)
        patient.setdoktor(doktor_id)

    def idle_doktors(self): 
        idle_doktors = [] 
        for doktor in self.doktor_list:
            if len(doktor.get_patient()) == 0: 
                idle_doktors.append(doktor) 
        idle_doktors.sort(key=lambda x: (x.familiyasi(), x.ismi())) 
        return idle_doktors 
    
    def busy_doktors(self): 
        busy_doktors = [] 
        for doktor in self.doktor_list: 
            if len(doktor.get_patient()) > 0: 
                busy_doktors.append(doktor) 
        busy_doktors.sort(key=lambda x: (x.familiyasi(), x.ismi())) 
        return busy_doktors 
    
    def doctors_by_num_patients(self): 
        doktors = [] 
        for doktor in self.doktor_list: 
            doktors.append((len(doktor.get_patient()), doktor.id(), doktor.familiyasi(), doktor.ismi())) 
        doktors.sort(reverse=True) 
        doktors_str = [] 
        for doktor in doktors: 
            doktors_str.append(f"{doktor[0]}: {doktor[1]} {doktor[2]} {doktor[3]}") 
        return doktors_str 
 