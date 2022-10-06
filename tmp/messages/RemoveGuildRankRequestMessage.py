class RemoveGuildRankRequestMessage:
   def __init__(self,input):
      self._rankIdFunc(input)
      self._newRankIdFunc(input)
   
   def _rankIdFunc(self,input) :
      self.rankId = input.readVarUhInt()
      if(self.rankId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.rankId) + ") on element of RemoveGuildRankRequestMessage.rankId.")
   
   def _newRankIdFunc(self,input) :
      self.newRankId = input.readVarUhInt()
      if(self.newRankId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.newRankId) + ") on element of RemoveGuildRankRequestMessage.newRankId.")

   def resume(self):
      print("rankId :",self.rankId)
      print("newRankId :",self.newRankId)
