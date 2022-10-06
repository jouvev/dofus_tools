class GameActionFightCastRequestMessage:
   def __init__(self,input):
      self._spellIdFunc(input)
      self._cellIdFunc(input)
   
   def _spellIdFunc(self,input) :
      self.spellId = input.readVarUhShort()
      if(self.spellId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.spellId) + ") on element of GameActionFightCastRequestMessage.spellId.")
   
   def _cellIdFunc(self,input) :
      self.cellId = input.readShort()
      if(self.cellId < -1 or self.cellId > 559) :
         raise RuntimeError("Forbidden value (" + str(self.cellId) + ") on element of GameActionFightCastRequestMessage.cellId.")

   def resume(self):
      print("spellId :",self.spellId)
      print("cellId :",self.cellId)
