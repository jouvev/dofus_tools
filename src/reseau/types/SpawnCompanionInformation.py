from src.reseau.types.SpawnInformation import SpawnInformation

class SpawnCompanionInformation(SpawnInformation):
   def __init__(self,input):
      super().__init__(input)
      self._modelIdFunc(input)
      self._levelFunc(input)
      self._summonerIdFunc(input)
      self._ownerIdFunc(input)
   
   def _modelIdFunc(self,input) :
      self.modelId = input.readByte()
      if(self.modelId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.modelId) + ") on element of SpawnCompanionInformation.modelId.")
   
   def _levelFunc(self,input) :
      self.level = input.readVarUhShort()
      if(self.level < 1 or self.level > 200) :
         raise RuntimeError("Forbidden value (" + str(self.level) + ") on element of SpawnCompanionInformation.level.")
   
   def _summonerIdFunc(self,input) :
      self.summonerId = input.readDouble()
      if(self.summonerId < -9007199254740992 or self.summonerId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.summonerId) + ") on element of SpawnCompanionInformation.summonerId.")
   
   def _ownerIdFunc(self,input) :
      self.ownerId = input.readDouble()
      if(self.ownerId < -9007199254740992 or self.ownerId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.ownerId) + ") on element of SpawnCompanionInformation.ownerId.")

   def resume(self):
      super().resume()
      print("modelId :",self.modelId)
      print("level :",self.level)
      print("summonerId :",self.summonerId)
      print("ownerId :",self.ownerId)
