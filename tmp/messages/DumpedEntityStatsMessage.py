from tmp.types.CharacterCharacteristics import CharacterCharacteristics

class DumpedEntityStatsMessage:
   def __init__(self,input):
      self._actorIdFunc(input)
      self.stats = CharacterCharacteristics(input)
   
   def _actorIdFunc(self,input) :
      self.actorId = input.readDouble()
      if(self.actorId < -9007199254740992 or self.actorId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.actorId) + ") on element of DumpedEntityStatsMessage.actorId.")

   def resume(self):
      print("actorId :",self.actorId)
      self.stats.resum()
