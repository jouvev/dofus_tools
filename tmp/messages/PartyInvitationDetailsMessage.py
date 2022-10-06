import tmp.TypesFactory as pf
from tmp.messages.AbstractPartyMessage import AbstractPartyMessage
from tmp.types.PartyGuestInformations import PartyGuestInformations

class PartyInvitationDetailsMessage(AbstractPartyMessage):
   def __init__(self,input):
      self.members = []
      self.guests = []
      _id6 = 0
      _item6 = None
      _item7 = None
      super().__init__(input)
      self._partyTypeFunc(input)
      self._partyNameFunc(input)
      self._fromIdFunc(input)
      self._fromNameFunc(input)
      self._leaderIdFunc(input)
      _membersLen = input.readUnsignedShort()
      for _i6 in range(0,_membersLen):
         _id6 = input.readUnsignedShort()
         _item6 = pf.TypesFactory.get_instance_id(_id6,input)
         self.members.append(_item6)
      _guestsLen = input.readUnsignedShort()
      for _i7 in range(0,_guestsLen):
         _item7 = PartyGuestInformations(input)
         self.guests.append(_item7)
   
   def _partyTypeFunc(self,input) :
      self.partyType = input.readByte()
      if(self.partyType < 0) :
         raise RuntimeError("Forbidden value (" + str(self.partyType) + ") on element of PartyInvitationDetailsMessage.partyType.")
   
   def _partyNameFunc(self,input) :
      self.partyName = input.readUTF()
   
   def _fromIdFunc(self,input) :
      self.fromId = input.readVarUhLong()
      if(self.fromId < 0 or self.fromId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.fromId) + ") on element of PartyInvitationDetailsMessage.fromId.")
   
   def _fromNameFunc(self,input) :
      self.fromName = input.readUTF()
   
   def _leaderIdFunc(self,input) :
      self.leaderId = input.readVarUhLong()
      if(self.leaderId < 0 or self.leaderId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.leaderId) + ") on element of PartyInvitationDetailsMessage.leaderId.")

   def resume(self):
      super().resume()
      print("partyType :",self.partyType)
      print("partyName :",self.partyName)
      print("fromId :",self.fromId)
      print("fromName :",self.fromName)
      print("leaderId :",self.leaderId)
      for e in self.members:
         e.resume()
      for e in self.guests:
         e.resume()
