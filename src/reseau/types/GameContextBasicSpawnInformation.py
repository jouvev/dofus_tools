import src.reseau.TypesFactory as pf

class GameContextBasicSpawnInformation:
   def __init__(self,input):
      self._teamIdFunc(input)
      self._aliveFunc(input)
      _id3 = input.readUnsignedShort()
      self.informations = pf.TypesFactory.get_instance_id(_id3,input)
   
   def _teamIdFunc(self,input) :
      self.teamId = input.readByte()
      if(self.teamId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.teamId) + ") on element of GameContextBasicSpawnInformation.teamId.")
   
   def _aliveFunc(self,input) :
      self.alive = input.readBoolean()

   def resume(self):
      print("teamId :",self.teamId)
      print("alive :",self.alive)
