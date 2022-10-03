import tmp.TypesFactory as pf
class PresetsMessage:
   def __init__(self,input):
      self.presets = []
      _id1 = 0
      _item1 = None
      _presetsLen = input.readUnsignedShort()
      for _i1 in range(0,_presetsLen):
         _id1 = input.readUnsignedShort()
         _item1 = pf.TypesFactory.get_instance_id(_id1,input)
         self.presets.append(_item1)