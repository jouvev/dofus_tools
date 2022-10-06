from src.reseau.types.HavenBagRoomPreviewInformation import HavenBagRoomPreviewInformation

class HavenBagRoomUpdateMessage:
   def __init__(self,input):
      self.roomsPreview = []
      _item2 = None
      self._actionFunc(input)
      _roomsPreviewLen = input.readUnsignedShort()
      for _i2 in range(0,_roomsPreviewLen):
         _item2 = HavenBagRoomPreviewInformation(input)
         self.roomsPreview.append(_item2)
   
   def _actionFunc(self,input) :
      self.action = input.readByte()
      if(self.action < 0) :
         raise RuntimeError("Forbidden value (" + str(self.action) + ") on element of HavenBagRoomUpdateMessage.action.")

   def resume(self):
      print("action :",self.action)
      for e in self.roomsPreview:
         e.resume()
