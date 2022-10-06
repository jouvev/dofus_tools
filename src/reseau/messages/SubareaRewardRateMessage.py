class SubareaRewardRateMessage:
   def __init__(self,input):
      self._subAreaRateFunc(input)
   
   def _subAreaRateFunc(self,input) :
      self.subAreaRate = input.readVarShort()

   def resume(self):
      print("subAreaRate :",self.subAreaRate)
