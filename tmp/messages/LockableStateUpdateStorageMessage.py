from tmp.messages.LockableStateUpdateAbstractMessage import LockableStateUpdateAbstractMessage
class LockableStateUpdateStorageMessage(LockableStateUpdateAbstractMessage):
   def __init__(self,input):
      super().__init__(input)
      self._mapIdFunc(input)
      self._elementIdFunc(input)
   
   def _mapIdFunc(self,input) :
      self.mapId = input.readDouble()
      if(self.mapId < 0 or self.mapId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.mapId + ") on element of LockableStateUpdateStorageMessage.mapId.")
   
   def _elementIdFunc(self,input) :
      self.elementId = input.readVarUhInt()
      if(self.elementId < 0) :
         raise RuntimeError("Forbidden value (" + self.elementId + ") on element of LockableStateUpdateStorageMessage.elementId.")