from tmp.types.ObjectEffect import ObjectEffect
class ObjectEffectString(ObjectEffect):
   def __init__(self,input):
      super().__init__(input)
      self._valueFunc(input)
   
   def _valueFunc(self,input) :
      self.value = input.readUTF()