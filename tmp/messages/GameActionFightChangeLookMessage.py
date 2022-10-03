from tmp.messages.AbstractGameActionMessage import AbstractGameActionMessage
from tmp.types.EntityLook import EntityLook
class GameActionFightChangeLookMessage(AbstractGameActionMessage):
   def __init__(self,input):
      super().__init__(input)
      self._targetIdFunc(input)
      self.entityLook = EntityLook(input)
   
   def _targetIdFunc(self,input) :
      self.targetId = input.readDouble()
      if(self.targetId < -9007199254740992 or self.targetId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.targetId + ") on element of GameActionFightChangeLookMessage.targetId.")