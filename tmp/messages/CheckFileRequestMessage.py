class CheckFileRequestMessage:
   def __init__(self,input):
      self._filenameFunc(input)
      self._typeFunc(input)
   
   def _filenameFunc(self,input) :
      self.filename = input.readUTF()
   
   def _typeFunc(self,input) :
      self.type = input.readByte()
      if(self.type < 0) :
         raise RuntimeError("Forbidden value (" + str(self.type) + ") on element of CheckFileRequestMessage.type.")

   def resume(self):
      print("filename :",self.filename)
      print("type :",self.type)
