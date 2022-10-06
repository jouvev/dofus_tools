class BreachRoomUnlockRequestMessage:
   def __init__(self,input):
      self._roomIdFunc(input)
   
   def _roomIdFunc(self,input) :
      self.roomId = input.readByte()
      if(self.roomId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.roomId) + ") on element of BreachRoomUnlockRequestMessage.roomId.")

   def resume(self):
      print("roomId :",self.roomId)
