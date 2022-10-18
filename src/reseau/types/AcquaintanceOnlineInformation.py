import src.reseau.TypesFactory as pf
from src.reseau.types.AcquaintanceInformation import AcquaintanceInformation

class AcquaintanceOnlineInformation(AcquaintanceInformation):
   def __init__(self,input):
      super().__init__(input)
      self._playerIdFunc(input)
      self._playerNameFunc(input)
      self._moodSmileyIdFunc(input)
      _id4 = input.readUnsignedShort()
      self.status = pf.TypesFactory.get_instance_id(_id4,input)
   
   def _playerIdFunc(self,input) :
      self.playerId = input.readVarUhLong()
      if(self.playerId < 0 or self.playerId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.playerId) + ") on element of AcquaintanceOnlineInformation.playerId.")
   
   def _playerNameFunc(self,input) :
      self.playerName = input.readUTF()
   
   def _moodSmileyIdFunc(self,input) :
      self.moodSmileyId = input.readVarUhShort()
      if(self.moodSmileyId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.moodSmileyId) + ") on element of AcquaintanceOnlineInformation.moodSmileyId.")

   def resume(self):
      super().resume()
      print("playerId :",self.playerId)
      print("playerName :",self.playerName)
      print("moodSmileyId :",self.moodSmileyId)
      self.status.resume()
