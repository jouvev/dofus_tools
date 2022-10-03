import tmp.TypesFactory as pf
class ServerSessionConstantsMessage:
   def __init__(self,input):
      self.variables = []
      _id1 = 0
      _item1 = None
      _variablesLen = input.readUnsignedShort()
      for _i1 in range(0,_variablesLen):
         _id1 = input.readUnsignedShort()
         _item1 = pf.TypesFactory.get_instance_id(_id1,input)
         self.variables.append(_item1)