class MapFightCountMessage:
   def __init__(self,input):
      self._fightCountFunc(input)
   
   def _fightCountFunc(self,input) :
      self.fightCount = input.readVarUhShort()
      if(self.fightCount < 0) :
         raise RuntimeError("Forbidden value (" + self.fightCount + ") on element of MapFightCountMessage.fightCount.")