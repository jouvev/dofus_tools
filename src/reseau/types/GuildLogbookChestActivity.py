from src.reseau.types.ObjectItemNotInContainer import ObjectItemNotInContainer
from src.reseau.types.GuildLogbookEntryBasicInformation import GuildLogbookEntryBasicInformation

class GuildLogbookChestActivity(GuildLogbookEntryBasicInformation):
   def __init__(self,input):
      super().__init__(input)
      self._playerIdFunc(input)
      self._playerNameFunc(input)
      self._eventTypeFunc(input)
      self._quantityFunc(input)
      self.object = ObjectItemNotInContainer(input)
      self._sourceTabIdFunc(input)
      self._destinationTabIdFunc(input)
   
   def _playerIdFunc(self,input) :
      self.playerId = input.readVarUhLong()
      if(self.playerId < 0 or self.playerId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.playerId) + ") on element of GuildLogbookChestActivity.playerId.")
   
   def _playerNameFunc(self,input) :
      self.playerName = input.readUTF()
   
   def _eventTypeFunc(self,input) :
      self.eventType = input.readByte()
      if(self.eventType < 0) :
         raise RuntimeError("Forbidden value (" + str(self.eventType) + ") on element of GuildLogbookChestActivity.eventType.")
   
   def _quantityFunc(self,input) :
      self.quantity = input.readInt()
      if(self.quantity < 0) :
         raise RuntimeError("Forbidden value (" + str(self.quantity) + ") on element of GuildLogbookChestActivity.quantity.")
   
   def _sourceTabIdFunc(self,input) :
      self.sourceTabId = input.readInt()
      if(self.sourceTabId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.sourceTabId) + ") on element of GuildLogbookChestActivity.sourceTabId.")
   
   def _destinationTabIdFunc(self,input) :
      self.destinationTabId = input.readInt()
      if(self.destinationTabId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.destinationTabId) + ") on element of GuildLogbookChestActivity.destinationTabId.")

   def resume(self):
      super().resume()
      print("playerId :",self.playerId)
      print("playerName :",self.playerName)
      print("eventType :",self.eventType)
      print("quantity :",self.quantity)
      print("sourceTabId :",self.sourceTabId)
      print("destinationTabId :",self.destinationTabId)
      self.object.resume()
