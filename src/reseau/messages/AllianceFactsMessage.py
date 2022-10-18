import src.reseau.TypesFactory as pf
from src.reseau.types.GuildInAllianceInformations import GuildInAllianceInformations

class AllianceFactsMessage:
   def __init__(self,input):
      self.guilds = []
      self.controlledSubareaIds = []
      _item2 = None
      _val3 = 0
      _id1 = input.readUnsignedShort()
      self.infos = pf.TypesFactory.get_instance_id(_id1,input)
      _guildsLen = input.readUnsignedShort()
      for _i2 in range(0,_guildsLen):
         _item2 = GuildInAllianceInformations(input)
         self.guilds.append(_item2)
      _controlledSubareaIdsLen = input.readUnsignedShort()
      for _i3 in range(0,_controlledSubareaIdsLen):
         _val3 = input.readVarUhShort()
         if(_val3 < 0) :
            raise RuntimeError("Forbidden value (" + _val3 + ") on elements of controlledSubareaIds.")
         self.controlledSubareaIds.append(_val3)
      self._leaderCharacterIdFunc(input)
      self._leaderCharacterNameFunc(input)
   
   def _leaderCharacterIdFunc(self,input) :
      self.leaderCharacterId = input.readVarUhLong()
      if(self.leaderCharacterId < 0 or self.leaderCharacterId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.leaderCharacterId) + ") on element of AllianceFactsMessage.leaderCharacterId.")
   
   def _leaderCharacterNameFunc(self,input) :
      self.leaderCharacterName = input.readUTF()

   def resume(self):
      print("leaderCharacterId :",self.leaderCharacterId)
      print("leaderCharacterName :",self.leaderCharacterName)
      self.infos.resume()
      for e in self.guilds:
         e.resume()
      print("controlledSubareaIds :",self.controlledSubareaIds)
