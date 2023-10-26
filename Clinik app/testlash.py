from clinik import Clinic
from patient import Patient
from doktor import Doktor
from person import Person

clinik = Clinic()

patient1 = Patient('Ali', 'Valiyev', 'ssn001')
patient2 = Patient('Bekmirza', 'Jahonov', 'ssn002')
patient3 = Patient('Shokir', 'Hoshimov','ssn003')


doktor1 = Doktor('Suhrob', 'Allamurodov', 'ssn018', 'Nevrolog', 00.41)
doktor2 = Doktor('Sardor', 'Allamurodov', 'ssn021','Xirurg', 00.42)
doktor3 = Doktor('Behruz', 'Allamurodov','ssn0024', "Ko'z jarrohlik", 00.43)

print(clinik.add_patient(patient1))
print(clinik.add_patient(patient2))
print(clinik.add_patient(patient3))


print(clinik.add_doktor(doktor1))
print(clinik.add_doktor(doktor2))
print(clinik.add_doktor(doktor3))

print(clinik.get_patient(patient1))
print(clinik.get_patient(patient2))             #bu yerda ssn ni tanimayapti ishlamadi
print(clinik.get_patient(patient3))


print(clinik.get_doktor(00.41))
print(clinik.get_doktor(00.42))
print(clinik.get_doktor(00.43))

print(clinik.assignpatient_to_doktor('ssn001', 00.41))

# print(clinik.idle_doktors([doktor2]))

# print(clinik.busy_doktors([doktor1]))