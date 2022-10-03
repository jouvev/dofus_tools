from tmp.messages.ObtainedItemMessage import ObtainedItemMessage
class ObtainedItemWithBonusMessage(ObtainedItemMessage):
   def __init__(self,input):
      super().__init__(input)
      self._bonusQuantityFunc(input)
   
   def _bonusQuantityFunc(self,input) :
      self.bonusQuantity = input.readVarUhInt()
      if(self.bonusQuantity < 0) :
         raise RuntimeError("Forbidden value (" + self.bonusQuantity + ") on element of ObtainedItemWithBonusMessage.bonusQuantity.")