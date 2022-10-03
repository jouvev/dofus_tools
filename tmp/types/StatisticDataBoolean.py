from tmp.types.StatisticData import StatisticData
class StatisticDataBoolean(StatisticData):
   def __init__(self,input):
      super().__init__(input)
      self._valueFunc(input)
   
   def _valueFunc(self,input) :
      self.value = input.readBoolean()