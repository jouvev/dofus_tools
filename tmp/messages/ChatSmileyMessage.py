class ChatSmileyMessage:
   def __init__(self,input):
      self._entityIdFunc(input)
      self._smileyIdFunc(input)
      self._accountIdFunc(input)
   
   def _entityIdFunc(self,input) :
      self.entityId = input.readDouble()
      if(self.entityId < -9007199254740992 or self.entityId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.entityId + ") on element of ChatSmileyMessage.entityId.")
   
   def _smileyIdFunc(self,input) :
      self.smileyId = input.readVarUhShort()
      if(self.smileyId < 0) :
         raise RuntimeError("Forbidden value (" + self.smileyId + ") on element of ChatSmileyMessage.smileyId.")
   
   def _accountIdFunc(self,input) :
      self.accountId = input.readInt()
      if(self.accountId < 0) :
         raise RuntimeError("Forbidden value (" + self.accountId + ") on element of ChatSmileyMessage.accountId.")