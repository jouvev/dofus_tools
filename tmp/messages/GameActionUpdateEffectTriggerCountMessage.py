from tmp.types.GameFightEffectTriggerCount import GameFightEffectTriggerCount
class GameActionUpdateEffectTriggerCountMessage:
   def __init__(self,input):
      self.targetIds = []
      _item1 = None
      _targetIdsLen = input.readUnsignedShort()
      for _i1 in range(0,_targetIdsLen):
         _item1 = GameFightEffectTriggerCount(input)
         self.targetIds.append(_item1)