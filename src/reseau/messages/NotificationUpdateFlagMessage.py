class NotificationUpdateFlagMessage:
   def __init__(self,input):
      self._indexFunc(input)
   
   def _indexFunc(self,input) :
      self.index = input.readVarUhShort()
      if(self.index < 0) :
         raise RuntimeError("Forbidden value (" + str(self.index) + ") on element of NotificationUpdateFlagMessage.index.")

   def resume(self):
      print("index :",self.index)
