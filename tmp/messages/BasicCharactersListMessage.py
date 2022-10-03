import tmp.TypesFactory as pf
class BasicCharactersListMessage:
   def __init__(self,input):
      self.characters = []
      _id1 = 0
      _item1 = None
      _charactersLen = input.readUnsignedShort()
      for _i1 in range(0,_charactersLen):
         _id1 = input.readUnsignedShort()
         _item1 = pf.TypesFactory.get_instance_id(_id1,input)
         self.characters.append(_item1)