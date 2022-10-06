from src.reseau.types.EntityLook import EntityLook

class ContactLookMessage:
   def __init__(self,input):
      self._requestIdFunc(input)
      self._playerNameFunc(input)
      self._playerIdFunc(input)
      self.look = EntityLook(input)
   
   def _requestIdFunc(self,input) :
      self.requestId = input.readVarUhInt()
      if(self.requestId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.requestId) + ") on element of ContactLookMessage.requestId.")
   
   def _playerNameFunc(self,input) :
      self.playerName = input.readUTF()
   
   def _playerIdFunc(self,input) :
      self.playerId = input.readVarUhLong()
      if(self.playerId < 0 or self.playerId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.playerId) + ") on element of ContactLookMessage.playerId.")

   def resume(self):
      print("requestId :",self.requestId)
      print("playerName :",self.playerName)
      print("playerId :",self.playerId)
      self.look.resum()
