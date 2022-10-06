from src.reseau.types.StatisticData import StatisticData

class StatisticDataByte(StatisticData):
   def __init__(self,input):
      super().__init__(input)
      self._valueFunc(input)
   
   def _valueFunc(self,input) :
      self.value = input.readByte()

   def resume(self):
      super().resume()
      print("value :",self.value)
