from src.reseau.types.FightStartingPositions import FightStartingPositions

class MapFightStartPositionsUpdateMessage:
   def __init__(self,input):
      self._mapIdFunc(input)
      self.fightStartPositions = FightStartingPositions(input)
   
   def _mapIdFunc(self,input) :
      self.mapId = input.readDouble()
      if(self.mapId < 0 or self.mapId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.mapId) + ") on element of MapFightStartPositionsUpdateMessage.mapId.")

   def resume(self):
      print("mapId :",self.mapId)
      self.fightStartPositions.resum()
