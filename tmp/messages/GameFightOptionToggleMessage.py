class GameFightOptionToggleMessage:
   def __init__(self,input):
      self._optionFunc(input)
   
   def _optionFunc(self,input) :
      self.option = input.readByte()
      if(self.option < 0) :
         raise RuntimeError("Forbidden value (" + str(self.option) + ") on element of GameFightOptionToggleMessage.option.")

   def resume(self):
      print("option :",self.option)
