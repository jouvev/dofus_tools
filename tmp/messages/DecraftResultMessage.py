from tmp.types.DecraftedItemStackInfo import DecraftedItemStackInfo
class DecraftResultMessage:
   def __init__(self,input):
      self.results = []
      _item1 = None
      _resultsLen = input.readUnsignedShort()
      for _i1 in range(0,_resultsLen):
         _item1 = DecraftedItemStackInfo(input)
         self.results.append(_item1)