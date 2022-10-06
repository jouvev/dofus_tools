from src.reseau.types.FightTeamLightInformations import FightTeamLightInformations
from src.reseau.types.FightOptionsInformations import FightOptionsInformations

class FightExternalInformations:
   def __init__(self,input):
      self._fightIdFunc(input)
      self._fightTypeFunc(input)
      self._fightStartFunc(input)
      self._fightSpectatorLockedFunc(input)
      for _i5 in range(0,2):
         self.fightTeams[_i5] = FightTeamLightInformations(input)
      for _i6 in range(0,2):
         self.fightTeamsOptions[_i6] = FightOptionsInformations(input)
   
   def _fightIdFunc(self,input) :
      self.fightId = input.readVarUhShort()
      if(self.fightId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.fightId) + ") on element of FightExternalInformations.fightId.")
   
   def _fightTypeFunc(self,input) :
      self.fightType = input.readByte()
      if(self.fightType < 0) :
         raise RuntimeError("Forbidden value (" + str(self.fightType) + ") on element of FightExternalInformations.fightType.")
   
   def _fightStartFunc(self,input) :
      self.fightStart = input.readInt()
      if(self.fightStart < 0) :
         raise RuntimeError("Forbidden value (" + str(self.fightStart) + ") on element of FightExternalInformations.fightStart.")
   
   def _fightSpectatorLockedFunc(self,input) :
      self.fightSpectatorLocked = input.readBoolean()

   def resume(self):
      print("fightId :",self.fightId)
      print("fightType :",self.fightType)
      print("fightStart :",self.fightStart)
      print("fightSpectatorLocked :",self.fightSpectatorLocked)
