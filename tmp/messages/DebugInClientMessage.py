class DebugInClientMessage:
   def __init__(self,input):
      self._levelFunc(input)
      self._messageFunc(input)
   
   def _levelFunc(self,input) :
      self.level = input.readByte()
      if(self.level < 0) :
         raise RuntimeError("Forbidden value (" + self.level + ") on element of DebugInClientMessage.level.")
   
   def _messageFunc(self,input) :
      self.message = input.readUTF()