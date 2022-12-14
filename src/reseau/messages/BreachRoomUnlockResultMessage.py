class BreachRoomUnlockResultMessage:
   def __init__(self,input):
      self._roomIdFunc(input)
      self._resultFunc(input)
   
   def _roomIdFunc(self,input) :
      self.roomId = input.readByte()
      if(self.roomId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.roomId) + ") on element of BreachRoomUnlockResultMessage.roomId.")
   
   def _resultFunc(self,input) :
      self.result = input.readByte()
      if(self.result < 0) :
         raise RuntimeError("Forbidden value (" + str(self.result) + ") on element of BreachRoomUnlockResultMessage.result.")

   def resume(self):
      print("roomId :",self.roomId)
      print("result :",self.result)
