from src.reseau.types.UpdateMountCharacteristic import UpdateMountCharacteristic

class UpdateMountIntegerCharacteristic(UpdateMountCharacteristic):
   def __init__(self,input):
      super().__init__(input)
      self._valueFunc(input)
   
   def _valueFunc(self,input) :
      self.value = input.readInt()

   def resume(self):
      super().resume()
      print("value :",self.value)
