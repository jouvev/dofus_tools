import tmp.TypesFactory as pf
from tmp.types.NamedPartyTeamWithOutcome import NamedPartyTeamWithOutcome
class GameFightEndMessage:
   def __init__(self,input):
      self.results = []
      self.namedPartyTeamsOutcomes = []
      _id4 = 0
      _item4 = None
      _item5 = None
      self._durationFunc(input)
      self._rewardRateFunc(input)
      self._lootShareLimitMalusFunc(input)
      _resultsLen = input.readUnsignedShort()
      for _i4 in range(0,_resultsLen):
         _id4 = input.readUnsignedShort()
         _item4 = pf.TypesFactory.get_instance_id(_id4,input)
         self.results.append(_item4)
      _namedPartyTeamsOutcomesLen = input.readUnsignedShort()
      for _i5 in range(0,_namedPartyTeamsOutcomesLen):
         _item5 = NamedPartyTeamWithOutcome(input)
         self.namedPartyTeamsOutcomes.append(_item5)
   
   def _durationFunc(self,input) :
      self.duration = input.readInt()
      if(self.duration < 0) :
         raise RuntimeError("Forbidden value (" + self.duration + ") on element of GameFightEndMessage.duration.")
   
   def _rewardRateFunc(self,input) :
      self.rewardRate = input.readVarShort()
   
   def _lootShareLimitMalusFunc(self,input) :
      self.lootShareLimitMalus = input.readShort()