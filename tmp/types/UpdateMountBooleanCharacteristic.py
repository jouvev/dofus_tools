from tmp.types.UpdateMountCharacteristic import UpdateMountCharacteristic

class UpdateMountBooleanCharacteristic(UpdateMountCharacteristic):
   def __init__(self,input):
      super().__init__(input)
      self._valueFunc(input)
   
   def _valueFunc(self,input) :
      self.value = input.readBoolean()

   def resume(self):
      super().resume()
      print("value :",self.value)
