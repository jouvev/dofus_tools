from tmp.types.EntityInformation import EntityInformation
class EntitiesInformationMessage:
   def __init__(self,input):
      self.entities = []
      _item1 = None
      _entitiesLen = input.readUnsignedShort()
      for _i1 in range(0,_entitiesLen):
         _item1 = EntityInformation(input)
         self.entities.append(_item1)