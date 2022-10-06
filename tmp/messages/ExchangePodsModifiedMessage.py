from tmp.messages.ExchangeObjectMessage import ExchangeObjectMessage

class ExchangePodsModifiedMessage(ExchangeObjectMessage):
   def __init__(self,input):
      super().__init__(input)
      self._currentWeightFunc(input)
      self._maxWeightFunc(input)
   
   def _currentWeightFunc(self,input) :
      self.currentWeight = input.readVarUhInt()
      if(self.currentWeight < 0) :
         raise RuntimeError("Forbidden value (" + str(self.currentWeight) + ") on element of ExchangePodsModifiedMessage.currentWeight.")
   
   def _maxWeightFunc(self,input) :
      self.maxWeight = input.readVarUhInt()
      if(self.maxWeight < 0) :
         raise RuntimeError("Forbidden value (" + str(self.maxWeight) + ") on element of ExchangePodsModifiedMessage.maxWeight.")

   def resume(self):
      super().resume()
      print("currentWeight :",self.currentWeight)
      print("maxWeight :",self.maxWeight)
