import tmp.TypesFactory as pf
from tmp.types.ActorRestrictionsInformations import ActorRestrictionsInformations
class HumanInformations:
   def __init__(self,input):
      self.options = []
      _id3 = 0
      _item3 = None
      self.restrictions = ActorRestrictionsInformations(input)
      self._sexFunc(input)
      _optionsLen = input.readUnsignedShort()
      for _i3 in range(0,_optionsLen):
         _id3 = input.readUnsignedShort()
         _item3 = pf.TypesFactory.get_instance_id(_id3,input)
         self.options.append(_item3)
   
   def _sexFunc(self,input) :
      self.sex = input.readBoolean()