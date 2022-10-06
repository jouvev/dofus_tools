from tmp.messages.GameRolePlayDelayedActionMessage import GameRolePlayDelayedActionMessage

class GameRolePlayDelayedObjectUseMessage(GameRolePlayDelayedActionMessage):
   def __init__(self,input):
      super().__init__(input)
      self._objectGIDFunc(input)
   
   def _objectGIDFunc(self,input) :
      self.objectGID = input.readVarUhInt()
      if(self.objectGID < 0) :
         raise RuntimeError("Forbidden value (" + str(self.objectGID) + ") on element of GameRolePlayDelayedObjectUseMessage.objectGID.")

   def resume(self):
      super().resume()
      print("objectGID :",self.objectGID)
