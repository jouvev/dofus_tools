from tmp.types.FightDispellableEffectExtendedInformations import FightDispellableEffectExtendedInformations
from tmp.types.GameActionMark import GameActionMark
from tmp.types.Idol import Idol
from tmp.types.GameFightEffectTriggerCount import GameFightEffectTriggerCount
class GameFightSpectateMessage:
   def __init__(self,input):
      self.effects = []
      self.marks = []
      self.idols = []
      self.fxTriggerCounts = []
      _item1 = None
      _item2 = None
      _item5 = None
      _item6 = None
      _effectsLen = input.readUnsignedShort()
      for _i1 in range(0,_effectsLen):
         _item1 = FightDispellableEffectExtendedInformations(input)
         self.effects.append(_item1)
      _marksLen = input.readUnsignedShort()
      for _i2 in range(0,_marksLen):
         _item2 = GameActionMark(input)
         self.marks.append(_item2)
      self._gameTurnFunc(input)
      self._fightStartFunc(input)
      _idolsLen = input.readUnsignedShort()
      for _i5 in range(0,_idolsLen):
         _item5 = Idol(input)
         self.idols.append(_item5)
      _fxTriggerCountsLen = input.readUnsignedShort()
      for _i6 in range(0,_fxTriggerCountsLen):
         _item6 = GameFightEffectTriggerCount(input)
         self.fxTriggerCounts.append(_item6)
   
   def _gameTurnFunc(self,input) :
      self.gameTurn = input.readVarUhShort()
      if(self.gameTurn < 0) :
         raise RuntimeError("Forbidden value (" + self.gameTurn + ") on element of GameFightSpectateMessage.gameTurn.")
   
   def _fightStartFunc(self,input) :
      self.fightStart = input.readInt()
      if(self.fightStart < 0) :
         raise RuntimeError("Forbidden value (" + self.fightStart + ") on element of GameFightSpectateMessage.fightStart.")