class UpdateMountCharacteristic:
   def __init__(self,input):
      self._typeFunc(input)
   
   def _typeFunc(self,input) :
      self.type = input.readByte()
      if(self.type < 0) :
         raise RuntimeError("Forbidden value (" + str(self.type) + ") on element of UpdateMountCharacteristic.type.")

   def resume(self):
      print("type :",self.type)
