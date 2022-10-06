import tmp.TypesFactory as pf
from tmp.types.GameRolePlayNamedActorInformations import GameRolePlayNamedActorInformations

class GameRolePlayMerchantInformations(GameRolePlayNamedActorInformations):
   def __init__(self,input):
      self.options = []
      _id2 = 0
      _item2 = None
      super().__init__(input)
      self._sellTypeFunc(input)
      _optionsLen = input.readUnsignedShort()
      for _i2 in range(0,_optionsLen):
         _id2 = input.readUnsignedShort()
         _item2 = pf.TypesFactory.get_instance_id(_id2,input)
         self.options.append(_item2)
   
   def _sellTypeFunc(self,input) :
      self.sellType = input.readByte()
      if(self.sellType < 0) :
         raise RuntimeError("Forbidden value (" + str(self.sellType) + ") on element of GameRolePlayMerchantInformations.sellType.")

   def resume(self):
      super().resume()
      print("sellType :",self.sellType)
      for e in self.options:
         e.resume()
