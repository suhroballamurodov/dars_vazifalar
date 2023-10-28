class Flat:

      def __init__(self, code: int, maydon:str):
            self._code = code
            self._maydon = maydon
            self.tariffs = []

      @property
      def getCode(self):
          return self.code
    
      @property
      def getDimention(self):
          return self.maydon
    
      def setTariffs(self, tariflar):
          self.tariffs = tariflar

      def getTriffs(self):
           return self.tariffs