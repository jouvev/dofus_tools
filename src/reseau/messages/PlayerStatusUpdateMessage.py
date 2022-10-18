import src.reseau.TypesFactory as pf

class PlayerStatusUpdateMessage:
   def __init__(self,input):
      self._accountIdFunc(input)
      self._playerIdFunc(input)
      _id3 = input.readUnsignedShort()
      self.status = pf.TypesFactory.get_instance_id(_id3,input)
   
   def _accountIdFunc(self,input) :
      self.accountId = input.readInt()
      if(self.accountId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.accountId) + ") on element of PlayerStatusUpdateMessage.accountId.")
   
   def _playerIdFunc(self,input) :
      self.playerId = input.readVarUhLong()
      if(self.playerId < 0 or self.playerId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.playerId) + ") on element of PlayerStatusUpdateMessage.playerId.")

   def resume(self):
      print("accountId :",self.accountId)
      print("playerId :",self.playerId)
      self.status.resume()
