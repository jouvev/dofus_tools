from src.reseau.types.GameRolePlayNpcQuestFlag import GameRolePlayNpcQuestFlag

class MapNpcQuestInfo:
   def __init__(self,input):
      self.npcsIdsWithQuest = []
      self.questFlags = []
      _val2 = 0
      _item3 = None
      self._mapIdFunc(input)
      _npcsIdsWithQuestLen = input.readUnsignedShort()
      for _i2 in range(0,_npcsIdsWithQuestLen):
         _val2 = input.readInt()
         self.npcsIdsWithQuest.append(_val2)
      _questFlagsLen = input.readUnsignedShort()
      for _i3 in range(0,_questFlagsLen):
         _item3 = GameRolePlayNpcQuestFlag(input)
         self.questFlags.append(_item3)
   
   def _mapIdFunc(self,input) :
      self.mapId = input.readDouble()
      if(self.mapId < 0 or self.mapId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.mapId) + ") on element of MapNpcQuestInfo.mapId.")

   def resume(self):
      print("mapId :",self.mapId)
      print("npcsIdsWithQuest :",self.npcsIdsWithQuest)
      for e in self.questFlags:
         e.resume()
