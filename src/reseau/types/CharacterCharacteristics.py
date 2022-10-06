import src.reseau.TypesFactory as pf

class CharacterCharacteristics:
   def __init__(self,input):
      self.characteristics = []
      _id1 = 0
      _item1 = None
      _characteristicsLen = input.readUnsignedShort()
      for _i1 in range(0,_characteristicsLen):
         _id1 = input.readUnsignedShort()
         _item1 = pf.TypesFactory.get_instance_id(_id1,input)
         self.characteristics.append(_item1)

   def resume(self):
      for e in self.characteristics:
         e.resume()
