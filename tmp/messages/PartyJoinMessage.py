import tmp.TypesFactory as pf
from tmp.messages.AbstractPartyMessage import AbstractPartyMessage
from tmp.types.PartyGuestInformations import PartyGuestInformations
class PartyJoinMessage(AbstractPartyMessage):
   def __init__(self,input):
      self.members = []
      self.guests = []
      _id4 = 0
      _item4 = None
      _item5 = None
      super().__init__(input)
      self._partyTypeFunc(input)
      self._partyLeaderIdFunc(input)
      self._maxParticipantsFunc(input)
      _membersLen = input.readUnsignedShort()
      for _i4 in range(0,_membersLen):
         _id4 = input.readUnsignedShort()
         _item4 = pf.TypesFactory.get_instance_id(_id4,input)
         self.members.append(_item4)
      _guestsLen = input.readUnsignedShort()
      for _i5 in range(0,_guestsLen):
         _item5 = PartyGuestInformations(input)
         self.guests.append(_item5)
      self._restrictedFunc(input)
      self._partyNameFunc(input)
   
   def _partyTypeFunc(self,input) :
      self.partyType = input.readByte()
      if(self.partyType < 0) :
         raise RuntimeError("Forbidden value (" + self.partyType + ") on element of PartyJoinMessage.partyType.")
   
   def _partyLeaderIdFunc(self,input) :
      self.partyLeaderId = input.readVarUhLong()
      if(self.partyLeaderId < 0 or self.partyLeaderId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.partyLeaderId + ") on element of PartyJoinMessage.partyLeaderId.")
   
   def _maxParticipantsFunc(self,input) :
      self.maxParticipants = input.readByte()
      if(self.maxParticipants < 0) :
         raise RuntimeError("Forbidden value (" + self.maxParticipants + ") on element of PartyJoinMessage.maxParticipants.")
   
   def _restrictedFunc(self,input) :
      self.restricted = input.readBoolean()
   
   def _partyNameFunc(self,input) :
      self.partyName = input.readUTF()