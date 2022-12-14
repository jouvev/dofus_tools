class HavenBagDailyLoteryMessage:
   def __init__(self,input):
      self._returnTypeFunc(input)
      self._gameActionIdFunc(input)
   
   def _returnTypeFunc(self,input) :
      self.returnType = input.readByte()
      if(self.returnType < 0) :
         raise RuntimeError("Forbidden value (" + str(self.returnType) + ") on element of HavenBagDailyLoteryMessage.returnType.")
   
   def _gameActionIdFunc(self,input) :
      self.gameActionId = input.readUTF()

   def resume(self):
      print("returnType :",self.returnType)
      print("gameActionId :",self.gameActionId)
