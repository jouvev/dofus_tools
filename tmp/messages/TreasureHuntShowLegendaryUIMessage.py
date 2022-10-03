class TreasureHuntShowLegendaryUIMessage:
   def __init__(self,input):
      self.availableLegendaryIds = []
      _val1 = 0
      _availableLegendaryIdsLen = input.readUnsignedShort()
      for _i1 in range(0,_availableLegendaryIdsLen):
         _val1 = input.readVarUhShort()
         if(_val1 < 0) :
            raise RuntimeError("Forbidden value (" + _val1 + ") on elements of availableLegendaryIds.")
         self.availableLegendaryIds.append(_val1)