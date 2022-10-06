class ObjectEffect:
   def __init__(self,input):
      self._actionIdFunc(input)
   
   def _actionIdFunc(self,input) :
      self.actionId = input.readVarUhShort()
      if(self.actionId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.actionId) + ") on element of ObjectEffect.actionId.")

   def resume(self):
      print("actionId :",self.actionId)
