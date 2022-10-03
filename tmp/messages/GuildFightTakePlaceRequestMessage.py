from tmp.messages.GuildFightJoinRequestMessage import GuildFightJoinRequestMessage
class GuildFightTakePlaceRequestMessage(GuildFightJoinRequestMessage):
   def __init__(self,input):
      super().__init__(input)
      self._replacedCharacterIdFunc(input)
   
   def _replacedCharacterIdFunc(self,input) :
      self.replacedCharacterId = input.readVarUhLong()
      if(self.replacedCharacterId < 0 or self.replacedCharacterId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.replacedCharacterId + ") on element of GuildFightTakePlaceRequestMessage.replacedCharacterId.")