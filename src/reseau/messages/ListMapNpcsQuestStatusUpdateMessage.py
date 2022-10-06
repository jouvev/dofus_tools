from src.reseau.types.MapNpcQuestInfo import MapNpcQuestInfo

class ListMapNpcsQuestStatusUpdateMessage:
   def __init__(self,input):
      self.mapInfo = []
      _item1 = None
      _mapInfoLen = input.readUnsignedShort()
      for _i1 in range(0,_mapInfoLen):
         _item1 = MapNpcQuestInfo(input)
         self.mapInfo.append(_item1)

   def resume(self):
      for e in self.mapInfo:
         e.resume()
