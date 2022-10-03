import tmp.TypesFactory as pf
class InteractiveMapUpdateMessage:
   def __init__(self,input):
      self.interactiveElements = []
      _id1 = 0
      _item1 = None
      _interactiveElementsLen = input.readUnsignedShort()
      for _i1 in range(0,_interactiveElementsLen):
         _id1 = input.readUnsignedShort()
         _item1 = pf.TypesFactory.get_instance_id(_id1,input)
         self.interactiveElements.append(_item1)