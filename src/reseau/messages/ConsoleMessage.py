class ConsoleMessage:
   def __init__(self,input):
      self._typeFunc(input)
      self._contentFunc(input)
   
   def _typeFunc(self,input) :
      self.type = input.readByte()
      if(self.type < 0) :
         raise RuntimeError("Forbidden value (" + str(self.type) + ") on element of ConsoleMessage.type.")
   
   def _contentFunc(self,input) :
      self.content = input.readUTF()

   def resume(self):
      print("type :",self.type)
      print("content :",self.content)
