import src.reseau.TypesFactory as pf
from src.reseau.types.FightOptionsInformations import FightOptionsInformations

class FightCommonInformations:
   def __init__(self,input):
      self.fightTeams = []
      self.fightTeamsPositions = []
      self.fightTeamsOptions = []
      _id3 = 0
      _item3 = None
      _val4 = 0
      _item5 = None
      self._fightIdFunc(input)
      self._fightTypeFunc(input)
      _fightTeamsLen = input.readUnsignedShort()
      for _i3 in range(0,_fightTeamsLen):
         _id3 = input.readUnsignedShort()
         _item3 = pf.TypesFactory.get_instance_id(_id3,input)
         self.fightTeams.append(_item3)
      _fightTeamsPositionsLen = input.readUnsignedShort()
      for _i4 in range(0,_fightTeamsPositionsLen):
         _val4 = input.readVarUhShort()
         if(_val4 < 0 or _val4 > 559) :
            raise RuntimeError("Forbidden value (" + _val4 + ") on elements of fightTeamsPositions.")
         self.fightTeamsPositions.append(_val4)
      _fightTeamsOptionsLen = input.readUnsignedShort()
      for _i5 in range(0,_fightTeamsOptionsLen):
         _item5 = FightOptionsInformations(input)
         self.fightTeamsOptions.append(_item5)
   
   def _fightIdFunc(self,input) :
      self.fightId = input.readVarUhShort()
      if(self.fightId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.fightId) + ") on element of FightCommonInformations.fightId.")
   
   def _fightTypeFunc(self,input) :
      self.fightType = input.readByte()
      if(self.fightType < 0) :
         raise RuntimeError("Forbidden value (" + str(self.fightType) + ") on element of FightCommonInformations.fightType.")

   def resume(self):
      print("fightId :",self.fightId)
      print("fightType :",self.fightType)
      for e in self.fightTeams:
         e.resume()
      print("fightTeamsPositions :",self.fightTeamsPositions)
      for e in self.fightTeamsOptions:
         e.resume()
