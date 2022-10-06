class ExchangeTypesExchangerDescriptionForUserMessage:
   def __init__(self,input):
      self.typeDescription = []
      _val2 = 0
      self._objectTypeFunc(input)
      _typeDescriptionLen = input.readUnsignedShort()
      for _i2 in range(0,_typeDescriptionLen):
         _val2 = input.readVarUhInt()
         if(_val2 < 0) :
            raise RuntimeError("Forbidden value (" + _val2 + ") on elements of typeDescription.")
         self.typeDescription.append(_val2)
   
   def _objectTypeFunc(self,input) :
      self.objectType = input.readInt()
      if(self.objectType < 0) :
         raise RuntimeError("Forbidden value (" + str(self.objectType) + ") on element of ExchangeTypesExchangerDescriptionForUserMessage.objectType.")

   def resume(self):
      print("objectType :",self.objectType)
      print("typeDescription :",self.typeDescription)
