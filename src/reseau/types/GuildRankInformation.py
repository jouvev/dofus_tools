from src.reseau.types.GuildRankMinimalInformation import GuildRankMinimalInformation

class GuildRankInformation(GuildRankMinimalInformation):
   def __init__(self,input):
      self.rights = []
      _val4 = 0
      super().__init__(input)
      self._orderFunc(input)
      self._gfxIdFunc(input)
      self._modifiableFunc(input)
      _rightsLen = input.readUnsignedShort()
      for _i4 in range(0,_rightsLen):
         _val4 = input.readVarUhInt()
         if(_val4 < 0) :
            raise RuntimeError("Forbidden value (" + _val4 + ") on elements of rights.")
         self.rights.append(_val4)
   
   def _orderFunc(self,input) :
      self.order = input.readVarUhInt()
      if(self.order < 0) :
         raise RuntimeError("Forbidden value (" + str(self.order) + ") on element of GuildRankInformation.order.")
   
   def _gfxIdFunc(self,input) :
      self.gfxId = input.readVarUhInt()
      if(self.gfxId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.gfxId) + ") on element of GuildRankInformation.gfxId.")
   
   def _modifiableFunc(self,input) :
      self.modifiable = input.readBoolean()

   def resume(self):
      super().resume()
      print("order :",self.order)
      print("gfxId :",self.gfxId)
      print("modifiable :",self.modifiable)
      print("rights :",self.rights)
