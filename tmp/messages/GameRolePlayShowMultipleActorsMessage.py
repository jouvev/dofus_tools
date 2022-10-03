import tmp.TypesFactory as pf
class GameRolePlayShowMultipleActorsMessage:
   def __init__(self,input):
      self.informationsList = []
      _id1 = 0
      _item1 = None
      _informationsListLen = input.readUnsignedShort()
      for _i1 in range(0,_informationsListLen):
         _id1 = input.readUnsignedShort()
         _item1 = pf.TypesFactory.get_instance_id(_id1,input)
         self.informationsList.append(_item1)