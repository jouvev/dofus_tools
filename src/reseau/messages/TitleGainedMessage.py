class TitleGainedMessage:
   def __init__(self,input):
      self._titleIdFunc(input)
   
   def _titleIdFunc(self,input) :
      self.titleId = input.readVarUhShort()
      if(self.titleId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.titleId) + ") on element of TitleGainedMessage.titleId.")

   def resume(self):
      print("titleId :",self.titleId)
