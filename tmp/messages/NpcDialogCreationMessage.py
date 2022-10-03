class NpcDialogCreationMessage:
   def __init__(self,input):
      self._mapIdFunc(input)
      self._npcIdFunc(input)
   
   def _mapIdFunc(self,input) :
      self.mapId = input.readDouble()
      if(self.mapId < 0 or self.mapId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.mapId + ") on element of NpcDialogCreationMessage.mapId.")
   
   def _npcIdFunc(self,input) :
      self.npcId = input.readInt()