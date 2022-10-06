class DungeonKeyRingUpdateMessage:
   def __init__(self,input):
      self._dungeonIdFunc(input)
      self._availableFunc(input)
   
   def _dungeonIdFunc(self,input) :
      self.dungeonId = input.readVarUhShort()
      if(self.dungeonId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.dungeonId) + ") on element of DungeonKeyRingUpdateMessage.dungeonId.")
   
   def _availableFunc(self,input) :
      self.available = input.readBoolean()

   def resume(self):
      print("dungeonId :",self.dungeonId)
      print("available :",self.available)
