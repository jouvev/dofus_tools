from tmp.messages.AbstractGameActionMessage import AbstractGameActionMessage

class GameActionFightReflectSpellMessage(AbstractGameActionMessage):
   def __init__(self,input):
      super().__init__(input)
      self._targetIdFunc(input)
   
   def _targetIdFunc(self,input) :
      self.targetId = input.readDouble()
      if(self.targetId < -9007199254740992 or self.targetId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.targetId) + ") on element of GameActionFightReflectSpellMessage.targetId.")

   def resume(self):
      super().resume()
      print("targetId :",self.targetId)
