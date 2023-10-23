from clinik import Clinic
from patient import Patient
from doktor import Doktor
from person import Person

clinik = Clinic()

patient1 = Patient('Ali', 'Valiyev', 'ssn001')
patient2 = Patient('Bekmirza', 'Jahonov', 'ssn002')


doktor1 = Doktor('Suhrob', 'Allamurodov', 'ssn018', 'Nevrolog', 00.41)
doktor2 = Doktor('Sardor', 'Allamurodov', 'ssn021','Xirurg', 00.42)


print(clinik.add_patient(patient1))
print(clinik.add_patient(patient2))


print(clinik.add_doktor(doktor1))
print(clinik.add_doktor(doktor2))


print(clinik.get_patient(patient1, 'ssn001'))
print(clinik.get_patient(patient2, 'ssn002'))             #bu yerda ssn ni tanimayapti ishlamadi


print(clinik.get_doktor(00.41))
print(clinik.get_doktor(00.42))