from src.reseau.types.GuildRankMinimalInformation import GuildRankMinimalInformation

class GuildRankPublicInformation(GuildRankMinimalInformation):
   def __init__(self,input):
      super().__init__(input)
      self._orderFunc(input)
      self._gfxIdFunc(input)
   
   def _orderFunc(self,input) :
      self.order = input.readVarUhInt()
      if(self.order < 0) :
         raise RuntimeError("Forbidden value (" + str(self.order) + ") on element of GuildRankPublicInformation.order.")
   
   def _gfxIdFunc(self,input) :
      self.gfxId = input.readVarUhInt()
      if(self.gfxId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.gfxId) + ") on element of GuildRankPublicInformation.gfxId.")

   def resume(self):
      super().resume()
      print("order :",self.order)
      print("gfxId :",self.gfxId)
