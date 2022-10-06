from tmp.messages.AbstractGameActionMessage import AbstractGameActionMessage

class GameActionFightDispellMessage(AbstractGameActionMessage):
   def __init__(self,input):
      super().__init__(input)
      self._targetIdFunc(input)
      self._verboseCastFunc(input)
   
   def _targetIdFunc(self,input) :
      self.targetId = input.readDouble()
      if(self.targetId < -9007199254740992 or self.targetId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.targetId) + ") on element of GameActionFightDispellMessage.targetId.")
   
   def _verboseCastFunc(self,input) :
      self.verboseCast = input.readBoolean()

   def resume(self):
      super().resume()
      print("targetId :",self.targetId)
      print("verboseCast :",self.verboseCast)
