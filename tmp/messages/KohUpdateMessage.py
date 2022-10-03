from tmp.types.AllianceInformations import AllianceInformations
from tmp.types.BasicAllianceInformations import BasicAllianceInformations
class KohUpdateMessage:
   def __init__(self,input):
      self.alliances = []
      self.allianceNbMembers = []
      self.allianceRoundWeigth = []
      self.allianceMatchScore = []
      self.allianceMapWinners = []
      _item1 = None
      _val2 = 0
      _val3 = 0
      _val4 = 0
      _item5 = None
      _alliancesLen = input.readUnsignedShort()
      for _i1 in range(0,_alliancesLen):
         _item1 = AllianceInformations(input)
         self.alliances.append(_item1)
      _allianceNbMembersLen = input.readUnsignedShort()
      for _i2 in range(0,_allianceNbMembersLen):
         _val2 = input.readVarUhShort()
         if(_val2 < 0) :
            raise RuntimeError("Forbidden value (" + _val2 + ") on elements of allianceNbMembers.")
         self.allianceNbMembers.append(_val2)
      _allianceRoundWeigthLen = input.readUnsignedShort()
      for _i3 in range(0,_allianceRoundWeigthLen):
         _val3 = input.readVarUhInt()
         if(_val3 < 0) :
            raise RuntimeError("Forbidden value (" + _val3 + ") on elements of allianceRoundWeigth.")
         self.allianceRoundWeigth.append(_val3)
      _allianceMatchScoreLen = input.readUnsignedShort()
      for _i4 in range(0,_allianceMatchScoreLen):
         _val4 = input.readByte()
         if(_val4 < 0) :
            raise RuntimeError("Forbidden value (" + _val4 + ") on elements of allianceMatchScore.")
         self.allianceMatchScore.append(_val4)
      _allianceMapWinnersLen = input.readUnsignedShort()
      for _i5 in range(0,_allianceMapWinnersLen):
         _item5 = BasicAllianceInformations(input)
         self.allianceMapWinners.append(_item5)
      self._allianceMapWinnerScoreFunc(input)
      self._allianceMapMyAllianceScoreFunc(input)
      self._nextTickTimeFunc(input)
   
   def _allianceMapWinnerScoreFunc(self,input) :
      self.allianceMapWinnerScore = input.readVarUhInt()
      if(self.allianceMapWinnerScore < 0) :
         raise RuntimeError("Forbidden value (" + self.allianceMapWinnerScore + ") on element of KohUpdateMessage.allianceMapWinnerScore.")
   
   def _allianceMapMyAllianceScoreFunc(self,input) :
      self.allianceMapMyAllianceScore = input.readVarUhInt()
      if(self.allianceMapMyAllianceScore < 0) :
         raise RuntimeError("Forbidden value (" + self.allianceMapMyAllianceScore + ") on element of KohUpdateMessage.allianceMapMyAllianceScore.")
   
   def _nextTickTimeFunc(self,input) :
      self.nextTickTime = input.readDouble()
      if(self.nextTickTime < 0 or self.nextTickTime > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.nextTickTime + ") on element of KohUpdateMessage.nextTickTime.")