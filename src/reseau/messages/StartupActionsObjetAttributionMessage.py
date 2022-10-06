class StartupActionsObjetAttributionMessage:
   def __init__(self,input):
      self._actionIdFunc(input)
      self._characterIdFunc(input)
   
   def _actionIdFunc(self,input) :
      self.actionId = input.readInt()
      if(self.actionId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.actionId) + ") on element of StartupActionsObjetAttributionMessage.actionId.")
   
   def _characterIdFunc(self,input) :
      self.characterId = input.readVarUhLong()
      if(self.characterId < 0 or self.characterId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.characterId) + ") on element of StartupActionsObjetAttributionMessage.characterId.")

   def resume(self):
      print("actionId :",self.actionId)
      print("characterId :",self.characterId)
