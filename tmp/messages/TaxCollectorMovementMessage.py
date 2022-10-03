from tmp.types.TaxCollectorBasicInformations import TaxCollectorBasicInformations
class TaxCollectorMovementMessage:
   def __init__(self,input):
      self._movementTypeFunc(input)
      self.basicInfos = TaxCollectorBasicInformations(input)
      self._playerIdFunc(input)
      self._playerNameFunc(input)
   
   def _movementTypeFunc(self,input) :
      self.movementType = input.readByte()
      if(self.movementType < 0) :
         raise RuntimeError("Forbidden value (" + self.movementType + ") on element of TaxCollectorMovementMessage.movementType.")
   
   def _playerIdFunc(self,input) :
      self.playerId = input.readVarUhLong()
      if(self.playerId < 0 or self.playerId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.playerId + ") on element of TaxCollectorMovementMessage.playerId.")
   
   def _playerNameFunc(self,input) :
      self.playerName = input.readUTF()