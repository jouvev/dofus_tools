class ExchangeWeightMessage:
   def __init__(self,input):
      self._currentWeightFunc(input)
      self._maxWeightFunc(input)
   
   def _currentWeightFunc(self,input) :
      self.currentWeight = input.readVarUhInt()
      if(self.currentWeight < 0) :
         raise RuntimeError("Forbidden value (" + str(self.currentWeight) + ") on element of ExchangeWeightMessage.currentWeight.")
   
   def _maxWeightFunc(self,input) :
      self.maxWeight = input.readVarUhInt()
      if(self.maxWeight < 0) :
         raise RuntimeError("Forbidden value (" + str(self.maxWeight) + ") on element of ExchangeWeightMessage.maxWeight.")

   def resume(self):
      print("currentWeight :",self.currentWeight)
      print("maxWeight :",self.maxWeight)
