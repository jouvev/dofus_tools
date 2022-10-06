class GameFightLeaveMessage:
   def __init__(self,input):
      self._charIdFunc(input)
   
   def _charIdFunc(self,input) :
      self.charId = input.readDouble()
      if(self.charId < -9007199254740992 or self.charId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.charId) + ") on element of GameFightLeaveMessage.charId.")

   def resume(self):
      print("charId :",self.charId)
