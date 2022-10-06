import tmp.TypesFactory as pf
from tmp.types.GameRolePlayActorInformations import GameRolePlayActorInformations

class GameRolePlayGroupMonsterInformations(GameRolePlayActorInformations):
   def __init__(self,input):
      super().__init__(input)
      self.deserializeByteBoxes(input)
      _id1 = input.readUnsignedShort()
      self.staticInfos = pf.TypesFactory.get_instance_id(_id1,input)
      self._lootShareFunc(input)
      self._alignmentSideFunc(input)
   
   def deserializeByteBoxes(self,input) :
      _box0 = input.readByte()
      self.keyRingBonus = bool(bin(_box0)[2:].zfill(8)[0])
      self.hasHardcoreDrop = bool(bin(_box0)[2:].zfill(8)[1])
      self.hasAVARewardToken = bool(bin(_box0)[2:].zfill(8)[2])
   
   def _lootShareFunc(self,input) :
      self.lootShare = input.readByte()
      if(self.lootShare < -1 or self.lootShare > 8) :
         raise RuntimeError("Forbidden value (" + str(self.lootShare) + ") on element of GameRolePlayGroupMonsterInformations.lootShare.")
   
   def _alignmentSideFunc(self,input) :
      self.alignmentSide = input.readByte()

   def resume(self):
      super().resume()
      print("lootShare :",self.lootShare)
      print("alignmentSide :",self.alignmentSide)
