class GuildFightLeaveRequestMessage:
   def __init__(self,input):
      self._taxCollectorIdFunc(input)
      self._characterIdFunc(input)
   
   def _taxCollectorIdFunc(self,input) :
      self.taxCollectorId = input.readDouble()
      if(self.taxCollectorId < 0 or self.taxCollectorId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.taxCollectorId) + ") on element of GuildFightLeaveRequestMessage.taxCollectorId.")
   
   def _characterIdFunc(self,input) :
      self.characterId = input.readVarUhLong()
      if(self.characterId < 0 or self.characterId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.characterId) + ") on element of GuildFightLeaveRequestMessage.characterId.")

   def resume(self):
      print("taxCollectorId :",self.taxCollectorId)
      print("characterId :",self.characterId)
