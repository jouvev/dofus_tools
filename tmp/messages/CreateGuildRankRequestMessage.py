class CreateGuildRankRequestMessage:
   def __init__(self,input):
      self._parentRankIdFunc(input)
      self._gfxIdFunc(input)
      self._nameFunc(input)
   
   def _parentRankIdFunc(self,input) :
      self.parentRankId = input.readVarUhInt()
      if(self.parentRankId < 0) :
         raise RuntimeError("Forbidden value (" + self.parentRankId + ") on element of CreateGuildRankRequestMessage.parentRankId.")
   
   def _gfxIdFunc(self,input) :
      self.gfxId = input.readVarUhInt()
      if(self.gfxId < 0) :
         raise RuntimeError("Forbidden value (" + self.gfxId + ") on element of CreateGuildRankRequestMessage.gfxId.")
   
   def _nameFunc(self,input) :
      self.name = input.readUTF()