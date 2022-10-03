import tmp.TypesFactory as pf
from tmp.types.CharacterMinimalGuildPublicInformations import CharacterMinimalGuildPublicInformations
class GuildFactsMessage:
   def __init__(self,input):
      self.members = []
      _item4 = None
      _id1 = input.readUnsignedShort()
      self.infos = pf.TypesFactory.get_instance_id(_id1,input)
      self._creationDateFunc(input)
      self._nbTaxCollectorsFunc(input)
      _membersLen = input.readUnsignedShort()
      for _i4 in range(0,_membersLen):
         _item4 = CharacterMinimalGuildPublicInformations(input)
         self.members.append(_item4)
   
   def _creationDateFunc(self,input) :
      self.creationDate = input.readInt()
      if(self.creationDate < 0) :
         raise RuntimeError("Forbidden value (" + self.creationDate + ") on element of GuildFactsMessage.creationDate.")
   
   def _nbTaxCollectorsFunc(self,input) :
      self.nbTaxCollectors = input.readVarUhShort()
      if(self.nbTaxCollectors < 0) :
         raise RuntimeError("Forbidden value (" + self.nbTaxCollectors + ") on element of GuildFactsMessage.nbTaxCollectors.")