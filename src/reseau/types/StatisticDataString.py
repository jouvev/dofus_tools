from src.reseau.types.StatisticData import StatisticData

class StatisticDataString(StatisticData):
   def __init__(self,input):
      super().__init__(input)
      self._valueFunc(input)
   
   def _valueFunc(self,input) :
      self.value = input.readUTF()

   def resume(self):
      super().resume()
      print("value :",self.value)
