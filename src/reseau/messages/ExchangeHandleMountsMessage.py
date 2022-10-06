class ExchangeHandleMountsMessage:
   def __init__(self,input):
      self.ridesId = []
      _val2 = 0
      self._actionTypeFunc(input)
      _ridesIdLen = input.readUnsignedShort()
      for _i2 in range(0,_ridesIdLen):
         _val2 = input.readVarUhInt()
         if(_val2 < 0) :
            raise RuntimeError("Forbidden value (" + _val2 + ") on elements of ridesId.")
         self.ridesId.append(_val2)
   
   def _actionTypeFunc(self,input) :
      self.actionType = input.readByte()

   def resume(self):
      print("actionType :",self.actionType)
      print("ridesId :",self.ridesId)
