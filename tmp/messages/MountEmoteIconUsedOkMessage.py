class MountEmoteIconUsedOkMessage:
   def __init__(self,input):
      self._mountIdFunc(input)
      self._reactionTypeFunc(input)
   
   def _mountIdFunc(self,input) :
      self.mountId = input.readVarInt()
   
   def _reactionTypeFunc(self,input) :
      self.reactionType = input.readByte()
      if(self.reactionType < 0) :
         raise RuntimeError("Forbidden value (" + self.reactionType + ") on element of MountEmoteIconUsedOkMessage.reactionType.")