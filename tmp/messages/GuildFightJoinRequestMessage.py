class GuildFightJoinRequestMessage:
   def __init__(self,input):
      self._taxCollectorIdFunc(input)
   
   def _taxCollectorIdFunc(self,input) :
      self.taxCollectorId = input.readDouble()
      if(self.taxCollectorId < 0 or self.taxCollectorId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.taxCollectorId + ") on element of GuildFightJoinRequestMessage.taxCollectorId.")