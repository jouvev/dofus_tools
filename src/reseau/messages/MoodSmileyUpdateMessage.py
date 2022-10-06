class MoodSmileyUpdateMessage:
   def __init__(self,input):
      self._accountIdFunc(input)
      self._playerIdFunc(input)
      self._smileyIdFunc(input)
   
   def _accountIdFunc(self,input) :
      self.accountId = input.readInt()
      if(self.accountId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.accountId) + ") on element of MoodSmileyUpdateMessage.accountId.")
   
   def _playerIdFunc(self,input) :
      self.playerId = input.readVarUhLong()
      if(self.playerId < 0 or self.playerId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.playerId) + ") on element of MoodSmileyUpdateMessage.playerId.")
   
   def _smileyIdFunc(self,input) :
      self.smileyId = input.readVarUhShort()
      if(self.smileyId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.smileyId) + ") on element of MoodSmileyUpdateMessage.smileyId.")

   def resume(self):
      print("accountId :",self.accountId)
      print("playerId :",self.playerId)
      print("smileyId :",self.smileyId)
