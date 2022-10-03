class TitlesAndOrnamentsListMessage:
   def __init__(self,input):
      self.titles = []
      self.ornaments = []
      _val1 = 0
      _val2 = 0
      _titlesLen = input.readUnsignedShort()
      for _i1 in range(0,_titlesLen):
         _val1 = input.readVarUhShort()
         if(_val1 < 0) :
            raise RuntimeError("Forbidden value (" + _val1 + ") on elements of titles.")
         self.titles.append(_val1)
      _ornamentsLen = input.readUnsignedShort()
      for _i2 in range(0,_ornamentsLen):
         _val2 = input.readVarUhShort()
         if(_val2 < 0) :
            raise RuntimeError("Forbidden value (" + _val2 + ") on elements of ornaments.")
         self.ornaments.append(_val2)
      self._activeTitleFunc(input)
      self._activeOrnamentFunc(input)
   
   def _activeTitleFunc(self,input) :
      self.activeTitle = input.readVarUhShort()
      if(self.activeTitle < 0) :
         raise RuntimeError("Forbidden value (" + self.activeTitle + ") on element of TitlesAndOrnamentsListMessage.activeTitle.")
   
   def _activeOrnamentFunc(self,input) :
      self.activeOrnament = input.readVarUhShort()
      if(self.activeOrnament < 0) :
         raise RuntimeError("Forbidden value (" + self.activeOrnament + ") on element of TitlesAndOrnamentsListMessage.activeOrnament.")