class CheckFileMessage:
   def __init__(self,input):
      self._filenameHashFunc(input)
      self._typeFunc(input)
      self._valueFunc(input)
   
   def _filenameHashFunc(self,input) :
      self.filenameHash = input.readUTF()
   
   def _typeFunc(self,input) :
      self.type = input.readByte()
      if(self.type < 0) :
         raise RuntimeError("Forbidden value (" + str(self.type) + ") on element of CheckFileMessage.type.")
   
   def _valueFunc(self,input) :
      self.value = input.readUTF()

   def resume(self):
      print("filenameHash :",self.filenameHash)
      print("type :",self.type)
      print("value :",self.value)
