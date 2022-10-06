from tmp.messages.ExchangeStartOkCraftMessage import ExchangeStartOkCraftMessage

class ExchangeStartOkCraftWithInformationMessage(ExchangeStartOkCraftMessage):
   def __init__(self,input):
      super().__init__(input)
      self._skillIdFunc(input)
   
   def _skillIdFunc(self,input) :
      self.skillId = input.readVarUhInt()
      if(self.skillId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.skillId) + ") on element of ExchangeStartOkCraftWithInformationMessage.skillId.")

   def resume(self):
      super().resume()
      print("skillId :",self.skillId)
