from manager import Manager
from client import Client
from flat import Flat


manager = Manager()

kvartira = Flat(0.01, '35 kv.m')
kvartira1 = Flat(0.02, '54 kv.m')
kvartira2 = Flat(0.03, '96 kv.m')
kvartira3 = Flat(0.04, '100 kv.m')

client = Client('Suhrob', 'Allamurodov', 0.41)
client1 = Client('Sardor', 'Allamurodov', 0.44)
client2 = Client('Behruz', 'Allamurodov', 0.58)
client3 = Client('Dilshod', 'Aminov', 0.78)

print(manager.newFlat(kvartira))
print(manager.newFlat(kvartira1))
print(manager.newFlat(kvartira2))
print(manager.newFlat(kvartira3))

print(manager.newClient(client))
print(manager.newClient(client1))
print(manager.newClient(client2))
print(manager.newClient(client3))

print(manager.getClient(0.41))

print(manager.getClients())