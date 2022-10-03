class ForgettableSpellDeleteMessage:
   def __init__(self,input):
      self.spells = []
      _val2 = 0
      self._reasonFunc(input)
      _spellsLen = input.readUnsignedShort()
      for _i2 in range(0,_spellsLen):
         _val2 = input.readInt()
         if(_val2 < 0) :
            raise RuntimeError("Forbidden value (" + _val2 + ") on elements of spells.")
         self.spells.append(_val2)
   
   def _reasonFunc(self,input) :
      self.reason = input.readByte()
      if(self.reason < 0) :
         raise RuntimeError("Forbidden value (" + self.reason + ") on element of ForgettableSpellDeleteMessage.reason.")