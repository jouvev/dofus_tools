import tmp.TypesFactory as pf
class IgnoredListMessage:
   def __init__(self,input):
      self.ignoredList = []
      _id1 = 0
      _item1 = None
      _ignoredListLen = input.readUnsignedShort()
      for _i1 in range(0,_ignoredListLen):
         _id1 = input.readUnsignedShort()
         _item1 = pf.TypesFactory.get_instance_id(_id1,input)
         self.ignoredList.append(_item1)