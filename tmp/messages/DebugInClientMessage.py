class DebugInClientMessage:
   def __init__(self,input):
      self._levelFunc(input)
      self._messageFunc(input)
   
   def _levelFunc(self,input) :
      self.level = input.readByte()
      if(self.level < 0) :
         raise RuntimeError("Forbidden value (" + str(self.level) + ") on element of DebugInClientMessage.level.")
   
   def _messageFunc(self,input) :
      self.message = input.readUTF()

   def resume(self):
      print("level :",self.level)
      print("message :",self.message)
