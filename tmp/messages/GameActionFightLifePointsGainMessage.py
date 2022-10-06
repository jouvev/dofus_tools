from tmp.messages.AbstractGameActionMessage import AbstractGameActionMessage

class GameActionFightLifePointsGainMessage(AbstractGameActionMessage):
   def __init__(self,input):
      super().__init__(input)
      self._targetIdFunc(input)
      self._deltaFunc(input)
   
   def _targetIdFunc(self,input) :
      self.targetId = input.readDouble()
      if(self.targetId < -9007199254740992 or self.targetId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.targetId) + ") on element of GameActionFightLifePointsGainMessage.targetId.")
   
   def _deltaFunc(self,input) :
      self.delta = input.readVarUhInt()
      if(self.delta < 0) :
         raise RuntimeError("Forbidden value (" + str(self.delta) + ") on element of GameActionFightLifePointsGainMessage.delta.")

   def resume(self):
      super().resume()
      print("targetId :",self.targetId)
      print("delta :",self.delta)
