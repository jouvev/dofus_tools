from src.reseau.messages.AbstractGameActionMessage import AbstractGameActionMessage

class GameActionFightDodgePointLossMessage(AbstractGameActionMessage):
   def __init__(self,input):
      super().__init__(input)
      self._targetIdFunc(input)
      self._amountFunc(input)
   
   def _targetIdFunc(self,input) :
      self.targetId = input.readDouble()
      if(self.targetId < -9007199254740992 or self.targetId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.targetId) + ") on element of GameActionFightDodgePointLossMessage.targetId.")
   
   def _amountFunc(self,input) :
      self.amount = input.readVarUhShort()
      if(self.amount < 0) :
         raise RuntimeError("Forbidden value (" + str(self.amount) + ") on element of GameActionFightDodgePointLossMessage.amount.")

   def resume(self):
      super().resume()
      print("targetId :",self.targetId)
      print("amount :",self.amount)
