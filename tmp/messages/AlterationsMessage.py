from tmp.types.AlterationInfo import AlterationInfo
class AlterationsMessage:
   def __init__(self,input):
      self.alterations = []
      _item1 = None
      _alterationsLen = input.readUnsignedShort()
      for _i1 in range(0,_alterationsLen):
         _item1 = AlterationInfo(input)
         self.alterations.append(_item1)