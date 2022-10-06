from tmp.types.GameFightFighterLightInformations import GameFightFighterLightInformations

class GameFightFighterEntityLightInformation(GameFightFighterLightInformations):
   def __init__(self,input):
      super().__init__(input)
      self._entityModelIdFunc(input)
      self._masterIdFunc(input)
   
   def _entityModelIdFunc(self,input) :
      self.entityModelId = input.readByte()
      if(self.entityModelId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.entityModelId) + ") on element of GameFightFighterEntityLightInformation.entityModelId.")
   
   def _masterIdFunc(self,input) :
      self.masterId = input.readDouble()
      if(self.masterId < -9007199254740992 or self.masterId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.masterId) + ") on element of GameFightFighterEntityLightInformation.masterId.")

   def resume(self):
      super().resume()
      print("entityModelId :",self.entityModelId)
      print("masterId :",self.masterId)
