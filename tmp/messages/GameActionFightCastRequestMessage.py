class GameActionFightCastRequestMessage:
   def __init__(self,input):
      self._spellIdFunc(input)
      self._cellIdFunc(input)
   
   def _spellIdFunc(self,input) :
      self.spellId = input.readVarUhShort()
      if(self.spellId < 0) :
         raise RuntimeError("Forbidden value (" + self.spellId + ") on element of GameActionFightCastRequestMessage.spellId.")
   
   def _cellIdFunc(self,input) :
      self.cellId = input.readShort()
      if(self.cellId < -1 or self.cellId > 559) :
         raise RuntimeError("Forbidden value (" + self.cellId + ") on element of GameActionFightCastRequestMessage.cellId.")