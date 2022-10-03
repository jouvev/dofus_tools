from tmp.messages.AbstractGameActionMessage import AbstractGameActionMessage
class GameActionFightLifePointsLostMessage(AbstractGameActionMessage):
   def __init__(self,input):
      super().__init__(input)
      self._targetIdFunc(input)
      self._lossFunc(input)
      self._permanentDamagesFunc(input)
      self._elementIdFunc(input)
   
   def _targetIdFunc(self,input) :
      self.targetId = input.readDouble()
      if(self.targetId < -9007199254740992 or self.targetId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.targetId + ") on element of GameActionFightLifePointsLostMessage.targetId.")
   
   def _lossFunc(self,input) :
      self.loss = input.readVarUhInt()
      if(self.loss < 0) :
         raise RuntimeError("Forbidden value (" + self.loss + ") on element of GameActionFightLifePointsLostMessage.loss.")
   
   def _permanentDamagesFunc(self,input) :
      self.permanentDamages = input.readVarUhInt()
      if(self.permanentDamages < 0) :
         raise RuntimeError("Forbidden value (" + self.permanentDamages + ") on element of GameActionFightLifePointsLostMessage.permanentDamages.")
   
   def _elementIdFunc(self,input) :
      self.elementId = input.readVarInt()