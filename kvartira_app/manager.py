from flat import Flat
from client import Client


class Manager:
    
    def __init__(self):
        self.flats_list: list [Flat] = []
        self.clients_list: list [Client] = []



    def newFlat(self,flat:Flat):
        self.flats_list.append(flat)
        return ("Yangi kvartira bazaga qo'shildi")
        
    

    def newClient(self, client:Client):
        self.clients_list.append(client)
        return ("Yangi mijoz bazaga qo'shildi")
        

    def getClient(self,id):
        for client in self.clients_list:
            if client.getID == id:
                return client
        return None
            

    def getClients(self):
        return self.clients_list
            
        