from kitob import Kitob
from kutubhona import Kutubhona

lib = Kutubhona()

kitob1 = Kitob("Tohir Mlik", "Odamiylik mulki")
kitob2 = Kitob("Tohir Mlik", "Odamiylik")

print(lib.add(1, "C2", 1, kitob1))
print(lib.contain(1, "C2", 1, kitob1))
print(lib.contain(1, "C2", 1, kitob2))

