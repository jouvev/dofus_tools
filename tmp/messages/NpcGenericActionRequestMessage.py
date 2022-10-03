class NpcGenericActionRequestMessage:
   def __init__(self,input):
      self._npcIdFunc(input)
      self._npcActionIdFunc(input)
      self._npcMapIdFunc(input)
   
   def _npcIdFunc(self,input) :
      self.npcId = input.readInt()
   
   def _npcActionIdFunc(self,input) :
      self.npcActionId = input.readByte()
      if(self.npcActionId < 0) :
         raise RuntimeError("Forbidden value (" + self.npcActionId + ") on element of NpcGenericActionRequestMessage.npcActionId.")
   
   def _npcMapIdFunc(self,input) :
      self.npcMapId = input.readDouble()
      if(self.npcMapId < 0 or self.npcMapId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.npcMapId + ") on element of NpcGenericActionRequestMessage.npcMapId.")