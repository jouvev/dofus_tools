from src.reseau.types.ObjectEffect import ObjectEffect

class ObjectEffectMinMax(ObjectEffect):
   def __init__(self,input):
      super().__init__(input)
      self._minFunc(input)
      self._maxFunc(input)
   
   def _minFunc(self,input) :
      self.min = input.readVarUhInt()
      if(self.min < 0) :
         raise RuntimeError("Forbidden value (" + str(self.min) + ") on element of ObjectEffectMinMax.min.")
   
   def _maxFunc(self,input) :
      self.max = input.readVarUhInt()
      if(self.max < 0) :
         raise RuntimeError("Forbidden value (" + str(self.max) + ") on element of ObjectEffectMinMax.max.")

   def resume(self):
      super().resume()
      print("min :",self.min)
      print("max :",self.max)
