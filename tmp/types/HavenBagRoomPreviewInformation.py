class HavenBagRoomPreviewInformation:
   def __init__(self,input):
      self._roomIdFunc(input)
      self._themeIdFunc(input)
   
   def _roomIdFunc(self,input) :
      self.roomId = input.readUnsignedByte()
      if(self.roomId < 0 or self.roomId > 255) :
         raise RuntimeError("Forbidden value (" + self.roomId + ") on element of HavenBagRoomPreviewInformation.roomId.")
   
   def _themeIdFunc(self,input) :
      self.themeId = input.readByte()