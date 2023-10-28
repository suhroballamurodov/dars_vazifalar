class Client:

    def __init__(self, name, surname, id):
        self._name = name
        self._surname = surname
        self._id = id

    @property
    def getName(self):
        return self.name
    

    @property
    def getSurname(self):
        return self.surname
    
    @property
    def getID(self):
        return self._id
    
    def __str__(self):
        return f"Client haqida to'liq ma'lumot ismi: {self._name}, familiyasi: {self._surname}, idsi: {self._id}"
    