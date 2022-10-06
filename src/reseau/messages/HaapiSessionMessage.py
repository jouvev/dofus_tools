class HaapiSessionMessage:
   def __init__(self,input):
      self._keyFunc(input)
      self._typeFunc(input)
   
   def _keyFunc(self,input) :
      self.key = input.readUTF()
   
   def _typeFunc(self,input) :
      self.type = input.readByte()
      if(self.type < 0) :
         raise RuntimeError("Forbidden value (" + str(self.type) + ") on element of HaapiSessionMessage.type.")

   def resume(self):
      print("key :",self.key)
      print("type :",self.type)
