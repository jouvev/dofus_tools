class MountEmoteIconUsedOkMessage:
   def __init__(self,input):
      self._mountIdFunc(input)
      self._reactionTypeFunc(input)
   
   def _mountIdFunc(self,input) :
      self.mountId = input.readVarInt()
   
   def _reactionTypeFunc(self,input) :
      self.reactionType = input.readByte()
      if(self.reactionType < 0) :
         raise RuntimeError("Forbidden value (" + str(self.reactionType) + ") on element of MountEmoteIconUsedOkMessage.reactionType.")

   def resume(self):
      print("mountId :",self.mountId)
      print("reactionType :",self.reactionType)
