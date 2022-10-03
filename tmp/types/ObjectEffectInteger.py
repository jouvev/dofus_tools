from tmp.types.ObjectEffect import ObjectEffect
class ObjectEffectInteger(ObjectEffect):
   def __init__(self,input):
      super().__init__(input)
      self._valueFunc(input)
   
   def _valueFunc(self,input) :
      self.value = input.readVarUhInt()
      if(self.value < 0) :
         raise RuntimeError("Forbidden value (" + self.value + ") on element of ObjectEffectInteger.value.")