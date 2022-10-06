class JobCrafterDirectoryRemoveMessage:
   def __init__(self,input):
      self._jobIdFunc(input)
      self._playerIdFunc(input)
   
   def _jobIdFunc(self,input) :
      self.jobId = input.readByte()
      if(self.jobId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.jobId) + ") on element of JobCrafterDirectoryRemoveMessage.jobId.")
   
   def _playerIdFunc(self,input) :
      self.playerId = input.readVarUhLong()
      if(self.playerId < 0 or self.playerId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.playerId) + ") on element of JobCrafterDirectoryRemoveMessage.playerId.")

   def resume(self):
      print("jobId :",self.jobId)
      print("playerId :",self.playerId)
