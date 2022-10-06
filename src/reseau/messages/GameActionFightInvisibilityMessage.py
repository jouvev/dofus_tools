from src.reseau.messages.AbstractGameActionMessage import AbstractGameActionMessage

class GameActionFightInvisibilityMessage(AbstractGameActionMessage):
   def __init__(self,input):
      super().__init__(input)
      self._targetIdFunc(input)
      self._stateFunc(input)
   
   def _targetIdFunc(self,input) :
      self.targetId = input.readDouble()
      if(self.targetId < -9007199254740992 or self.targetId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.targetId) + ") on element of GameActionFightInvisibilityMessage.targetId.")
   
   def _stateFunc(self,input) :
      self.state = input.readByte()
      if(self.state < 0) :
         raise RuntimeError("Forbidden value (" + str(self.state) + ") on element of GameActionFightInvisibilityMessage.state.")

   def resume(self):
      super().resume()
      print("targetId :",self.targetId)
      print("state :",self.state)
