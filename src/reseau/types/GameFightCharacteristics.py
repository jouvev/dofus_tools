from src.reseau.types.CharacterCharacteristics import CharacterCharacteristics

class GameFightCharacteristics:
   def __init__(self,input):
      self.characteristics = CharacterCharacteristics(input)
      self._summonerFunc(input)
      self._summonedFunc(input)
      self._invisibilityStateFunc(input)
   
   def _summonerFunc(self,input) :
      self.summoner = input.readDouble()
      if(self.summoner < -9007199254740992 or self.summoner > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.summoner) + ") on element of GameFightCharacteristics.summoner.")
   
   def _summonedFunc(self,input) :
      self.summoned = input.readBoolean()
   
   def _invisibilityStateFunc(self,input) :
      self.invisibilityState = input.readByte()
      if(self.invisibilityState < 0) :
         raise RuntimeError("Forbidden value (" + str(self.invisibilityState) + ") on element of GameFightCharacteristics.invisibilityState.")

   def resume(self):
      print("summoner :",self.summoner)
      print("summoned :",self.summoned)
      print("invisibilityState :",self.invisibilityState)
      self.characteristics.resume()
